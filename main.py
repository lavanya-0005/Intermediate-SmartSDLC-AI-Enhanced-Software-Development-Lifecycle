from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def home():
    return "Welcome to SmartSDLC AI Backend"

@app.route('/upload', methods=['POST'])
def upload_requirements():
    file = request.files.get('file')
    if not file:
        return jsonify({'error': 'No file uploaded'}), 400
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    # Simulate classification
    return jsonify({'status': 'success', 'message': f'Requirements from {filename} classified into SDLC phases.'})

@app.route('/generate-code', methods=['POST'])
def generate_code():
    prompt = request.json.get('prompt', '')
    # Simulated response
    return jsonify({
        'generated_code': f"# Code generated for prompt: {prompt}\ndef example_function():\n    print('Hello from SmartSDLC!')"
    })

@app.route('/fix-bug', methods=['POST'])
def fix_bug():
    buggy_code = request.json.get('code', '')
    # Simulated fix
    return jsonify({
        'fixed_code': buggy_code.replace("pritn", "print")
    })

@app.route('/generate-tests', methods=['POST'])
def generate_tests():
    function_name = request.json.get('function', 'example_function')
    return jsonify({
        'test_code': f"import unittest\n\nclass Test{function_name.capitalize()}(unittest.TestCase):\n    def test_case(self):\n        self.assertTrue(True)\n\nif __name__ == '__main__':\n    unittest.main()"
    })

@app.route('/summarize-code', methods=['POST'])
def summarize_code():
    code = request.json.get('code', '')
    return jsonify({
        'summary': 'This function prints a greeting message to the console.'
    })

@app.route('/chatbot', methods=['POST'])
def chatbot():
    question = request.json.get('question', '')
    return jsonify({
        'response': f"You asked: '{question}'. Here’s a smart response from the AI assistant."
    })

if __name__ == '__main__':
    app.run(debug=True)
