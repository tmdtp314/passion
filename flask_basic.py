from flask import Flask, jsonify, request  #request: 파라미터 값을 flask안에서 사용하기 위해
app = Flask(__name__)

@app.route('/login')
def login():
    username = request.args.get('user_name') # get방식1
                                             # java의 변수 = request.getParameter('파라미터명')
    if username == 'Yoon':
        return_data = {'auth':'success'}
    else:
        return_data = {'auth':'failed'}
    return jsonify(return_data)

    if __name__ =="__main__":
        app.run(host='0.0.0.0',port='8082')

@app.route('/test2')
def test():
    return 'test'


