from flask import Blueprint

parent_bp = Blueprint("parent", __name__)

@parent_bp.route("/parents", methods=["GET"])
def get_parents():
    return {"message": "Parent route placeholder"}, 200
