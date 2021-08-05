from flask import Flask
import requests

app = Flask(__name__)

if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('yoon_server.log',maxBytes=2000,backupCount=10) #yoon_server.log파일은 해당 .py있는 폴더에 자동으로 저장된다. 
    file_handler.setLevel(logging.WARNING) # 어느 레벨까지 로깅 할건지
    app.logger.addHandler(file_handler) #app.logger.addHandler() 에 등록시켜줘야 app.logger로 사용 가능
    app.logger.addHandler(file_handler)

@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(error)
    return "<h1>404 Error</h1>",404

if __name__ =="__main__":
    app.run(host='0.0.0.0',port="8085") #debug 옵션을 설정해주었다. 

