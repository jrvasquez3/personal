from flask import Flask, render_template, request


app = Flask(__name__, template_folder='template', static_folder='static')


@app.route("/")
@app.route("/main", methods = ['GET', 'POST'])
def main():
    return render_template("main.html")





if __name__ == "__main__":
  app.run(debug=True)