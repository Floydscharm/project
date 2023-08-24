from flask import Flask, render_template, send_from_directory, request
from fuzzywuzzy import fuzz
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/syllabus')
def syllabus():
    return render_template('syllabus.html')
@app.route('/choice')
def choice():
    return render_template('1.html')
@app.route('/list',methods=['POST'])
def list():
    dept=request.form.get('dept','')
    sem=request.form.get('sem','')
@app.route('/searchengine')
def searchengine():
    return render_template('searchengine.html')
@app.route('/search', methods=['POST'])
def search():
    search_term = request.form.get('search_term', '')
    pdf_files = []
    
    if search_term:
        documents_dir = os.path.join('static', 'Documents')
        for filename in os.listdir(documents_dir):
            if filename.lower().endswith('.pdf'):
                similarity_score = fuzz.partial_ratio(search_term.lower(), filename.lower())
                if similarity_score >= 70:
                    pdf_files.append(filename)
    
    return render_template('results.html', pdf_files=pdf_files, search_term=search_term)

@app.route('/download/<filename>')
def download(filename):
    documents_dir = os.path.join('static', 'Documents')
    return send_from_directory(documents_dir, filename)
if __name__ == '__main__':
    app.run(debug=True)
