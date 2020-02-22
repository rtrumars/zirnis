from flask import Flask, json, jsonify, render_template, request
import chats

app = Flask('app')

@app.route('/')
def home():
  return render_template('home.html')
@app.route('/lapa')
def lapa():
  return render_template('lapa.html')
@app.route('/contact')
def contact():
  return render_template('contact.html')

  @app.route('/')
def index_lapa():
  return render_template('chats.html')


@app.route('/health')
def health_check():
  return "OK"


@app.route('/chats/lasi')
def ielasit_chatu():
  return chats.lasi()


@app.route('/chats/suuti', methods=['POST'])
def suutiit_zinju():
  dati = request.json
  
  chats.pieraksti_zinju(dati)

  return chats.lasi()
  

if __name__ == "__main__":
    app.run(threaded=True, port=5000)