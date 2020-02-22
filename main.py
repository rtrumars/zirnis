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


  

if __name__ == "__main__":
    app.run(threaded=True, port=5000)