import requests
import json
import os

url = "https://stream.watsonplatform.net/speech-to-text/api/v1/recognize"
username = 'e7a9eb3e-ab96-4456-9fc5-6d94831b4b8e'
password = 'uENPXIuTACJy'

headers={}

filepath = "C:\\Users\\LS-COM-00025\\LifeSemantics\\flask\\CheckEatOut\\app\\user_image\\hello.mp3"  # path to file
filename = os.path.basename(filepath)

audio = open(filepath, 'rb')

files_input = {
    "audioFile": (filename, audio, 'audio/mp3')
}

r = requests.post(url, auth=(username, password), params={"model" :"ko-KR_BroadbandModel", "max_alternatives":"5"},headers={"Content-Type": "audio/mp3"}, files=files_input)
# print((json.dumps(r)))
response = json.loads(r.text)
result=json.dumps(response)
print(type(result))
# print('stauts_code: {} (reason: {})'.format(response.status_code, response.reason))
#
# print (response.text)


#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?timestamps=true&word_alternatives_threshold=0.9&keywords=%22colorado%22%2C%22tornado%22%2C%22tornadoes%22&keywords_threshold=0.5', headers=headers, data=data, auth=('{username}', '{password}'))




# from watson_developer_cloud import SpeechToTextV1
# from watson_developer_cloud.websocket import RecognizeCallback
# import os
# from flask import Flask, request, render_template
# from werkzeug import secure_filename
# import json
# from collections import OrderedDict
# from clarifai.rest import ClarifaiApp
# from clarifai.rest import Image as ClImage
# from watson_developer_cloud import SpeechToTextV1
# from watson_developer_cloud.websocket import RecognizeCallback
#
#
# UPLOAD_FOLDER = 'C:\\Users\\LS-COM-00025\\LifeSemantics\\flask\\CheckEatOut\\app\\user_image'
# ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp3'])
#
#
# class MyRecognizeCallback(RecognizeCallback):
#     def __init__(self):
#         RecognizeCallback.__init__(self)
#
#     def on_data(self, data):
#         print(data)
#         # print(data["results"][0]["alternatives"][0])
#         # print(json.dumps(data, indent=2))
#
#     def on_error(self, error):
#         print('Error received: {}'.format(error))
#
#     def on_inactivity_timeout(self, error):
#         print('Inactivity timeout: {}'.format(error))
#
#
# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#
# # upload
#
# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
#
#
# @app.route('/upload/voice', methods=['POST'])
# def upload_voice_file():
#     if request.method == 'POST':
#         file = request.files['file']
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#
#             # Using Voice API
#             speech_to_text = SpeechToTextV1(
#                 username='e7a9eb3e-ab96-4456-9fc5-6d94831b4b8e',
#                 password='uENPXIuTACJy')
#
#
#             myRecognizeCallback = MyRecognizeCallback()
#             # join(dirname(__file__), './.', 'audio-file.flac'
#             with open('C:\\Users\\LS-COM-00025\\LifeSemantics\\flask\\CheckEatOut\\app\\user_image\\'+filename,'rb') as audio_file:
#                 speech_to_text.recognize_with_websocket(
#                     audio=audio_file,
#                     content_type='audio/mp3',
#                     model='ko-KR_BroadbandModel',
#                     recognize_callback=myRecognizeCallback,
#                     interim_results=False,
#                     keywords=['food'],
#                     keywords_threshold=0.5,
#                     max_alternatives=3)
#
#
#
# # from collections import OrderedDict
# # import json
# #
# # false= "false"
# # predict_json = {"status": {"code": 10000, "description": "Ok"}, "outputs": [{"id": "85d600bc281b41afa07b3ccedeaed7d4", "status": {"code": 10000, "description": "Ok"}, "created_at": "2018-08-01T01:38:42.751106085Z", "model": {"id": "food", "name": "food", "created_at": "2018-07-18T04:23:51.633274Z", "app_id": "e046ff71f7d34f318c2a260b98a367b2", "output_info": {"output_config": {"concepts_mutually_exclusive": false, "closed_environment": false}, "message": "Show output_info with: GET /models/{model_id}/output_info", "type": "concept", "type_ext": "concept"}, "model_version": {"id": "dc3cf4800da84fd5ac2043d4205f5b45", "created_at": "2018-07-18T05:10:51.786600Z", "status": {"code": 21100, "description": "Model trained successfully"}, "total_input_count": 58}}, "input": {"id": "cb6df155d215445b92f6f5b01806c1f4", "data": {"image": {"url": "https://s3.amazonaws.com/clarifai-api/img3/prod/small/f2ebaa207c62438789a5e4f843c5d3c5/d6d2547e6a7e8b6fd0f95d11b24c15ac", "base64": "dHJ1ZQ=="}}}, "data": {"concepts": [{"id": "lamyeon", "name": "lamyeon", "value": 1, "app_id": "e046ff71f7d34f318c2a260b98a367b2"}, {"id": "jajangmyeon", "name": "jajangmyeon", "value": 3.766251e-08, "app_id": "e046ff71f7d34f318c2a260b98a367b2"}, {"id": "ddukbokkie", "name": "ddukbokkie", "value": 1.6659797e-09, "app_id": "e046ff71f7d34f318c2a260b98a367b2"}]}}]}
# # outputs = predict_json["outputs"]
# # concepts = outputs[0]['data']['concepts']
# # result = OrderedDict()
# # output = OrderedDict()
# # rank = []
# #
# # result["status"] = "Success"
# # num = 1
# # for i in concepts:
# #     rank.append({"ranknum": str(num), "name": i['name'], "value": str(round(i['value'] * 100, 2)) + '%'})
# #     num += 1
# #
# # result["output"] = rank
# #
# #
# # print(json.dumps(result, ensure_ascii=False, indent="\t"))
#
# #
# # list = [1,2,3,4,5]
# # dict = {1:2, 2:3, 3:4}
# # print(str(dict))
#
#
#
# # for i in concepts:
# #     # result["output"] = []
# #     result["output"] =[{"ranknum": str(num), "name": i['name'], "value": str(round(i['value'] * 100, 2)) + '%'}]
# #     rank[num] ={"ranknum": str(num), "name": i['name'], "value": str(round(i['value'] * 100, 2)) + '%'}
# #     # [rank].append({"ranknum": str(num), "name": i['name'], "value": str(round(i['value'] * 100, 2)) + '%'})
# #     # result["output"] = {"ranknum": str(num), "name": i['name'], "value": str(round(i['value'] * 100, 2)) + '%'}
# #     # print(type(result["output"]))
# #     # result["output"].add({"ranknum": str(num), "name": i['name'], "value": str(round(i['value'] * 100, 2)) + '%'})
# #     # print([rank])
# #     # print(type([rank]))
# #     # sorce={"ranknum": str(num), "name": i['name'], "value": str(round(i['value'] * 100, 2)) + '%'}
# #     # list(rank).append(source)
# #     # print(list(rank))
# #     # print([rank])
# #
# #     num +=1
# #
# # result["output"]= rank
# #
# #
# #
# # print(json.dumps(result, ensure_ascii=False, indent="\t"))
#
#
# # -*- coding:utf-8 -*-
# import urllib3
# import json
# import base64
#
# # openApiURL = "http://aiopen.etri.re.kr:8000/WiseASR/Recognition"
# # accessKey = "4ae9530a-bb8d-4204-8dcb-097c5ec385ea"
# # audioFilePath = "C:\\Users\\LS-COM-00025\\LifeSemantics\\flask\\CheckEatOut\\app\\sample.mp3"
# # languageCode = "korean"
# #
# # file = open(audioFilePath, "rb")
# # audioContents = base64.b64encode(file.read()).decode("utf8")
# # file.close()
# #
# # requestJson = {
# #     "access_key": accessKey,
# #     "argument": {
# #         "language_code": languageCode,
# #         "audio": audioContents
# #     }
# # }
# #
# # http = urllib3.PoolManager()
# # response = http.request(
# #     "POST",
# #     openApiURL,
# #     headers={"Content-Type": "application/json; charset=UTF-8"},
# #     body=json.dumps(requestJson)
# # )
# #
# # print("[responseCode] " + str(response.status))
# # print("[responBody]")
# # print(response.data)