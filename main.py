from flask import Flask, render_template, request

app = Flask('app')

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/eng')
def homeeng():
  return render_template('home-eng.html')

@app.route('/lapa/eng')
def lapaeng():
  return render_template('lapa-eng.html')

@app.route('/about/eng')
def contacteng():
  return render_template('contact-eng.html')

@app.route('/lapa')
def lapa():
  return render_template('lapa.html')

@app.route('/about')
def contact():
  return render_template('contact.html')


  

if __name__ == "__main__":
    app.run(threaded=True, port=5000)