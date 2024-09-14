from flask import Flask, render_template, request, redirect, url_for
import os
from image_palette import gen_palette

app = Flask(__name__)

IMAGE_FOLDER = 'static/images'
app.config['IMAGE_FOLDER'] = IMAGE_FOLDER

if not os.path.exists(IMAGE_FOLDER):
    os.makedirs(IMAGE_FOLDER)

@app.route('/')
def index():
    return render_template('upload.html', image_url=None)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return "No file part"

    file = request.files['image']

    if file.filename == '':
        return "no selected file"

    if file:
        file_path = os.path.join(app.config['IMAGE_FOLDER'], file.filename)
        file.save(file_path)
        image_url = f'/{file_path}'
        palette_path = gen_palette(file.filename, file_path)
        palette_url = f'/{palette_path}'
        # return render_template('upload.html', image_url=image_url)
        return render_template('upload.html', image_url=image_url, palette_url=palette_url)

if __name__ == "__main__":
    app.run(debug=True)
