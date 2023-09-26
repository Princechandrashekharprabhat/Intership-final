from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    text='hi'
    global cb
    if request.args.get('q') !=None :
        que = request.args.get('q')
        text+=que
    return render_template('chatbot.html',res=text)

app.run(debug=True)