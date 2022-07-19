from flask import Flask
from wol import WakeOnLan

wol = WakeOnLan()

app = Flask(__name__)

@app.route('/wake/<name>')
def wake(name):
    return wol(name)



if __name__ == "__main__":
    app.run('::', 5000)
