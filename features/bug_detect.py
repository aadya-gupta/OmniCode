import subprocess
import tempfile
from config import model

analyzers = {
    "Python": ("Python", ["pylint", "--disable=all", "--enable=E,W"]),
    "JavaScript": ("eslint", ["eslint"]),
    "Java": ("checkstyle", ["checkstyle"]),
    "C++": ("cppcheck", ["cppcheck"]),
    "Go": ("golint", ["golint"]) 
}

def detect_language(code):
    prompt = f"Identify the programming language of the following code: {code}. Reply only with the language name."
    try:
        result = model.generate_content(prompt)
        return result.text.strip()
    except Exception:
        return "Unknown language."

def static_analyse(language, code_snippet):
    command = analyzers.get(language)

    if not command:
        return "No static analyzer available for this language."
    
    extensions = {"Python": ".py", "JavaScript": ".js", "Java": ".java", "C++": ".cpp", "Go": ".go"}
    file_ext = extensions.get(language, ".txt")
    
    with tempfile.NamedTemporaryFile(mode="w", suffix=file_ext, delete=False) as temp_file:
        temp_file.write(code_snippet)
        temp_path = temp_file.name
    
    try:
        result = subprocess.run(command + [temp_path], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception:
        return "Static analysis failed."


def detect_bug(code):
    lang = detect_language(code)
    static_report = static_analyse(lang, code)

    prompt =  f'''You are a bug detection tool.  
                Detect bugs in the following {lang} code. Use your reasoning and the static analyzer report to find issues.  
                Avoid using or referring to known copyrighted code.  
                Provide clear explanations and corrected code with proper comments.  
                Code:  
                --- {code} ---
                Static analysis report:  
                --- {static_report or "No issues found."} ---
                Politely decline any queries which are not related to bug detection in a code.'''
    try:
        final_response = model.generate_content(prompt)
        return lang, static_report, final_response.text.strip() 
    except Exception as e:
        return lang, static_report, f"Error detecting bugs: {e}"
