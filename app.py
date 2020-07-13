




from flask import Flask, render_template, request, jsonify, redirect, url_for
import atexit
import os
import json
import pandas as  pd


app = Flask(__name__, static_url_path='',template_folder='static')



# On IBM Cloud Cloud Foundry, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
#port = int(os.getenv('PORT', 8000))
#port=int(os.getenv("VCAP_APP_PORT"))

@app.route('/')
def index():
    df = pd.read_csv(os.getcwd()+'/merged_sentiments.csv')
    chart_data = df.to_dict(orient='records')
    chart_data = json.dumps(chart_data)
    data = {'chart_data': chart_data}
    return render_template("index.html", data=data)

@app.route("/sentiment")
def sentiment():
    df = pd.read_csv(os.getcwd()+'/merged_sentiments.csv')
    chart_data = df.to_dict(orient='records')
    chart_data = json.dumps(chart_data)
    data = {'chart_data': chart_data}
    return render_template("index2.html", data=data)



@app.route("/wordcloud")
def wordcloud():
    df = pd.read_csv(os.getcwd()+'/merged_sentiments.csv')
    chart_data = df.to_dict(orient='records')
    chart_data = json.dumps(chart_data)
    data = {'chart_data': chart_data}
    return render_template("index3.html", data=data)


@app.route("/emotion")
def emotion():
    df = pd.read_csv(os.getcwd()+'/sentiment_labeled_name_category_final.csv')
    chart_data = df.to_dict(orient='records')
    chart_data = json.dumps(chart_data)
    data = {'chart_data': chart_data}
    return render_template("emotion.html", data=data)
# /* Endpoint to greet and add a new visitor to database.
# * Send a POST request to localhost:8000/api/visitors with body
# * {
# *     "name": "Bob"
# * }
# */


if __name__ == '__main__':
    app.run(host='0.0.0.0')
