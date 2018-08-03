import os
from flask import Flask, request, render_template
from werkzeug import secure_filename
import json
from collections import OrderedDict
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import requests
from watson_developer_cloud.websocket import RecognizeCallback



UPLOAD_FOLDER = '/home/intern/check_eat_out/app/uploaded_files/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp3'])


class MyRecognizeCallback(RecognizeCallback):
    def __init__(self):
        self.recognized_data = ""
        RecognizeCallback.__init__(self)

    def on_data(self, data):
        # return render_template("result.html", json=json.dumps(data))
        # print(data["results"][0]["alternatives"][0])
        self.recognized_data = json.dumps(data, indent=2)
        # self.recognized_data = data

    def on_error(self, error):
        return ('Error received: {}'.format(error))

    def on_inactivity_timeout(self, error):
        return ('Inactivity timeout: {}'.format(error))


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
            result = OrderedDict()
            # output = OrderedDict()
            rank = []
            result["status"] = "Success"
            num = 1
            for i in concepts:
                rank.append({"ranknum": str(num), "name": i['name'], "value": str(round(i['value'] * 100, 2)) + '%'})
                num += 1

            result["output"] = rank
            return render_template("result.html",json = json.dumps(result, ensure_ascii=False, indent="\t"), file=file)



@app.route('/upload/voice', methods=['POST'])
def upload_voice_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # Using Voice API

            url = "https://stream.watsonplatform.net/speech-to-text/api/v1/recognize"
            username = 'e7a9eb3e-ab96-4456-9fc5-6d94831b4b8e'
            password = 'uENPXIuTACJy'


            filepath = UPLOAD_FOLDER+filename  # path to file
            filename = os.path.basename(filepath)

            audio = open(filepath, 'rb')

            files_input = {
                "audioFile": (filename, audio, 'audio/mp3')
            }

            r = requests.post(url, auth=(username, password),params={"model": "ko-KR_BroadbandModel", "max_alternatives": "5"}, headers={"Content-Type": "audio/mp3"}, files=files_input)
            response = json.loads(r.text)
            result = json.dumps(response)

            return render_template("result.html", json=result)


# Run
if __name__ == '__main__':
    app.run(debug=True)