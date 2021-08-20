from flask import Flask,jsonify



app = Flask(__name__)

@app.route('/')
def validate():
   
    return "hello world Friday 10:22"
      

if __name__ == '__main__':
    app.run(debug=True)
