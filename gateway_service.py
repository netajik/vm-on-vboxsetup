from flask import Flask
import requests  # you may need to: pip3 install requests

app = Flask(__name__)

@app.route('/')
def home():
    try:
        # VM1 calls VM2's IP address
        response = requests.get('http://10.0.2.4:5001/get_data')
        data_from_vm2 = response.json()
        return f"Gateway Status: Active Data from VM2: {data_from_vm2}"
    except Exception as e:
        print(f"Failed to connect VM2: {e}")
        return "Service Error"

if __name__ == '__main__':
    print("VM1 started...")
    app.run(host='0.0.0.0', port=5000)