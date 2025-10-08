from flask import Flask, render_template, request, jsonify
import os, base64, datetime, json, requests

app = Flask(__name__)
UPLOAD_FOLDER = 'captures'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def get_ip_info(ip):
    try:
        res = requests.get(f"https://ipinfo.io/{ip}/json", timeout=5)
        return res.json()
    except Exception:
        return {"error": "IP lookup failed"}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    data = request.get_json()
    image_data = data.get('image')
    meta = data.get('meta', {})

    if not image_data:
        return jsonify({'status': 'error', 'msg': 'no image data'})

    # Decode image
    header, encoded = image_data.split(",", 1)
    img_bytes = base64.b64decode(encoded)

    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    img_name = f"capture_{timestamp}.jpg"
    img_path = os.path.join(UPLOAD_FOLDER, img_name)

    # Save image
    with open(img_path, "wb") as f:
        f.write(img_bytes)

    # Add IP and location info
    client_ip = request.remote_addr
    ip_info = get_ip_info(client_ip)
    meta["client_ip"] = client_ip
    meta["ip_info"] = ip_info

    # Save meta info
    meta_path = os.path.join(UPLOAD_FOLDER, f"meta_{timestamp}.txt")
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=4, ensure_ascii=False)

    return jsonify({'status': 'ok', 'file': img_name, 'meta_saved': meta_path})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
