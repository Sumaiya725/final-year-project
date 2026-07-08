from flask import Blueprint

attendance_bp = Blueprint("attendance", __name__)

@attendance_bp.route("/attendance", methods=["GET"])
def get_attendance():
    return {"message": "Attendance route placeholder"}, 200
