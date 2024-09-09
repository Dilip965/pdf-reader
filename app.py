from flask import Flask, render_template, request
import os
import PyPDF2

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    text = ""
    if request.method == "POST":
        pdf_file = request.files["pdf"]
        if pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text() + "\n"
    return render_template("index.html", text=text)

if __name__ == "__main__":
    # Bind to the port provided by the environment or use default (10000)
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
