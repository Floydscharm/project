from flask import Flask, render_template, send_from_directory, request
# from google.cloud import storage
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:\Downloads\neural-foundry-397208-848acb6822e5.json"

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
    if pdf_files:
        return render_template('results.html', pdf_files=pdf_files, dept=dept,sem=sem,documents_dir=documents_dir )
    else:
        return render_template('error.html')


# def upload_pdf_to_gcs(pdf_file, bucket_name, destination_blob_name):
#     """Uploads a PDF file to a Google Cloud Storage bucket."""
#     client = storage.Client()
#     bucket = client.get_bucket(bucket_name)
#     blob = bucket.blob(destination_blob_name)

#     with open(pdf_file, "rb") as pdf_data:
#         blob.upload_from_file(pdf_data, content_type="application/pdf")

# def download_pdf_from_gcs(bucket_name, blob_name, destination_file):
#     """Downloads a PDF file from a Google Cloud Storage bucket."""
#     client = storage.Client()
#     bucket = client.get_bucket(bucket_name)
#     blob = bucket.blob(blob_name)

#     with open(destination_file, "wb") as output_file:
#         blob.download_to_file(output_file)



@app.route('/download/<documents_dir>/<filename>')
def download(filename,documents_dir):
    return send_from_directory(documents_dir, filename)
if __name__ == '__main__':
    app.run(debug=True)
