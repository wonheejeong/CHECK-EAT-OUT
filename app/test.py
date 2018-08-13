from flask import Flask, request, render_template, url_for
from werkzeug import secure_filename
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from pydub import AudioSegment
import json, requests, os
# UPLOAD_FOLDER = '/home/intern/check_eat_out/app/static/uploaded_files/'
UPLOAD_FOLDER = 'C:\\Users\\LS-COM-00025\\LifeSemantics\\flask\\CheckEatOut\\app\\static\\user_image\\'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp3', 'm4a'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


# new

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS



@app.route('/upload/image', methods=['POST'])
def upload_image_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # url = redirect(url_for('uploaded_file', filename=filename))

            # Using Image API
            app_api = ClarifaiApp(api_key='e635a47197fd4904b470507b9d3cde08')
            model = app_api.models.get('food')
            model.model_version = 'dc3cf4800da84fd5ac2043d4205f5b45'
            image = ClImage(file_obj=open(UPLOAD_FOLDER+filename,'rb'))
            predict_json = model.predict([image])
            outputs = predict_json["outputs"]
            concepts = outputs[0]['data']['concepts']
            result = []
            num = 0
            for i in concepts:
                result.insert(num, i['name'] + str(round(i['value'] * 100, 2)) + '%')
                num += 1
            return render_template("image_result.html",json = result, filepath = url_for('static', filename= 'user_image/'+filename))



@app.route('/upload/voice', methods=['POST'])
def upload_voice_file():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        filepath = UPLOAD_FOLDER + filename
        #Conver file (m4a to mp3)
        m4a_audio = AudioSegment.from_file(filepath, format="m4a")
        m4a_audio.export(filepath.replace((filepath).split('.')[-1], 'mp3'), format="mp3")
        os.remove(filepath)
        # Using Voice API

        url = "https://stream.watsonplatform.net/speech-to-text/api/v1/recognize"
        username = 'e7a9eb3e-ab96-4456-9fc5-6d94831b4b8e'
        password = 'uENPXIuTACJy'

        # path to file

        new_filename = filename.replace(str(filename.split(".")[1]),'mp3')
        filepath = UPLOAD_FOLDER + new_filename
        filename = os.path.basename(filepath)
        audio = open(filepath, 'rb')
        files_input = {
            "audioFile": (filename, audio, 'audio/mp3')
        }
        r = requests.post(url, auth=(username, password),
                          params={"model": "ko-KR_BroadbandModel", "max_alternatives": "5"},
                          headers={"Content-Type": "audio/mp3"}, files=files_input)
        response =json.loads(r.text)
        result = []
        html = ""
        num = 0
        for i in response['results'][0]['alternatives']:
            # html += "<input type='button' value=" + str(i["transcript"]) + "/>"
            result.insert(num, str(i["transcript"]))
            num += 1
        return render_template("voice_result.html", json=result, filepath = url_for('static', filename= 'user_image/'+new_filename))


# Run
if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0')
    app.run(debug=True)