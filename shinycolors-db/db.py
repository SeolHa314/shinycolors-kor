import json, traceback

def addCommu():
    try:
        with open("db.json", 'r', -1, "UTF-8") as json_file:
            db_r = json.load(json_file)
    except:
        traceback.print_exc()
        print("에러: db.json을 제대로 삽입했는지 확인해주세요")
    try:
        with open("add.json", 'r', -1, "UTF-8") as json_file:
            add_r = json.load(json_file)
    except:
        traceback.print_exc()
        print("에러: add.json을 제대로 삽입했는지 확인해주세요")
    for i in add_r:
        for j in i:
            if 'text' in j and 'text-patch' in j:
                if j['text'] in db_r:
                    print(j['text'] + " : " +j['text-patch']+" - 덮어씀")
                else:
                    print(j['text'] + " : " +j['text-patch']+" - 추가")
                db_r[j['text']] = j['text-patch']
            if 'select' in j and 'select-patch' in j:
                if j['select'] in db_r:
                    print(j['select'] + " : " +j['select-patch']+" - 덮어씀")
                else:
                    print(j['select'] + " : " +j['select-patch']+" - 추가")
                db_r[j['select']] = j['select-patch']

            # if 'text' in j and 'text-ko' in j:
            #     if j['text'] in db_r:
            #         print(j['text'] + " : " +j['text-ko']+" - 덮어씀")
            #     else:
            #         print(j['text'] + " : " +j['text-ko']+" - 추가")
            #     db_r[j['text']] = j['text-ko']

    try:
        with open('db.json', 'w+', -1, "UTF-8") as w:
            w.write(json.dumps(db_r, ensure_ascii = False, sort_keys=True, indent=4))
    except:
        print("에러: 파일을 덮어씌우는데 실패했습니다")

    print("\nfinish")
                    
    

if __name__ == '__main__':
    print("작업시작")
    addCommu()