from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
import pandas as pd

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def data_load(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    try:
        df = pd.read_csv(file_path)
        return render_template('dataReview.html', filename=filename, graphData=df)
    except FileNotFoundError:
        return f"File {file_path} not found."
    except Exception as e:
        return str(e)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/<name>")
def hello_world(name=None):
    return render_template('index.html', person=name)

@app.route('/', methods=['GET', 'POST'])
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'the_file' not in request.files:
            return 'No file part'
        file = request.files['the_file']
        if file.filename == '':
            return 'No selected file'
        if file:
            original_filename = file.filename
            filename = original_filename.replace(" ", "_")
            secure_name = secure_filename(filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_name))
            return data_load(secure_name)
    return render_template('upload.html')


@app.route('/visualize')
def visualize():
    chart_type = request.args.get('chartType')
    x_axis = request.args.get('xAxis')
    y_axis = request.args.get('yAxis')
    filename = request.args.get('filename')

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    df = pd.read_csv(file_path)

    data = {
        'labels': df[x_axis].tolist(),
        'data': df[y_axis].tolist()
    }

    return jsonify(data)

if __name__ == "__main__":
    app.run(port=5000)