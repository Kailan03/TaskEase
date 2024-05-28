from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

task_bp = Blueprint('tasks', __name__)

@task_bp.route('/', methods=['POST'])
@jwt_required()
def create_task():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    due_date = data.get('due_date')
    user_id = get_jwt_identity()

    new_task = Task(title=title, description=description, due_date=due_date, user_id=user_id)
    db.session.add(new_task)
    db.session.commit()

    return jsonify({'message': 'Task created successfully'}), 201

@task_bp.route('/', methods=['GET'])
@jwt_required()
def get_tasks():
    user_id = get_jwt_identity()
    tasks = Task.query.filter_by(user_id=user_id).all()
    tasks_list = [{'id': task.id, 'title': task.title, 'description': task.description, 'status': task.status, 'due_date': task.due_date} for task in tasks]

    return jsonify(tasks_list), 200

@task_bp.route('/<int:task_id>', methods=['PUT'])
@jwt_required()
def update_task(task_id):
    data = request.get_json()
    task = Task.query.get_or_404(task_id)
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.status = data.get('status', task.status)
    task.due_date = data.get('due_date', task.due_date)
    db.session.commit()

    return jsonify({'message': 'Task updated successfully'}), 200

@task_bp.route('/<int:task_id>', methods=['DELETE'])
@jwt_required()
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()

    return jsonify({'message': 'Task deleted successfully'}), 200

