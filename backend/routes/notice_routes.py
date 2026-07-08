from flask import Blueprint

notice_bp = Blueprint("notice", __name__)

@notice_bp.route("/notices", methods=["GET"])
def get_notices():
    return {"message": "Notice route placeholder"}, 200
