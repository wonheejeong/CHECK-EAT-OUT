from watson_developer_cloud import SpeechToTextV1
from watson_developer_cloud.websocket import RecognizeCallback
from os.path import join, dirname
import json

speech_to_text = SpeechToTextV1(
    username='e7a9eb3e-ab96-4456-9fc5-6d94831b4b8e',
    password='uENPXIuTACJy')


class MyRecognizeCallback(RecognizeCallback):
    def __init__(self):
        RecognizeCallback.__init__(self)

    def on_data(self, data):
        print(json.dumps(data, indent=2))

    def on_error(self, error):
        print('Error received: {}'.format(error))

    def on_inactivity_timeout(self, error):
        print('Inactivity timeout: {}'.format(error))


myRecognizeCallback = MyRecognizeCallback()
# join(dirname(__file__), './.', 'audio-file.flac'
with open("C:\\Users\\LS-COM-00025\\Downloads\\korean_hello.mp3",'rb') as audio_file:
    speech_to_text.recognize_with_websocket(
        audio=audio_file,
        content_type='audio/mp3',
        model='ko-KR_BroadbandModel',
        recognize_callback=myRecognizeCallback,
        interim_results=False,
        keywords=['colorado', 'tornado', 'tornadoes'],
        keywords_threshold=0.5,
        max_alternatives=3)
