from flask import Flask, request, jsonify, render_template
from helper import recommend_books

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        # Collect search parameters from the form
        query_params = {
            'name': request.form.get('name'),
            'authors': request.form.get('authors'),
            'publish_year': request.form.get('publish_year'),
            'publisher': request.form.get('publisher')
        }
        
        # Filter out empty search parameters
        query_params = {k: v for k, v in query_params.items() if v}
        
        recommendations = recommend_books(query_params)
        return render_template('results.html', recommendations=recommendations)
    except ValueError as e:
        return render_template('error.html')

# if __name__ == '__main__':
#     app.run(debug=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

