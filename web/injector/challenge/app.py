from flask import Flask, request, render_template
import subprocess

BLACKLIST=['cat', 'echo']

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")


@app.route("/file", methods=['GET'])
def ls():
    file = request.args.get('file')
    if file:
        for blacklisted in BLACKLIST:
            if blacklisted in file:
                return 'Invalid file'
        try:
            output = subprocess.run(
                f"ls -lh {file}", shell=True, timeout=10, capture_output=True).stdout
            return output.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return e.output.decode('utf-8')
    return 'No file provided'