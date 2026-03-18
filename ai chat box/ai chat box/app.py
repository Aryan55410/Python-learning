from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def chatbot_reply(user_text):
    
   def chatbot_reply(user_text):
    user_text = user_text.lower()

    responses = {
        "hello": "Hello! How can I help you? 😊",
        "hi": "Hi there! 👋",
        "how are you": "I'm doing great! Thanks for asking 😄",
        "your name": "I am Aryan's AI Chatbot 🤖",
        "python": "Python is widely used in AI, ML, and Web Development.",
        "help": "Sure! Tell me what you need help with."
    }

    for key in responses:
        if key in user_text:
            return responses[key]

    return "I'm still learning 🤓 Can you ask something else?"


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_msg = request.args.get("msg")
    return chatbot_reply(user_msg)

if __name__ == "__main__":
    app.run(debug=True)
 

