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


  

if __name__ == "__main__":
    app.run(threaded=True, port=5000)