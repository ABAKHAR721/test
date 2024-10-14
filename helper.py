import numpy as np
from sklearn.metrics.pairwise import linear_kernel
import pandas as pd
import pickle
import re




# Load the saved TF-IDF Vectorizers and DataFrame
with open('model/tfidf_vectorizer_name.pkl', 'rb') as f:
    tfidf_vectorizer_name = pickle.load(f)
with open('model/tfidf_vectorizer_authors.pkl', 'rb') as f:
    tfidf_vectorizer_authors = pickle.load(f)
with open('model/tfidf_vectorizer_publish_year.pkl', 'rb') as f:
    tfidf_vectorizer_publish_year = pickle.load(f)
with open('model/tfidf_vectorizer_publisher.pkl', 'rb') as f:
    tfidf_vectorizer_publisher = pickle.load(f)

with open('model/books_df.pkl', 'rb') as f:
    books = pickle.load(f)






def clean_html_tags(text):
    # Replace <br /> tags with newlines and strip leading/trailing spaces
    cleaned_text = re.sub(r'<br\s*/?>', '\n', text)
    return cleaned_text.strip()  # Remove extra spaces and newlines

# Clean HTML tags in descriptions
books['Description'] = books['Description'].apply(clean_html_tags)
# Drop rows where 'Description' is empty or consists only of whitespace
books = books[books['Description'].str.strip().astype(bool)]


# Load pre-calculated TF-IDF matrices for each column
tfidf_matrix_name = tfidf_vectorizer_name.transform(books['Name'])
tfidf_matrix_authors = tfidf_vectorizer_authors.transform(books['Authors'])
tfidf_matrix_publish_year = tfidf_vectorizer_publish_year.transform(books['PublishYear'])
tfidf_matrix_publisher = tfidf_vectorizer_publisher.transform(books['Publisher'])




def recommend_books(query_params, top_n=5):
    # Initialize an array to accumulate cosine similarities
    cosine_similarities = np.zeros(tfidf_matrix_name.shape[0])

    # Check for each query parameter and add cosine similarity accordingly
    if 'name' in query_params:
        query_vector = tfidf_vectorizer_name.transform([query_params['name']])
        cosine_similarities += linear_kernel(query_vector, tfidf_matrix_name).flatten()

    if 'authors' in query_params:
        query_vector = tfidf_vectorizer_authors.transform([query_params['authors']])
        cosine_similarities += linear_kernel(query_vector, tfidf_matrix_authors).flatten()

    if 'publish_year' in query_params:
        query_vector = tfidf_vectorizer_publish_year.transform([query_params['publish_year']])
        cosine_similarities += linear_kernel(query_vector, tfidf_matrix_publish_year).flatten()

    if 'publisher' in query_params:
        query_vector = tfidf_vectorizer_publisher.transform([query_params['publisher']])
        cosine_similarities += linear_kernel(query_vector, tfidf_matrix_publisher).flatten()

    # If no valid search criteria, raise an error
    if cosine_similarities.sum() == 0:
        raise ValueError("Books Not Found 404.")

    # Get the top N results based on combined similarities
    top_indices = cosine_similarities.argsort()[-top_n:][::-1]
    top_books = books.iloc[top_indices]

    # Clean HTML tags in descriptions
    top_books['Description'] = top_books['Description'].apply(clean_html_tags)

    # Remove rows where the description is empty or missing
    top_books = top_books[top_books['Description'].notna() & top_books['Description'].str.strip() != '']

    # Sort the books by Rating in descending order
    top_books = top_books.sort_values(by='Rating', ascending=False)

    return top_books[['Name', 'Authors', 'PublishYear', 'Publisher', 'Description', 'Rating']].to_dict(orient='records')
