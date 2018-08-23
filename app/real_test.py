from flask import Flask, request, render_template, url_for
from werkzeug import secure_filename
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from pydub import AudioSegment
import json, requests, os
from bs4 import BeautifulSoup

# from flaskr import init_db
# init_db()

UPLOAD_FOLDER = '/home/intern/check_eat_out/app/static/uploaded_files/'
# UPLOAD_FOLDER = 'C:\\Users\\LS-COM-00025\\LifeSemantics\\flask\\CheckEatOut\\app\\static\\uploaded_files\\'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp3', 'm4a', 'wav', 'mpeg', 'flac'])


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

def get_nutrition(query):
    url = 'http://apis.data.go.kr/1470000/FoodNtrIrdntInfoService/getFoodNtrItdntList?serviceKey=5gR2Yl0HMrZtrAyfCxoqBEGhVZZAQz8S7YwV0NHpE%2BJWewgStQHnEzze%2BKPEHJ3gHrlkg2RfKvASvVmsZulyAQ%3D%3D&desc_kor={}&pageNo=1&startPage=1&numOfRows=1&pageSize=1'.format(query)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table2 = soup.find("items")
    table = table2.findAll("item")
    result = []
    num = 0

    for i in table:
        text = table[num].findAll(text=True)
        for i in range(0, 11):
            result.insert(i, str(text[i * 2 + 1]))
            i += 1
        num += 1

    return result

@app.route('/upload/image', methods=['POST'])
def upload_image_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            try:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                # url = redirect(url_for('uploaded_file', filename=filename))

                # Using Image API
                app_api = ClarifaiApp(api_key='e635a47197fd4904b470507b9d3cde08')
                model = app_api.models.get('food')
                model.model_version = '27fc125e385846b1a9fbc69480c774db'
                image = ClImage(file_obj=open(UPLOAD_FOLDER+filename,'rb'))
                predict_json = model.predict([image])
                outputs = predict_json["outputs"]
                concepts = outputs[0]['data']['concepts']
                result_web = []
                result_get = []
                num = 0
                for i in concepts:
                    result_get.insert(num, i['name'])
                    result_web.insert(num, i['name'] + str(round(i['value'] * 100, 2)) + '%')
                    num += 1
                return render_template("image_result.html",json = result_web ,nutrition=get_nutrition(result_get[0]), filepath = url_for('static', filename= 'uploaded_files/'+filename))
            except:
                return render_template("error.html")




@app.route('/upload/voice', methods=['POST'])
def upload_voice_file():
    file = request.files['file']
    if file and allowed_file(file.filename):
        try:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filepath = UPLOAD_FOLDER + filename
            audiotype = filename.split(".")[1]
            if audiotype =='m4a':
                #Conver file (m4a to mp3)
                m4a_audio = AudioSegment.from_file(filepath, format="m4a")
                m4a_audio.export(filepath.replace((filepath).split('.')[-1], 'mp3'), format="mp3")
                os.remove(filepath)
                filename = filename.replace(str(filename.split(".")[1]), 'mp3')
                audiotype = 'mp3'
            else:
                filename = filename
            # Using Voice API
            url = "https://stream.watsonplatform.net/speech-to-text/api/v1/recognize"
            username = 'e7a9eb3e-ab96-4456-9fc5-6d94831b4b8e'
            password = 'uENPXIuTACJy'

            # path to file
            filepath = UPLOAD_FOLDER + filename
            audio = open(filepath, 'rb')
            files_input = {
                "audioFile": (filename, audio, 'audio/'+ audiotype)
            }
            r = requests.post(url, auth=(username, password),
                              params={"model": "ko-KR_BroadbandModel", "max_alternatives": "5"},
                              headers={"Content-Type": "audio/"+ audiotype }, files=files_input)
            response =json.loads(r.text)
            result_web = []
            result_get = []
            num = 0

            for i in response['results'][0]['alternatives']:
                result_web.insert(num, str(i["transcript"]))
                result_get.insert(num, str(i["transcript"]))
                num += 1
            return render_template("voice_result.html", json=result_web, nutrition=get_nutrition(result_get[0]), filepath = url_for('static', filename= 'uploaded_files/'+filename))
        except:
            return render_template("error.html")
        #TypeError -> 파일 형식 확인해주세요. KeyError->

# Run
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    # app.run(debug=True)