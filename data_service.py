# data_service.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get_data')
def provide_data():
    return jsonify({
        "status": "Success",
        "message": "Hello from VM2!",
        "data": ["Student1@iitj.com", "Student2@iitj.com"]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)