import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define your Worqhat API URL and API token
WORQHAT_API_URL = "https://api.worqhat.com/api/ai/v2/pdf-extract"
WORQHAT_API_TOKEN = "Bearer sk-eee576b8e5774fd8be604db01b1300da"

@app.route('/extract-pdf', methods=['POST'])
def extract_pdf():
    try:
        # Check if a file was included in the request
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400

        file = request.files['file']

        # Check if the file has a valid name
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        # Prepare the headers for the Worqhat API request
        headers = {
            'Authorization': WORQHAT_API_TOKEN,
        }

        # Send a POST request to Worqhat API with the provided PDF file
        response = requests.post(WORQHAT_API_URL, headers=headers, files={'file': (file.filename, file)})

        # Check if the request was successful
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({'error': 'PDF extraction failed'}), response.status_code

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True,port=3000)
