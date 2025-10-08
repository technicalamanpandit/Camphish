
---

## 📄 `README.md`

```markdown
# Camphish - Auto Image Capture with Meta


Camphish is a **Flask-based project** that automatically captures images from the device camera (with permission)
and uploads them to a server along with metadata such as **location, timestamp, user agent, and IP information**.  
The project is designed for **educational or testing purposes** and requires explicit user permission to access the camera and location.

---

## Features

- Automatic image capture every **5 seconds** (configurable).  
- High-precision location capture (latitude, longitude, altitude, accuracy).  
- Captures browser/device metadata (user agent, platform, languages).  
- Saves each image and a corresponding metadata file on the server.  
- Placeholder image shown while waiting for camera permission.  
- No live camera preview shown to the user.  
- Fully open-source and easy to deploy with Flask.

---

## Folder Structure

```

AutoCam/
│
├─ app.py                  # Flask server
├─ templates/
│   └─ index.html          # Front-end page
├─ static/
│   └─ placeholder.jpg     # Placeholder image
└─ captures/               # Folder where images and metadata are saved

````

---

## Requirements

- Python 3.10+  
- Flask  
- Requests  

Install dependencies:

```bash
pip install flask requests
````

---

## Setup & Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YourUsername/AutoCam.git
cd AutoCam
```

### 2️⃣ Run the Flask server

```bash
python app.py
```

### 3️⃣ Open browser

```
http://127.0.0.1:5000
```

* Allow camera and location permissions to start automatic capture.
* Captured images and metadata files will be saved in the `captures/` folder.

---

## Access from Internet using Ngrok

Ngrok allows you to forward your local Flask server (default port 5000) to the internet so that you can access it from any device.

### Steps:

1. **Download Ngrok**:
   [https://ngrok.com/download](https://ngrok.com/download)
   Unzip and place it in a folder.

2. **Expose your Flask server**:
   Run this in a new terminal while your Flask server is running:

```bash
ngrok http 5000
```

3. **Copy the Forwarding URL**:
   Ngrok will display something like:

```
Forwarding   https://abcd1234.ngrok.io -> http://127.0.0.1:5000
```

* Open this `https://abcd1234.ngrok.io` link on any device or mobile browser.
* Your Camphish project will now be accessible publicly.

> ⚠️ Free Ngrok URLs change every time you start. Use paid plan for fixed URL.

---

## Configuration

* **Capture Interval**: Default is 5 seconds. Can be changed in `index.html`:

```js
let captureIntervalMs = 5000; // Change to your preferred interval
```

* **Placeholder Image**: Replace `static/placeholder.jpg` with any image you like.

---

## Notes

* **Permissions Required**: Browser will prompt for camera and location access.
* **Legal Notice**: Never use Camphish to capture images without consent. Unauthorized capture may violate privacy laws.
* **Cross-Platform**: Works on desktop and mobile browsers that support `getUserMedia` and `geolocation`.
* **IP Metadata**: Captured using `ipinfo.io` API.

---

## License

This project is **MIT Licensed**. You are free to use, modify, and distribute it for personal and educational purposes.

---

## Author

**Aman Pandit**

* GitHub: [https://github.com/AmanPandit](https://github.com/technicalamanpandit)
* Email: [aman@example.com](mailto:amanktindia@gmail.com)


