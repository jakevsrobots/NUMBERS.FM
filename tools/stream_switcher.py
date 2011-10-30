from flask import Flask


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def hello():
    return "o hai"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9090)
