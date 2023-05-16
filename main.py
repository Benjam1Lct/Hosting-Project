import pipeline, tools
import os
import shutil
from flask import Flask, render_template, request, redirect, url_for
from flask_uploads import UploadSet, configure_uploads, IMAGES

keras_pipeline = pipeline.Pipeline()

application = Flask(__name__, template_folder='templates', static_folder='static')

application.config['UPLOADED_PHOTOS_DEST'] = 'uploads'
photos = UploadSet('photos', IMAGES)
configure_uploads(application, photos)

@application.route('/', methods=['GET', 'POST'])
def index():
    folder_path_del = "./static/uploads"
    file_list = os.listdir(folder_path_del)
    for file_name in file_list:
        file_path = os.path.join(folder_path_del, file_name)
        os.remove(file_path)
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        folder_path = 'uploads'
        files = os.listdir(folder_path)
        latest_file = None
        for file in files:
            if latest_file is None or os.path.getctime(os.path.join(folder_path, file)) > os.path.getctime(os.path.join(folder_path, latest_file)):
                latest_file = file
        if latest_file is not None:
            full_path = folder_path + '/' + latest_file
        predictions = keras_pipeline.recognize([full_path])
        ocr_text = ""
        for text, box in predictions[0]:
            ocr_text += text + " "
        print(ocr_text)
        src_file = full_path
        dst_folder = './static/uploads'
        shutil.move(src_file, dst_folder)
        directory = 'uploads'
        if os.path.exists(directory):
            shutil.rmtree(directory)
            print(f"Le dossier {directory} a été supprimé avec succès")
        else:
            print(f"Le dossier {directory} n'existe pas")
        folder_path_name = './static/uploads'
        files_name = os.listdir(folder_path_name)
        latest_file_name = None
        for file_name in files_name:
            if latest_file_name is None or os.path.getctime(os.path.join(folder_path_name, file_name)) > os.path.getctime(os.path.join(folder_path_name, latest_file_name)):
                latest_file_name = file_name
        return render_template('render.html', ocr_text=ocr_text, name=latest_file_name)
    return render_template('index.html')

@application.route('/renderTest')
def render():
    ocr_text = 'lorem ipsum dolor sit amet, consectetur adipiscing,lorem ipsum dolor sit amet, consecteturem ipsum dolor sit amet, consectetur adipiscing,lorem ipsum dolor sit amet, consecteturem ipsum dolor sit amet, consectetur adipiscing,lorem ipsum dolor sit amet, consecteturem ipsum dolor sit amet, consectetur adipiscing,lorem ipsum dolor sit amet, consecteturem ipsum dolor sit amet, consectetur adipiscing,lorem ipsum dolor sit amet, consecteturem ipsum dolor sit amet, consectetur adipiscing,lorem ipsum dolor sit amet, consectetur adipiscinglorem ipsum dolor sit amet, consectetur adiis '
    full_path = 'telechargement.png'
    return render_template('render.html', ocr_text=ocr_text, name=full_path)

@application.route('/connexion')
def connexion():
    
    return render_template('connexion.html')

@application.route('/inscription')
def inscription():
    return render_template('inscription.html')

@application.route('/mobile')
def mobile():
    return render_template('mobile.html')

@application.route('/blog')
def blog():
    return render_template('blog.html')

@application.route('/about_us')
def about_us():
    return render_template('about_us.html')

@application.route('/services')
def services():
    return render_template('services.html')


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=80, debug=True)