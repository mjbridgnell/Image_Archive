from flask import Flask, send_from_directory, jsonify, abort
from flask_cors import CORS
from flask_login import login_required
from auth.auth import auth_bp, login_manager, bcrypt
import config
import os

app = Flask(__name__)
app.config.from_object(config)
CORS(app, supports_credentials=True)

login_manager.init_app(app)
bcrypt.init_app(app)

app.register_blueprint(auth_bp, url_prefix="/auth")

IMAGE_DIR = "/home/mjbridgnell/Image_Archiver/Images"

# Route to list all images
@app.route('/images')
@login_required
def list_images():
    if not os.path.exists(IMAGE_DIR):
        return jsonify([])
    files = [f for f in os.listdir(IMAGE_DIR)
             if os.path.isfile(os.path.join(IMAGE_DIR, f)) and ":" not in f]
    return jsonify(files)

# Route to serve a single image
@app.route('/images/<filename>')
@login_required
def serve_image(filename):
    if ":" in filename:
        abort(404)  # ignore Windows ADS files
    file_path = os.path.join(IMAGE_DIR, filename)
    if not os.path.exists(file_path):
        abort(404)
    return send_from_directory(IMAGE_DIR, filename)

if __name__ == "__main__":
    app.run(debug=True)
