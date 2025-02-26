from config import model 
from bug_detect import detect_language


def explanation(code):
    lang = detect_language(code)
    prompt = f'''You are a code explanation tool.  
                Explain the logic of the following {lang} code in simple, beginner-friendly terms.  
                Ensure the explanation is unique and avoids referencing publicly known solutions.  
                Include the language name in your explanation.  

                Code:  
                --- {code} ---'''
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error explaining code: {e}"
