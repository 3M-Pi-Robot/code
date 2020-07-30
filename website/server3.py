import pin
from flask import Flask
app = Flask(__name__)

pin.load("config.json")

filename="control.html"

@app.route("/")
def showIndex():
    with open(filename, "r") as file:
        return file.read()

@app.route("/move/<left>/<right>")
def moveTo(left,right):
    print(left,right)
    ena=int(left)
    enb=int(right)

    # set the motor speed    
    if(ena>=0):            
        ena = min(ena, 100)
        pin.Level("ENA",ena)
        pin.Out("IN1",0)
        pin.Out("IN2",1)
    else:
        ena_minus = abs(ena) 
        ena_minus = min(ena_minus, 100)
        pin.Level("ENA",ena_minus)
        pin.Out("IN1",1)
        pin.Out("IN2",0)
    if(enb>=0):
        enb = min(enb, 100)
        pin.Level("ENB",enb)
        pin.Out("IN3",1)
        pin.Out("IN4",0)
    else:
        enb_minus = abs(enb)        
        enb_minus = min(enb_minus, 100)
        pin.Level("ENB",enb_minus)
        pin.Out("IN3",0)
        pin.Out("IN4",1)    

    
    with open(filename, "r") as file:
        return file.read()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
