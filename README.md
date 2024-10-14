# Book Recommendation System
k
## Overview  
The Book Recommendation System is a web application designed to provide personalized book recommendations based on user inputs. It leverages TF-IDF vectorization and cosine similarity to match user queries with a pre-built dataset of books, returning relevant recommendations.

### Features
Search Functionality: Allows users to search for books based on various criteria 
such as name, authors, publish year, and publisher.

Recommendations: Displays a list of recommended books with details such as name, 
authors, publish year, publisher, and description.

Responsive Design: Built with Bootstrap for a responsive and modern user interface.
Dark Mode: Includes a dark-themed UI for a contemporary look and feel.
Technologies Used

#### Frontend:HTML, CSS, Bootstrap 4, Font Awesome
#### Backend: Flask (Python)
#### Machine Learning: Scikit-learn for TF-IDF vectorization and cosine similarity
#### Data Storage: Pickle for loading pre-trained models and book data

## Setup

1. **Clone the Repository**

    ```bash
    git clone https://github.com/ABAKHAR721/Book-Recommendation-System.git
    cd Book-Recommendation-System
    ```

2. **Create and Activate a Virtual Environment linux ubuntu 20.04**

    ```bash
    python -m venv books_env
    source books_env/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask Application**

    ```bash
    python app.py
    ```

5. **Navigate to `http://127.0.0.1:5000/` in your browser to use the application.**

## Files

- **app.py**: Main Flask application file.
- **requirements.txt**: Python dependencies.
- **static/styles.css**: CSS for styling the application.
- **templates/index.html**: Search input form.
- **templates/results.html**: Display recommendations.
- **templates/error.html**: 404 Page: Provides a user-friendly error message if no recommendations are found.
- **models/**: Directory containing saved model files.

## Contributing

Feel free to open issues or submit pull requests. Contributions are welcome to improve the functionality and features of this project.


## License

This project is licensed under the MIT License.
