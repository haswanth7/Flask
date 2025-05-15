from flask import Flask
app=Flask(__name__)
@app.route('/')
def self():
    return'''
     <html>
     <head>
     <title>self intro</title>
     <h1>I am Haswanth</h1>    </head>
     <p> Iam from chennai</p>
    </html>'''

if __name__=='__main__':
    app.run(port=3010,debug=True)