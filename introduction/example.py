from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route("/home")
def hello_internet():
    return "Hello Internet We made out first web APP!"

@app.route("/about")
def about():
    return "This is about page but there is nothing here Yet! :D"

@app.route("/squared/<int:number>,<int:number_two>")
def square(number, number_two):
    return str(number**number_two)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

