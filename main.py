from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    data = {}
    return render_template('index.html', data=data)

@app.route('/upload', methods=['POST'])
def upload():
    app.logger.info(request)
    url = request.form["profileURL"]
    if request.form["profileURL"][-1] != "/":
        url = url + "/"
    url = url + "tick-export"
    data = pd.read_csv(url)
    this_year = data[(data['Date'] >= '2023-01-01')]
    max_crag = this_year.groupby(['Location'])['Location'].count().idxmax()
    max_type = this_year.groupby(['Route Type'])['Route Type'].count().idxmax()
    max_route = this_year['Route'][this_year['Your Stars'].idxmax()]
    number_days = this_year['Date'].nunique()
    return render_template('data.html', routes=this_year.Route.nunique(), locations=this_year.Location.nunique(), max_crag=max_crag, max_type=max_type, max_route=max_route,number_days=number_days)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)