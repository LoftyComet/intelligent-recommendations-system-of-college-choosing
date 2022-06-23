from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/index')
def home():
    return index()
@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/load')
def load():
    return render_template("load.html")

@app.route('/predict')
def predict():
    return render_template("predict.html")

@app.route('/pricing')
def pricing():
    return render_template("pricing.html")

@app.route('/services')
def services():
    return render_template("services.html")


if __name__ == '__main__':
    app.run()