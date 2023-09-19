from flask import Flask, request, jsonify
from utils.captions import process_image
from utils.key_frames import process_video

app = Flask(__name__)

app.debug = True

@app.route("/api/caption", methods=["POST"])
def generate_caption():
    reqs = request.get_json()
    data = reqs.get("data", None)
    if data is not None:
        caption = process_image(data)
        return jsonify({"caption": caption})
    return jsonify({"error": "Invalid request data"}), 400

@app.route("/api/keyframes", methods=["POST"])
def generate_keyframes():
    video = request.files["video"]
    if video:
        print("accepted")
        video.save("./uploaded_files/" + video.filename)
        keyframes = process_video(video.filename)
        # keyframes = ["str1", "str2", "str3"]
        return jsonify({"keyframes": keyframes})
    return jsonify({"error": "Invalid video file"}), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)