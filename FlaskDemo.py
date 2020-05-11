from flask import Flask

app=Flask(__name__)
@app.route('/')
@app.route('/hello')
def Hello():
    return "Hello Pyhton"

if __name__ == "__main__":
    
    app.run('localhost',4449)