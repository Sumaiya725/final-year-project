from flask import Blueprint

qr_bp = Blueprint("qr", __name__)

@qr_bp.route("/qr", methods=["GET"])
def qr_home():
    return {"message": "QR route placeholder"}, 200
