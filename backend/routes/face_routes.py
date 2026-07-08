from flask import Blueprint

face_bp = Blueprint("face", __name__)

@face_bp.route("/face", methods=["GET"])
def face_home():
    return {"message": "Face route placeholder"}, 200
