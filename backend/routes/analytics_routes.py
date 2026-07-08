from flask import Blueprint

analytics_bp = Blueprint("analytics", __name__)

@analytics_bp.route("/analytics", methods=["GET"])
def analytics_home():
    return {"message": "Analytics route placeholder"}, 200
