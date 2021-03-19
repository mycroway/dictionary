from webscraping import get
from flask import Flask, request, jsonify

app = Flask('dictionary API')

@app.route('/', methods=["GET"])
def index():
	word = request.args.get('word')
	if word:
		return jsonify(get(word))
	else:
		return jsonify({"error": "palavra não inserida"})

app.run(port=3131, debug=False)
