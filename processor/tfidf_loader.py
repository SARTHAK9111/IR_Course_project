import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_tfidf_data(tfidf_index_path, cosine_similarities_path):
    """Loads TF-IDF vectorizer, matrix, and cosine similarities from files."""
    with open(tfidf_index_path, 'rb') as f:
        tfidf_vectorizer, tfidf_matrix = pickle.load(f)
    with open(cosine_similarities_path, 'rb') as f:
        cosine_similarities = pickle.load(f)
    return tfidf_vectorizer, tfidf_matrix, cosine_similarities

def search_similar_documents(query, tfidf_vectorizer, tfidf_matrix, cosine_similarities, documents, top_k):
    """Searches for documents similar to the query using cosine similarity."""
    query_vector = tfidf_vectorizer.transform([query])
    query_cosine_similarities = cosine_similarity(query_vector, tfidf_matrix)
    most_similar_indices = query_cosine_similarities.argsort()[0][::-1]
    
    similar_documents = [(cosine_similarities[0][idx], documents.iloc[idx]['title'].strip()) for idx in most_similar_indices[:top_k]]
    
    
    

    return similar_documents, most_similar_indices[:top_k]

def search_documents(query, data_directory="E:/IR/IRProject/Web_Crawler_Sarthak/f1_crawler/"):
    """Searches for documents using a specified query and data directory."""
    tfidf_index_path = data_directory + "tfidf.pkl"
    cosine_similarities_path = data_directory + "cosine_similarity.pkl"
    documents_path = data_directory + "f1_records.json"

    # Load indexed data
    tfidf_vectorizer, tfidf_matrix, cosine_similarities = load_tfidf_data(tfidf_index_path, cosine_similarities_path)

    # Load documents from JSON
    documents_df = pd.read_json(documents_path)

    # Perform search
    search_results, index = search_similar_documents(query, tfidf_vectorizer, tfidf_matrix, cosine_similarities, documents_df, top_k=5)

    return search_results, index


# Example usage (assuming you have the data files in the specified directory)
query = "information retrieval"
results = search_documents(query)

# for id in results:
#     print("id: ", id)
#     print(f"Document: {id['title']}, Similarity Score: {id['score']:.4f}")
