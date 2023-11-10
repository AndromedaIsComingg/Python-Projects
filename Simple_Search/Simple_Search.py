from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
	return render_template('index.html')

books = [
    {"id": 1, "title": "The Great Gatsby"},
    {"id": 2, "title": "Moby Dick"},
    {"id": 3, "title": "Pride and Prejudice"},
    # ... (potentially many more books)
]

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    results = [book for book in books if query.lower() in book['title'].lower()]
    return jsonify(results)


if __name__ == '__main__':
	app.run(debug=True)
