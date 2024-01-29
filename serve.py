from flask import Flask, request, jsonify
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    if request.method == 'POST':
        # Create a separate process to run "stress_cpu.py"
        subprocess.Popen(['python3', 'stress_cpu.py'])
        return jsonify({"message": "Stressing CPU in a separate process"})

    elif request.method == 'GET':
        # Get private IP address using socket
        private_ip = socket.gethostbyname(socket.gethostname())
        return private_ip

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
