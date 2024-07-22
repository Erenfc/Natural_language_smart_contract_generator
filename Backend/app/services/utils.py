def validate_user_input(user_input):
    if not user_input:
        raise ValueError("User input cannot be empty")
    return True

def sanitize_output(output):
    return output.strip()
