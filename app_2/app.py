from flask import Flask, render_template, request,make_response
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('first.html')

@app.route('/second')
def second():
   return render_template('second.html')

@app.route('/add1', methods = ['POST', 'GET'])
def add1():
   if request.method == 'POST':
      resp = make_response(render_template('first.html'))
      cart = request.cookies.get('cart')
      if(cart== None):
         cart=""
      cart= cart+" Item-1"
      resp.set_cookie('cart', cart)
      return resp

@app.route('/add2', methods = ['POST', 'GET'])
def add2():
   if request.method == 'POST':
      resp = make_response(render_template('first.html'))
      cart = request.cookies.get('cart')
      if(cart== None):
         cart=""
      cart= cart+" Item-2"
      resp.set_cookie('cart', cart)
      return resp

@app.route('/add3', methods = ['POST', 'GET'])
def add3():
   if request.method == 'POST':
      resp = make_response(render_template('first.html'))
      cart = request.cookies.get('cart')
      if(cart== None):
         cart=""
      cart= cart+" Item-3"
      resp.set_cookie('cart', cart)
      return resp

@app.route('/add4', methods = ['POST', 'GET'])
def add4():
   if request.method == 'POST':
      resp = make_response(render_template('second.html'))
      cart = request.cookies.get('cart')
      if(cart== None):
         cart=""
      cart= cart+" Item-4"
      resp.set_cookie('cart', cart)
      return resp

@app.route('/add5', methods = ['POST', 'GET'])
def add5():
   if request.method == 'POST':
      resp = make_response(render_template('second.html'))
      cart = request.cookies.get('cart')
      if(cart== None):
         cart=""
      cart= cart+" Item-5"
      resp.set_cookie('cart', cart)
      return resp


@app.route('/add6', methods = ['POST', 'GET'])
def add6():
   if request.method == 'POST':
      resp = make_response(render_template('second.html'))
      cart = request.cookies.get('cart')
      if(cart== None):
         cart=""
      cart= cart+" Item-6"
      resp.set_cookie('cart', cart)
      return resp

@app.route('/clear', methods = ['POST', 'GET'])
def clearr():
    resp = make_response(render_template('cart.html'))
    cart= ""
    resp.set_cookie('cart', cart)
    return resp


@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('cart')
   if(name== None or name ==""):
      return '<h1>Your cart is empty</h1>'
   return '<h1>Your Cookie :{ '+name+' }</h1>'

if __name__ == '__main__':
   app.run()
