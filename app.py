from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory task storage
tasks = [
    {"id": 1, "title": "Learn Azure DevOps", "completed": False},
    {"id": 2, "title": "Implement AI Testing", "completed": False},
]

# Endpoint to retrieve all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks), 200

# Endpoint to create a new task
@app.route("/tasks", methods=["POST"])
def create_task():
    new_task = request.json
    if not new_task.get("title"):
        return jsonify({"error": "Title is required"}), 400
    new_task["id"] = len(tasks) + 1
    new_task["completed"] = False
    tasks.append(new_task)
    return jsonify(new_task), 201

# Endpoint to update a task
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    updates = request.json
    task.update(updates)
    return jsonify(task), 200

# Endpoint to delete a task
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return jsonify({"message": "Task deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)
