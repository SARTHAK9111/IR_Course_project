# Web Crawler


## Abstract
This project utilizes Scrapy, a powerful web crawling framework, to gather approximately 300 HTML files from the internet. These files are then processed to generate a single JSON representation. Utilizing the capabilities of the Scikit-learn library, the project calculates both cosine similarity and TF-IDF scores. The computed scores are stored in a pickle file for future retrieval. This stored data serves as the foundation for retrieving the most relevant documents based on their respective scores. The objectives of this project include efficient web crawling, robust data processing, and accurate document retrieval. The next steps involve implementing a retrieval mechanism to efficiently access relevant documents based on the pre-computed scores.

## Overview
This project presents a comprehensive solution for web data retrieval and document relevance determination using Scrapy for web crawling, Scikit-learn for text processing, and Python's pickle module for data storage. The following outlines the solution's key components, relevant literature, and the proposed system architecture.

## Solution Outline
1. **Web Crawling with Scrapy**:
   - Utilizing Scrapy, a Python framework for web crawling, to extract approximately 300 HTML files from various sources on the internet.
   - Scrapy provides a robust, efficient, and scalable solution for crawling web pages, enabling systematic data collection.

2. **Text Processing and Feature Extraction**:
   - Processing the extracted HTML files to generate a single JSON representation for each document.
   - Using Scikit-learn, a machine learning library in Python, to calculate cosine similarity and TF-IDF scores for the documents.
   - Cosine similarity measures the similarity between two documents based on their vector representations in a multi-dimensional space.
   - TF-IDF (Term Frequency-Inverse Document Frequency) scores quantify the importance of terms in documents relative to a corpus.

3. **Data Storage and Retrieval**:
   - Storing the computed similarity scores and document representations in a pickle file format for efficient storage and retrieval.
   - The pickle module in Python facilitates the serialization and deserialization of Python objects, enabling seamless data storage.

## Relevant Literature
- "Scrapy: An Open Source and Collaborative Web Crawling Framework" by Pablo et al. (2016) provides insights into the features and capabilities of Scrapy for web crawling tasks.
- "Text Feature Extraction Techniques: A Literature Review" by Gupta and Lehal (2009) offers a comprehensive overview of text feature extraction methods, including TF-IDF.

## Interactions
1. **Web Crawling Module**:
   - Interacts with internet sources to extract HTML files using Scrapy.
   - Passes extracted files to the text processing module for further analysis.

2. **Text Processing Module**:
   - Receives HTML files from the web crawling module.
   - Processes HTML files to generate JSON representations and computes cosine similarity and TF-IDF scores using Scikit-learn.
   - Passes computed scores and representations to the data storage module for storage.

3. **Data Storage Module**:
   - Receives computed similarity scores and document representations from the text processing module.
   - Stores data in a pickle file format for efficient storage.
   - Provides retrieval mechanisms for accessing relevant documents based on pre-computed scores.

## Interactions with Flask
1. **Data Presentation**:
   - Flask interacts with the data storage module to retrieve computed similarity scores and relevant documents.
   - It formats the retrieved data into a suitable format for display on the web interface.

2. **API Endpoint Handling**:
   - Flask receives HTTP requests from Postman via API endpoints.
   - It processes these requests, which may include requests for retrieving specific documents or triggering other actions within the system.

## Architecture
### Software Components:
1. **Web Crawling Module (Scrapy)**:
   - Responsible for extracting HTML files from internet sources.
   - Implemented using Scrapy, a Python framework for web crawling.
2. **Text Processing Module (Scikit-learn)**:
   - Processes HTML files to generate JSON representations.
   - Computes cosine similarity and TF-IDF scores for document analysis.
   - Implemented using Scikit-learn, a machine learning library in Python.
3. **Data Storage Module (Pickle)**:
   - Stores computed similarity scores and document representations.
   - Implemented using Python's pickle module for efficient serialization and deserialization of Python objects.
4. **Web Application (Flask)**:
   - Provides a user interface for displaying computed results.
   - Implements API endpoints for accessing data and triggering actions within the system.
   - Implemented using Flask, a lightweight web application framework in Python.

### Interfaces:
1. **Web Crawling Module Interface**:
   - Exposes methods for initiating web crawling tasks.
   - Receives HTML files from internet sources and passes them to the text processing module.
   
2. **Text Processing Module Interface**:
   - Receives HTML files from the web crawling module.
   - Computes similarity scores and document representations using Scikit-learn.
   - Passes computed data to the data storage module for storage.
   
3. **Data Storage Module Interface**:
   - Receives computed similarity scores and document representations from the text processing module.
   - Stores data in a pickle file format for efficient storage.
   - Provides methods for retrieving stored data when requested by the web application or external clients.
   
4. **Web Application Interface**:
   - Provides a user interface for displaying computed results.
   - Implements API endpoints for retrieving data and triggering actions within the system.

## Success/Failure Results
1. **Success**:
   - The project successfully implements a comprehensive solution for web data retrieval, document analysis, and result presentation.
   - Web crawling tasks are efficiently performed using Scrapy, resulting in the extraction of approximately 300 HTML files from internet sources.
   - Text processing tasks, including JSON representation generation and computation of cosine similarity and TF-IDF scores, are accurately executed using Scikit-learn.
   - Computed similarity scores and document representations are effectively stored and retrieved using Python's pickle module.
   - The web application, built with Flask, provides a user-friendly interface for displaying computed results and accessing data via API endpoints.
   
2. **Failure**:
   - Failure to extract sufficient HTML files from internet sources due to limitations in web crawling techniques or constraints imposed by target websites.
   - Inaccurate computation of similarity scores or TF-IDF scores resulting from issues with text preprocessing, feature extraction, or model parameter tuning.
   - Unforeseen errors or bugs in the implementation of software components leading to system instability or malfunction.

## Outputs
- The project outputs include:
  - Extracted HTML files from internet sources.
  - JSON representations of processed documents.
  - Computed similarity scores and TF-IDF scores for document analysis.
  - Stored data in a pickle file format for efficient storage and retrieval.
  - A user-friendly web application interface for displaying computed results and accessing data via API endpoints.

## Caveats/Cautions
- Ensure compliance with Wikipedia's terms of service and usage policies when accessing and using data from their website.

## Dependencies and Setup
### Data Source
- Wikipedia Page: [Formula One](https://en.wikipedia.org/wiki/Formula_One)
  - This page can be used as a sample data source for web crawling and document processing tasks.

### Python Libraries
1. **Flask**:
   - Installation: You can install Flask using pip:
     ```
     pip install flask
     ```

2. **Scikit-learn**:


   - Installation: Install Scikit-learn using pip:
     ```
     pip install scikit-learn
     ```

3. **Pandas**:
   - Installation: Pandas can be installed via pip:
     ```
     pip install pandas
     ```

4. **BeautifulSoup**:
   - Installation: BeautifulSoup can be installed using pip:
     ```
     pip install beautifulsoup4
     ```

These libraries provide the necessary functionalities for web crawling, data processing, and web application development as part of your project. 

Remember to comply with Wikipedia's terms of service and usage policies when accessing and using data from their website.


### Operation

**Running the Project:**

1. **Clone the Repository:**
   - Clone the project repository from the provided GitHub link to your local machine.

2. **Install Required Libraries:**
   - Ensure that you have Python installed on your system.
   - Install the required Python libraries by running the following commands in your terminal:
     ```
     pip install scrapy scikit-learn pandas flask
     ```

3. **Phase 1: Web Crawling:**
   - Navigate to the directory containing the Scrapy spider.
   - Run the spider named GameCrawlerSpider using the following command:
     ```
     scrapy crawl f1_crawler
     ```
   - The spider will start fetching web pages from the specified domain (Wikipedia articles related to video games), extract content, and store the HTML files locally in a folder named webpages.

4. **Phase 2: Indexing:**
   - After the crawler finishes fetching HTML files, proceed to the indexing phase.
   - Execute the code to generate the TF-IDF matrix from JSON using the `TfidfVectorizer` method from the scikit-learn library.
   - Save the TF-IDF matrix and cosine similarity matrix as pickle files for later use.
     ```
     cd ..
     cd indexer
     python cropusCreation
     python TF_score
     ```

5. **Phase 3: Query Processing:**
   - In this phase, a Flask-based query processor handles user queries.
   - Load the TF-IDF matrix and cosine similarity matrix from the pickle files generated in the previous phase.
   - Create a Flask application with RESTful API endpoints to receive text queries in JSON format.
   - Implement query processing logic to vectorize user queries, calculate cosine similarity scores, and return top-k results.
     ```
     cd ..
     cd processor
     python tfidf_loader
     python processor
     ```

**Accessing the Application:**

- Once the Flask application is running, users can send text queries to the specified endpoint using HTTP GET or POST requests.
- The application will process the queries, retrieve relevant documents based on cosine similarity scores, and return the results to the users.
- Go to the localhost and append the query in front of the URL.

This guide provides step-by-step instructions on how to set up and run the project, as well as how to access and interact with the application.
### Snippets 

![WhatsApp Image 2024-04-22 at 23 07 13_397cca7b](https://github.com/SARTHAK9111/crawler/assets/77686182/5125ac17-4992-4fdf-8c86-7964ee2bc3d2)

![WhatsApp Image 2024-04-22 at 23 08 06_f54cb68f](https://github.com/SARTHAK9111/crawler/assets/77686182/e6345c17-48ec-4dd2-85ed-87168ae01d2e)

