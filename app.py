#!/usr/bin/env python3

import requests

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "CJMLS"

@app.route("/properties/<int:mlsid>")
def get_property(mlsid):
    data = requests.get(f"https://queryserviceb.placester.net/search?sort_field=price&sort_direction=desc&search_num_results=9&search_start_offset=0&purchase_types=buy&mls_id={mlsid}&region_id=nj&origin_ids=51967f537293b476e0000003").json()
    mongo_id = data['organic_results']['search_results'][0]['mongo_id']
    url = f"https://www.mcmls.net/property/x/x/x/x/x/{mongo_id}/"
    return f'<meta http-equiv="refresh" content="0; url={url}" />'

if __name__ == "__main__":
    app.run(debug=True)
