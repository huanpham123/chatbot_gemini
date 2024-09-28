from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    prompt = request.form['question']  # Đảm bảo sử dụng 'question' cho trường input
    api_url = f'https://deku-rest-api.gleeze.com/new/gemini?prompt={prompt}'

    try:
        response = requests.get(api_url)
        result = response.json()

        if 'result' in result and 'data' in result['result']:
            chatbot_response = result['result']['data']
        else:
            chatbot_response = 'Không có phản hồi phù hợp từ API.'
    except Exception as e:
        chatbot_response = 'Có lỗi xảy ra khi kết nối API.'

    return {'answer': chatbot_response}  # Trả về JSON thay vì render lại template

if __name__ == '__main__':
    app.run(debug=True)
