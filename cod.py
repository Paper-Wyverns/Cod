pip install flask requests

from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form action="/proxy" method="get">
            <input type="text" name="url" placeholder="Enter URL to proxy" size="50"/>
            <input type="submit" value="Submit"/>
        </form>
    '''

@app.route('/proxy')
def proxy():
    url = request.args.get('url')
    if not url:
        return "Please provide a URL to proxy.", 400

    try:
        response = requests.get(url)
        return Response(response.content, content_type=response.headers['Content-Type'])
    except requests.RequestException as e:
        return f"An error occurred: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)
