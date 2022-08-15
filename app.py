from flask import Flask, render_template, request
import pandas as pd


app = Flask(__name__)


@app.route('/')

def index():
    return render_template('index.html')


@app.route("/home")
def home():
    return render_template('home.html')


@app.route('/result', methods=["GET", 'POST'])

def result():

    source = str(request.form.get('source'))
    destination = request.form.get('destination')

    df = pd.read_csv("map_urls.csv")

    print(source)
    print(destination)

    url = df[(df['SOURCE'] == source) & (
        df['DESTINATION'] == destination)].reset_index().iloc[0]["MAP_URL"]

    # url = url.encode("utf-8")

    return render_template('result.html', iframe=url, source=source, destination=destination)


if __name__ == "__main__":
    app.run()
    app.debug = True
