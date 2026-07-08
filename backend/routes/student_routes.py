from flask import Blueprint

student_bp = Blueprint("student", __name__)

@student_bp.route("/students", methods=["GET"])
def get_students():
    return {"message": "Student route placeholder"}, 200
