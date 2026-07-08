from flask import Blueprint

leave_bp = Blueprint("leave", __name__)

@leave_bp.route("/leave", methods=["GET"])
def get_leaves():
    return {"message": "Leave route placeholder"}, 200
