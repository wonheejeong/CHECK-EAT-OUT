import os
from flask import Flask, request, render_template
from werkzeug import secure_filename
import json
from collections import OrderedDict
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from watson_developer_cloud import SpeechToTextV1
from watson_developer_cloud.websocket import RecognizeCallback

UPLOAD_FOLDER = 'C:\\Users\\LS-COM-00025\\LifeSemantics\\flask\\CheckEatOut\\app\\user_image'
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


# upload

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
            image = ClImage(file_obj=open('C:\\Users\\LS-COM-00025\\LifeSemantics\\flask\\CheckEatOut\\app\\user_image\\'+filename,'rb'))
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
            return render_template("result.html",json = json.dumps(result, ensure_ascii=False, indent="\t"))


# app.add_url_rule('/uploads/<filename>', 'uploaded_file',
#                  build_only=True)
# app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
#     '/uploads':  app.config['UPLOAD_FOLDER']
# })


@app.route('/upload/voice', methods=['POST'])
def upload_voice_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # Using Voice API

            speech_to_text = SpeechToTextV1(
                username='e7a9eb3e-ab96-4456-9fc5-6d94831b4b8e',
                password='uENPXIuTACJy')
            print("1")
            myRecognizeCallback = MyRecognizeCallback()
            # join(dirname(__file__), './.', 'audio-file.flac'
            with open("C:\\Users\\LS-COM-00025\\LifeSemantics\\flask\\CheckEatOut\\app\\user_image\\"+filename, 'rb') as audio_file:
                speech_to_text.recognize_with_websocket(
                    audio=audio_file,
                    content_type='audio/mp3',
                    model='ko-KR_BroadbandModel',
                    recognize_callback=myRecognizeCallback,
                    interim_results=False,
                    keywords=['colorado', 'tornado', 'tornadoes'],
                    keywords_threshold=0.5,
                    max_alternatives=3)
            data = myRecognizeCallback.recognized_data
            return data

            # myRecognizeCallback.on_data()

# Run
if __name__ == '__main__':
    app.run(debug=True)