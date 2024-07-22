from flask import request, jsonify, current_app as app
from .models import db, Contract
from .services.nlp_service import generate_contract_code
from .services.contract_service import render_contract_template, compile_smart_contract
from .services.utils import sanitize_output

@app.route('/generate_contract', methods=['POST'])
def generate_contract():
    try:
        data = request.json
        user_input = data.get('user_input')
        if not user_input:
            return jsonify({"error": "User input is required"}), 400
        contract_code = generate_contract_code(user_input)
        contract_code = sanitize_output(contract_code)
        template_path = 'app/templates/smart_contract_template.sol'
        rendered_code = render_contract_template(template_path, {"contract_code": contract_code})
        compiled_code = compile_smart_contract(rendered_code)
        new_contract = Contract(user_input=user_input, contract_code=rendered_code)
        db.session.add(new_contract)
        db.session.commit()
        return jsonify({"contract_code": rendered_code, "compiled_code": compiled_code})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
