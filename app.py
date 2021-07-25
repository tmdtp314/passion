from flask import Flask, jsonify, request, render_template  #request: 파라미터 값을 flask안에서 사용하기 위해
app = Flask(__name__,static_url_path='/static') # static_url_path 옵션으로 static 폴더에 부트스트랩 적용에 필요한 파일들을 몰아 넣는다!

@app.route('/login')
def login():
    email = request.args.get('email') # get방식1                                           # java의 변수 = request.getParameter('파라미터명')
    password = request.args.get('pw') # id값이 아닌 name 태그값이다!!!
    print(email,password)
   

    if email == 'tmdtp314@naver.com' and password=="1234":
        return_data = {'auth':'success'}
    else:
        return_data = {'auth':'failed'}
    
    return jsonify(return_data)
@app.route('/html_test')
def hello_html():
    return render_template('login_rawtest.html')


if __name__ =="__main__":
        app.run(host='0.0.0.0',port='8081')

print('__name__',__name__)

## Ctrl + C -> 종료