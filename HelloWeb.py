from flask import Flask         # flask 모듈 가져옴

app = Flask(__name__)

@app.route('/')                 # 클라이언트가 ui창에다가 /로 접속하면  이 함수 호출
def hello():                    # /로 실행하면 호출되는 뷰 함수
    return "Hello Flask"       

@app.route('/name')
def name():
    return "내이름 신 머 홍"

@app.route('/age')
def age():
    return "age = 22"

@app.route('/job')
def job():
    return "직업 : 학생(백수)"

@app.route('/about')
def about():
    return "<p>이름 : 신대홍 </p> <p>나이 : 22 </p> 직업 없음"

if __name__ == "__main__":      # main문
    app.run(host="0.0.0.0",port = "8080") 