system_message = ""

def generate_prompt(question):
    prompt = f"""
    Can you answer my request: '{question}'
"""
    return prompt