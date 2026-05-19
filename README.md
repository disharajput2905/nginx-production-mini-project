# 🚀 NGINX Production Mini Project

![NGINX](https://img.shields.io/badge/NGINX-Reverse%20Proxy-green)
![Flask](https://img.shields.io/badge/Flask-Backend-black)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-orange)
![SSL](https://img.shields.io/badge/SSL-OpenSSL-blue)
![Status](https://img.shields.io/badge/Project-Working-success)

---

## 📌 Overview

This project demonstrates a production-style web architecture using:

- NGINX Reverse Proxy
- Load Balancing (2 Flask backend servers)
- Static Frontend
- HTTPS (Self-Signed SSL)
- HTTP → HTTPS Redirection

This setup simulates how real-world production systems are structured.

---

## 🏗 Architecture

Client (Browser)
        │
        ▼
    NGINX (Port 80 → 443)
        │
        ├── Serves Static Frontend
        │
        └── /api/ → Load Balancer
                      │
        ┌─────────────┴─────────────┐
        ▼                           ▼
Backend 1 (Flask - 5000)     Backend 2 (Flask - 5001)

---

## 📂 Project Structure

nginx-production-mini-project/
│
├── backend1/
│   └── app.py
│
├── backend2/
│   └── app.py
│
├── frontend/
│   └── index.html
│
├── load_balancing.sh
└── README.md

---

## ⚙️ Technologies Used

- Ubuntu Linux
- NGINX
- Python 3
- Flask
- OpenSSL
- Bash

---

## 🔧 Backend Setup

Each backend runs a simple Flask app.

### backend1/app.py

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Backend 1"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### backend2/app.py

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Backend 2"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
```

Run both backends:

```bash
cd backend1
python3 app.py

cd ../backend2
python3 app.py
```

---

## 🌐 NGINX Configuration

### Features:
- Reverse Proxy
- Load Balancing
- Static File Serving
- HTTPS
- HTTP → HTTPS Redirect

Example configuration (`/etc/nginx/sites-available/myproject.conf`):

```nginx
upstream backend_servers {
    server 127.0.0.1:5000;
    server 127.0.0.1:5001;
}

server {
    listen 80;
    server_name localhost;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name localhost;

    ssl_certificate /etc/nginx/ssl/nginx.crt;
    ssl_certificate_key /etc/nginx/ssl/nginx.key;

    root /home/<your-username>/nginx-production-mini-project/frontend;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }

    location /api/ {
        proxy_pass http://backend_servers/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

Restart NGINX:

```bash
sudo nginx -t
sudo systemctl restart nginx
```

---

## 🔐 SSL Setup (Self-Signed)

Create SSL directory:

```bash
sudo mkdir -p /etc/nginx/ssl
```

Generate certificate:

```bash
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
-keyout /etc/nginx/ssl/nginx.key \
-out /etc/nginx/ssl/nginx.crt
```

---

## 🧪 Testing Load Balancing

Example test:

```bash
for i in {1..10}; do
  curl -k https://localhost/api/
done
```

Expected output (alternating):

Hello from Backend 1  
Hello from Backend 2  

---

## 🐞 Issues Debugged During Development

- 404 Not Found (Incorrect root / routing)
- 403 Forbidden (Directory permission issue)
- 502 Bad Gateway (Backend not bound to 0.0.0.0)
- Proxy path rewriting behavior

---

## 🎓 What This Project Demonstrates

- Understanding of NGINX internals
- Reverse proxy concepts
- Load balancing strategies
- Linux file permissions
- HTTP vs HTTPS behavior
- Real-world production debugging

---

## 🚀 Future Improvements

- Deploy on AWS EC2
- Use Let's Encrypt with real domain
- Dockerize application
- Add health checks
- Add logging and monitoring

---

Author
**Disha Rajput**
DevOps learner | cloud enthusiast
