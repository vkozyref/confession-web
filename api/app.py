from flask import Flask, request, jsonify, make_response
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)
# bot = ChatBot(
#     'Norman',
#     storage_adapter='chatterbot.storage.SQLStorageAdapter',
#     database_uri='sqlite:///database.sqlite3'
# )


bot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(bot)

# Train the chatbot based on the english corpus
trainer.train("./lang/common.yml")

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/chat', methods=['POST'])
def chat():
    req_data = request.get_json()
    text = req_data['text']

    if not text:
        return make_response(jsonify({
            'text': [
                'The attribute "text" is required.'
            ]
        }), 400)

    response = bot.get_response(text)
    response_data = response.serialize()
    return make_response(jsonify(response_data), 200)


if __name__ == '__main__':
    app.run()