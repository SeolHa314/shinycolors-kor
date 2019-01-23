# -*- encoding: utf-8 -*-
from flask import Flask, request, jsonify
from googletrans import Translator
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def main():
    return '샤이니컬러즈 한글패치!'

@app.route('/translate')
@cross_origin()
def translate():
    commuJa = request.args.get('commu').split('\n\n\n')
    temp = ['\n\n\n'.join(commuJa[i:i+30]) for i in range(0, len(commuJa), 30)]
    commuKo = ""
    for i in temp:
        translator = Translator()
        result = (translator.translate(i, src = "ja", dest='ko').text) #번역하기
        commuKo += result+"\n\n\n"
    
    commuKo = commuKo.split('\n\n\n')

    w = open("커뮤 대사 기록.txt", 'a', -1, "utf-8")
    r = open("커뮤 대사 기록.txt", 'r', -1, "utf-8")

    for i in range(0, len(commuKo)):
        log = "일어원본\n"+commuJa[i]+"\n\n한글 번역\n"+commuKo[i]+"\n\n\n\n"
        w.write(log)
            
    r.close()
    w.close()
    return jsonify(commuKo)

if __name__ == '__main__':
    print("샤니마스 한글패치 v1.0\n구동 시작했습니다 즐거운 샤니마스 되세요")
    app.run(port=4030)
