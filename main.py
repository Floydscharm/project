from flask import Flask, render_template, send_from_directory, request
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
    pdf_files=[]
    if sem=="1st" or sem=="2nd" :
        documents_dir = os.path.join('static', 'Documents',sem)
    else:
        documents_dir = os.path.join('static', 'Documents',dept,sem)
    for filename in os.listdir(documents_dir):
            if filename.lower().endswith('.pdf'):
                pdf_files.append(filename)
    return render_template('results.html', pdf_files=pdf_files, dept=dept,sem=sem,documents_dir=documents_dir )
@app.route('/download/<documents_dir>/<filename>')
def download(filename,documents_dir):
    return send_from_directory(documents_dir, filename)
if __name__ == '__main__':
    app.run(debug=True)
