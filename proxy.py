from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return 'Simple Web Proxy is Running! Add a URL parameter like ?url=https://example.com'

@app.route('/proxy')
def proxy():
    target_url = request.args.get('url')
    if not target_url:
        return "No URL provided!", 400

    try:
        response = requests.get(target_url)
        return Response(response.content, content_type=response.headers.get('Content-Type', 'text/html'))
    except Exception as e:
        return f"Error fetching the URL: {e}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
