from flask import Flask, render_template
app=Flask(__name__)
@app.route('/hello/<user>') # 변수값을 가져오기
def hello_name(user):
    return render_template('variable.html',name1=user, name2 ='YOON' ) # 폴더 경로!! html 파일이 꼭 template이라는 폴더 아래에 있어야 함

if __name__=='__main__':
    app.run(host='0.0.0.0',port='8082')