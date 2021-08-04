from flask import Flask, request,make_response,jsonify
from flask.wrappers import Response


app=Flask(__name__)


@app.errorhandler(404)  # flask에서 제공해 주는 에러 핸들러 
def page_not_found(error):
    return "<h1>404 Error</h1>",404

@app.route('/google')
def get_google():
    response = request.get('http://www.google.co.kr')
    return response.text

if __name__ =='__main__':
    app.run(host='0.0.0.0',port='8081')