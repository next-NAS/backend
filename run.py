from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'data'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/dataset', methods=['POST'])
def post_file():
  # check if the post request has the file part
  if 'file' not in request.files:
    flash('No file part')
    return redirect(request.url)
  file = request.files['file']
  # if user does not select file, browser also
  # submit an empty part without filename
  if file.filename == '':
    flash('No selected file')
    return redirect(request.url)
  if file and allowed_file(file.filename):
    print(file.filename)
    print(request.form)
    directory = os.path.join(app.config['UPLOAD_FOLDER'], 
                          os.path.split(request.form['relativePath'])[0])
    if not os.path.isdir(directory):
      os.makedirs(directory, exist_ok=True)
    filename = secure_filename(file.filename)
    file.save(os.path.join(directory, filename))
    return '''ok'''

app.run(debug=True, port=8080)