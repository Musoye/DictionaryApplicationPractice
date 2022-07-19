from flask import Flask, render_template, request
from scope import Dictionary

app = Flask(__name__)

app.secret_key = ''


@app.route('/', methods=['GET', 'POST'])
def index():
    user_response=''
    if request.method == 'POST':
        user_input = request.form['word']
        if user_input == '':
            user_response = "Enter a word into the input box."
        else:
            conn = Dictionary(user_input)
            user_response = conn.meaning()
   
    return render_template("index.html", user_response=user_response)
    

if __name__  == "__main__":
    app.run(debug=True)