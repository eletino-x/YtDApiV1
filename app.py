from flask import Flask, request, jsonify
import pytube

app = Flask(__name__)

@app.route("/download")
def download():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "Bitte URL mitgeben"}), 400

    # kurze Links normalisieren
    if "youtu.be/" in url:
        url = url.split("?")[0]

    try:
        yt = pytube.YouTube(url)
        stream = yt.streams.get_highest_resolution()
        return jsonify({
            "title": yt.title,
            "author": yt.author,
            "length": yt.length,
            "download_url": stream.url
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 590
