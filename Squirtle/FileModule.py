#파일 입출력을 위한 모듈
import json, Data

#직렬화 파일 초기화
def InitialData(): 
    try:
        f = open('SaveData.json', 'r')
    except FileNotFoundError: #파일이 없을 시
        data = Data.Data(3600, 60, "Squirtle", "스트레칭을 해주세요", False, 0) #Data 객체 생성
        SaveFile = SerializationData(data.Sec, data.Term, data.Name, data.Content, data.AutoStart, data.Language)
        SaveData(SaveFile)
    else: #파일이 있을 시
        LoadFile = LoadData()
        data = Data.Data(LoadFile[0], LoadFile[1], LoadFile[2], LoadFile[3], LoadFile[4], LoadFile[5])
    return data

def SerializationData(Sec, Term, Name, Content, AutoStart, Language): #Data 직렬화
    DataList = [Sec, Term, Name, Content, AutoStart, Language]
    return json.dumps(DataList, ensure_ascii = False) #ensure_ascii = False 한글 깨짐 방지

#파일 저장 
def SaveData(data): #data = 직렬화된 파일
    #파일 쓰기
    f = open("SaveData.json", 'w')
    f.write(data)
    f.close()

#파일 읽기
def LoadData(): 
    try:
        f = open('SaveData.json', 'r')
    except FileNotFoundError: #파일이 없을 시
        print("No such SaveData.json")
    else: #파일이 있을 시
        data = f.read()
    return json.loads(data)