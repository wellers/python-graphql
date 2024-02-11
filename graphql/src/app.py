import os
import time
from flask import Flask, jsonify
from strawberry.flask.views import AsyncGraphQLView
from server import schema

app = Flask(__name__)

@app.route("/status")
def status():
	return jsonify({ "date": time.time() })

app.add_url_rule(
	"/graphql",
	view_func=AsyncGraphQLView.as_view("graphql_view", schema=schema)
)

if __name__ == "__main__":
	from waitress import serve
	port = int(os.environ.get('PORT', 5000))
	serve(app, host="0.0.0.0", port=port)