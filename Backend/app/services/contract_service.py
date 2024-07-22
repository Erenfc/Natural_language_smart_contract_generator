from jinja2 import Template
from solcx import compile_standard, install_solc
import json

def render_contract_template(template_path, context):
    with open(template_path, 'r') as file:
        template = Template(file.read())
    return template.render(context)

def compile_smart_contract(solidity_code):
    install_solc('0.8.19') 

    compiled_sol = compile_standard({
        "language": "Solidity",
        "sources": {
            "Contract.sol": {
                "content": solidity_code
            }
        },
        "settings": {
            "outputSelection": {
                "*": {
                    "*": [
                        "metadata",
                        "evm.bytecode",
                        "evm.bytecode.sourceMap",
                        "abi"
                    ]
                }
            }
        }
    })

    contracts = compiled_sol['contracts']['Contract.sol']
    contract_name = list(contracts.keys())[0] 
    contract_data = contracts[contract_name]

    bytecode = contract_data['evm']['bytecode']['object']
    abi = contract_data['abi']

    return {
        "bytecode": bytecode,
        "abi": abi,
        "compiled": json.dumps(compiled_sol, indent=4) 
    }

if __name__ == "__main__":
    solidity_code = """
    pragma solidity ^0.8.0;

    contract SimpleStorage {
        uint public storedData;

        function set(uint x) public {
            storedData = x;
        }

        function get() public view returns (uint) {
            return storedData;
        }
    }
    """

    result = compile_smart_contract(solidity_code)
    print(result)

