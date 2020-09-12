from flask import Flask, render_template, request  
  
app = Flask(__name__)  
 
@app.route("/")  
def index():  
     return render_template('index.html')  
 
 
  
@app.route('/hello', methods=['POST'])  
def hello():  
    Message = request.form['Message']  
    data=' %s ' % (Message)  
    return render_template('hello.html',value=data)  
     
  
  
if __name__ == '__main__':  
    #app.run(use_debugger=False, use_reloader=False, passthrough_errors=True)  
    app.run('localhost', 4459)  