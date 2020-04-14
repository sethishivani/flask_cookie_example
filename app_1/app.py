from flask import Flask, render_template, request,make_response
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
      user = request.form['nm']
      resp = make_response(render_template('second.html'))
      resp.set_cookie('userID', user)
      return resp

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   if(name== None):
      return '<h1>Your Cache has been cleared</h1>'
   return '<h1>Your Cookie :{ '+name+' }</h1>'

if __name__ == '__main__':
   app.run()