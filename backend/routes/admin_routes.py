from flask import Blueprint

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/admin", methods=["GET"])
def admin_home():
    return {"message": "Admin route placeholder"}, 200
