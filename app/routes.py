# app/routes.py
from flask import Blueprint, request, jsonify
from app.algorithms import binary_search, quick_sort, bfs
from app.models import db, APILog

api_blueprint = Blueprint('api', __name__)

def log_api_call(name, input_data, output_data):
    log = APILog(
        algorithm_name=name,
        input_data=str(input_data),
        output_data=str(output_data)
    )
    db.session.add(log)
    db.session.commit()

@api_blueprint.route('/binary-search', methods=['POST'])
def binary_search_route():
    data = request.json
    arr = data.get('array')
    target = data.get('target')
    result = binary_search(arr, target)
    log_api_call('Binary Search', data, result)
    return jsonify({'result': result})

@api_blueprint.route('/quick-sort', methods=['POST'])
def quick_sort_route():
    data = request.json
    arr = data.get('array')
    result = quick_sort(arr)
    print(result)
    log_api_call('Quick Sort', data, result)
    return jsonify({'result': result})

@api_blueprint.route('/bfs', methods=['POST'])
def bfs_route():
    data = request.json
    graph = data.get('graph')
    start = data.get('start')
    result = bfs(graph, start)
    log_api_call('BFS', data, result)
    return jsonify({'result': result})

@api_blueprint.route('/logs', methods=['GET'])
def get_logs():
    logs = APILog.query.all()
    log_data = [{
        'id': log.id,
        'algorithm_name': log.algorithm_name,
        'input_data': log.input_data,
        'output_data': log.output_data,
        'timestamp': log.timestamp.strftime('%Y-%m-%d %H:%M:%S')
    } for log in logs]
    return jsonify({'logs': log_data})
