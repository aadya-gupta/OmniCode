from config import model

def gen_unit_test(code):
    prompt = f'''You are a unit test generation tool.  
                Generate **original** unit tests (at least 5) for the given code using the appropriate framework.  
                Ensure the tests are unique and do not replicate known public solutions. 
                Politely decline any queries which are not related to unit test generation in a code.
                ---
                {code}'''
    try:            
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating tests: {e}."
