from flask import Flask, render_template, request

app = Flask('app')

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/lapa')
def lapa():
  return render_template('lapa.html')

@app.route('/about')
def contact():
  return render_template('contact.html')

@app.route('/eng')
def homeeng():
  return render_template('homeeng.html')

@app.route('/lapa/eng')
def lapaeng():
  return render_template('lapaeng.html')

@app.route('/about/eng')
def contacteng():
  return render_template('contacteng.html')

  

if __name__ == "__main__":
    app.run(threaded=True, port=5000)