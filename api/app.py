from flask import Flask, request, jsonify, make_response
from chatterbot import ChatBot

app = Flask(__name__)
bot = ChatBot(
    'Norman',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/chat', methods=['POST'])
def chat():    
    return request.form['text']
    text = request.form['text']

    if not text:
        return make_response(jsonify({
            'text': [
                'The attribute "text" is required.'
            ]
        }), status=400)

    response = bot.get_response(input_data)
    response_data = response.serialize()
    return make_response(jsonify(response_data), status=200)


if __name__ == '__main__':
    app.run()