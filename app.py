from flask import Flask, render_template, request, jsonify, send_from_directory
import os
from organizer import organize_uploaded_files

app = Flask(__name__)
UPLOAD_FOLDER = "organized_files"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    # Get organized folders and files
    organized = {}
    for folder in os.listdir(UPLOAD_FOLDER):
        folder_path = os.path.join(UPLOAD_FOLDER, folder)
        if os.path.isdir(folder_path):
            organized[folder] = os.listdir(folder_path)
    return render_template("index.html", organized=organized)

@app.route("/organize_upload", methods=["POST"])
def organize_upload():
    uploaded_files = request.files.getlist("files[]")
    if not uploaded_files:
        return jsonify({"status": "error", "message": "No files uploaded!"})

    organize_uploaded_files(uploaded_files, UPLOAD_FOLDER)
    return jsonify({"status": "success", "message": "Files organized successfully!"})

@app.route("/organized_files/<folder>/<filename>")
def serve_file(folder, filename):
    folder_path = os.path.join(UPLOAD_FOLDER, folder)
    return send_from_directory(folder_path, filename)

if __name__ == "__main__":
    app.run(debug=True)
