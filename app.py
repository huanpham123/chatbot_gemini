from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# URL API của bạn
API_URL = "https://deku-rest-api.gleeze.com/new/gemini"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def chatbot():
    user_input = request.form['question']
    response = requests.post(API_URL, json={"prompt": user_input})

    if response.status_code == 200:
        data = response.json()
        answer = data['result']['data']  # Chỉ lấy câu trả lời
        return jsonify({'answer': answer})
    else:
        return jsonify({'answer': 'Có lỗi xảy ra!'}), 500

if __name__ == '__main__':
    app.run()
