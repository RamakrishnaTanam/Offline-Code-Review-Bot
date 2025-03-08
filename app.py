import subprocess
from flask import Flask, request, render_template
import pygments
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

app = Flask(__name__)

def analyze_code(code_snippet):
    """Runs the CodeLlama model using Ollama to analyze the given code snippet."""
    try:
        command = f'echo "{code_snippet}" | ollama run codellama'
        response = subprocess.run(command, shell=True, capture_output=True, text=True)
        return response.stdout.strip() if response.stdout else "No response from AI."
    except Exception as e:
        return f"Error analyzing code: {str(e)}"

def format_code(code_snippet):
    """Formats the code snippet with syntax highlighting."""
    return pygments.highlight(code_snippet, PythonLexer(), HtmlFormatter())

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    formatted_code = ""
    if request.method == 'POST':
        code = request.form['code']
        if not code.strip():
            result = "Please enter some code to analyze."
        else:
            formatted_code = format_code(code)
            result = analyze_code(code)
    return render_template('index.html', result=result, formatted_code=formatted_code, formatter=HtmlFormatter())

if __name__ == '__main__':
    app.run(debug=True)
