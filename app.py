from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Home page"
@app.route("/about")
def about():
    return "Welcome to about page"

@app.route("/contact")
def contact():
    return "Welcome to Contact"
if __name__ == "__main__":
    app.run(debug=True)