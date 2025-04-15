from flask import Flask,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["*"])

@app.route('/api/message',methods=['GET'])
def message():
    return jsonify({"message":"hello World"})

if __name__ == "__main__":
    app.run(debug=True,port=5000)