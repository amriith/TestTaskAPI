from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for tasks
tasks = []
task_id_counter = 1

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks"""
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    """Create a new task 1"""
    global task_id_counter
    
    if not request.json or 'title' not in request.json:
        return jsonify({'error': 'Title is required'}), 400
    
    task = {
        'id': task_id_counter,
        'title': request.json['title'],
        'description': request.json.get('description', ''),
        'completed': False
    }
    
    tasks.append(task)
    task_id_counter += 1
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Get a specific task by ID"""
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify(task)

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Update a task"""
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    
    if not request.json:
        return jsonify({'error': 'No data provided'}), 400
    
    task['title'] = request.json.get('title', task['title'])
    task['description'] = request.json.get('description', task['description'])
    task['completed'] = request.json.get('completed', task['completed'])
    
    return jsonify(task)

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task"""
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    
    tasks.remove(task)
    return jsonify({'message': 'Task deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True) 