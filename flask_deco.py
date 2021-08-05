from flask import Flask
import requests

app = Flask(__name__)

@app.before_first_request
def before_first_request():
    print('flask 실행 후 첫 요청 때에만 실행')

@app.before_request
def before_request():
    print('HTTP 요청이 들어올 때마다 실행')

@app.after_request
def after_request(response):
    print('HTTP요청 처리가 끝나고 브라우저에 응답하기 전에 실행')
    print('response >>>>  ',response)
    return response
    # 해당 요청이 들어올 때마다 요청에 대한 실행이 끝나고 return을 통해 응답 데이터가 만들어지면 이를 웹브라우저에 응답하기 전에 실행
    # return response해야 함

@app.route('/hello')
def hello():
    print('hello')
    return "<h1>Hello Flask!</h>"

if __name__== '__main__':
    app.run(host='0.0.0.0', port='8080')