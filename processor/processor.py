from flask import Flask, request, jsonify
import json
import tfidf_loader

app = Flask(__name__)

@app.route('/<query>', methods=['GET'])
def search_result(query):
    # Assuming tfidf_loader is some object or module where search_documents is defined
    results, index = tfidf_loader.search_documents(query)
    
    filtered_results = [result for result in results if result is not None]

    # Convert numpy.int64 to Python native integers
    new_results = []
    for result, idx in zip(filtered_results, index):
        temp = {"score": str(result[0]), "title": result[1], "index": str(idx)}
        new_results.append(temp)

    return jsonify(new_results)

if __name__ == '__main__':
    app.run()
