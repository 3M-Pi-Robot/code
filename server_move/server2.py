from flask import Flask
app = Flask(__name__)

filename="test.html"

@app.route("/")
def showIndex():
    with open(filename, "r") as file:
        return file.read()

@app.route("/move/<left>/<right>")
def moveTo(left,right):
    print(left,right)
    with open(filename, "r") as file:
        return file.read()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
