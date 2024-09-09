import os
from flask import Flask, render_template, request, redirect
from PyPDF2 import PdfReader

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'pdf' not in request.files:
            return redirect(request.url)

        file = request.files['pdf']
        
        if file.filename == '':
            return redirect(request.url)
        
        if file and file.filename.endswith('.pdf'):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            text = extract_text_from_pdf(filepath)

            return render_template('index.html', text=text)

    return render_template('index.html', text=None)

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ''
    
    for page in reader.pages:
        text += page.extract_text() + '\n'
    
    return text

if __name__ == '__main__':
    app.run(debug=True)
