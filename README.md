# 🏆 Flask API with DSA Algorithms (Binary Search, Quick Sort, BFS)

This is a Flask-based API that demonstrates fundamental Data Structures and Algorithms (DSA) concepts. The API includes the following algorithms:

✅ Binary Search  
✅ Quick Sort  
✅ Breadth First Search (BFS)  
✅ API Call Logging (stored using SQLite)  

---

## 🚀 **Features**
- Clean and modular Flask architecture  
- SQLite database for logging API calls  
- Handles edge cases with proper error handling  
- Deployed on Render (compatible with free plan)  
- Automatic table creation at startup  

---

## 🏗️ **Tech Stack**
- **Backend:** Flask  
- **Database:** SQLite  
- **Web Server:** Gunicorn  
- **Deployment:** Render  

## Install dependencies

pip install -r requirements.txt
## Set up the database

python setup_db.py

## local machine run the surver

python main.py

It will run in the surver 
http://127.0.0.1:5000

## 🌐 Deployed on Render

https://digantara-2.onrender.com

## Endpoints
1. ## Binary Search
Endpoint: /binary-search
Method: POST
Description: Performs a binary search on a sorted array.
Sample Request:
{
    "array": [1, 2, 3, 4, 5],
    "target": 3
}
Sample Response:
{
    "result": 2
}

2. ## Quick Sort
Endpoint: /quick-sort
Method: POST
Description: Performs quick sort on an array.
Sample Request:
{
    "array": [4, 6, 2, 5, 7, 9, 1, 3]
}
Sample Response:
{
    "result": [1, 2, 3, 4, 5, 6, 7, 9]
}


3. ## Breadth First Search (BFS)
Endpoint: /bfs
Method: POST
Description: Performs BFS on a graph and returns the traversal order.
Sample Request:
{
    "graph": {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["E"],
        "D": [],
        "E": []
    },
    "start": "A"
}
Sample Response:
{
    "result": ["A", "B", "C", "D", "E"]
}

4. ## Get All Logs
Endpoint: /logs
Method: GET
Description: Returns the list of all previously executed API calls.
Sample Response:
{
    "logs": [
        {
            "id": 1,
            "algorithm_name": "Binary Search",
            "input_data": "{'array': [1, 2, 3, 4], 'target': 3}",
            "output_data": "2",
            "timestamp": "2025-03-16 12:00:00"
        }
    ]
}
