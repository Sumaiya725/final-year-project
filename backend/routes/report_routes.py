from flask import Blueprint

report_bp = Blueprint("report", __name__)

@report_bp.route("/reports", methods=["GET"])
def get_reports():
    return {"message": "Report route placeholder"}, 200
