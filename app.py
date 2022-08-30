from flask import Flask, render_template, request
from dict import meaning

app = Flask(__name__)

app.secret_key = 'secretkey&&'


@app.route('/', methods=['GET', 'POST'])
def index():
    user_response=''
    if request.method == 'POST':
        user_input = request.form['word']
        if user_input == '':
            user_response = "Enter a word into the input box."
        else:
            user_response=meaning(user_input)
   
    return render_template("index.html", user_response=user_response)
    

if __name__  == "__main__":
    app.run(debug=True)