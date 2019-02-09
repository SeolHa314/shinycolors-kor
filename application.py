# -*- encoding: utf-8 -*-
from flask import Flask, request, jsonify
from googletrans import Translator
from flask_cors import CORS, cross_origin
import requests, copy, json, os

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
    reqType = request.args.get('type')
    filename = "unknown"

    if reqType == "json":
        param = request.args.get('data')
        jsonData = json.loads(param) # 샤니 서버 json

        for i in jsonData:
            if 'id' in i:
                filename = str(i['id'])
                break
    elif reqType == "url":
        param = request.args.get('data')
        filename = param[param.rfind("/")+1:]
        data = requests.get(param).text
        jsonData = json.loads(data) # 샤니 서버 json

    url = "https://maxkss.github.io/shinycolors-helper/db.json" # 유저 번역 DB json
    data = requests.get(url).text
    db = json.loads(data)

    for i in jsonData:
        if 'text' in i and i['text'] in db:
            i['text-patch'] = db[i['text']]
        if 'select' in i and i['select'] in db:
            i['select-patch'] = db[i['select']]

    array = []
    for i in range(0, len(jsonData), 30):
        temp = ""
        for j in jsonData[i:i+30]:
            if 'text' in j:
                temp += j['text'] +"\n\n\n"
            if 'select' in j:
                temp += j['select']+"\n\n\n"
        array.append(temp)

    commuKo = ""
    for i in array: # 번역하기
        translator = Translator()
        result = (translator.translate(i, src = "ja", dest='ko').text) #번역하기
        commuKo += result+"\n\n\n"
    commuKo = commuKo.split('\n\n\n')

    try:
        with open(os.getcwd()+"/커뮤 대사 기록.json", 'r', -1, "UTF-8") as json_file:
            r = json.load(json_file)
    except:
        r = []

    temp = copy.deepcopy(jsonData)

    cnt = 0;
    for i in temp:
        if 'text' in i:
            i['text-ko'] = commuKo[cnt]
            cnt+=1
        if 'select' in i:
            i['select-ko'] = commuKo[cnt]
            cnt+=1

    cnt = 0;
    for i in jsonData:
        if 'text' in i:
            if 'text-patch' in i:
                i['text'] = i['text-patch']
                i.pop('text-patch')
            else:
                i['text'] = commuKo[cnt]
            cnt+=1
        if 'select' in i:
            if 'select-patch' in i:
                i['select'] = i['select-patch']
                i.pop('select-patch')
            else:
                i['select'] = commuKo[cnt]
            cnt+=1

    temp[0]['filename'] = filename
    jsonData[0]['filename'] = filename

    if len(r) == 0:
        r.append(temp)
    else:
        flag = True
        for i in r:
            if i[0]['filename'] == filename:
                flag = False
        if flag:
            r.append(temp)

    with open(os.getcwd()+'/커뮤 대사 기록.json', 'w+', -1, "UTF-8") as w:
        w.write(json.dumps(r, ensure_ascii = False, sort_keys=True, indent=4))
            

    return json.dumps(jsonData, ensure_ascii = False )

if __name__ == '__main__':
    print("샤니마스 한글패치 v2.3\n구동 시작했습니다 즐거운 샤니마스 되세요")
    print(os.getcwd())
    app.run(port=4030)