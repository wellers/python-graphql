import os
import time
from flask import Flask, jsonify
from strawberry.flask.views import GraphQLView
from server import schema

app = Flask(__name__)

@app.route("/status")
def status():
	return jsonify({ "date": time.time() })

app.add_url_rule(
	"/graphql",
	view_func=GraphQLView.as_view("graphql_view", schema=schema)
)

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(debug=True, host="0.0.0.0", port=port)