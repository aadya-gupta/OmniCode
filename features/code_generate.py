from config import model

def generate_code(description):
    prompt = f'''You are an AI code generation tool. 
                Generate original and clean code with proper comments and a docstring.  
                Avoid copying existing solutions verbatim. 
                If no language is specified, use Python.  
                Write the code for the following task (ensure it's unique and beginner-friendly): {description}
                '''
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating code: {e}"
