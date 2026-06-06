from flask import Flask, render_template, request, jsonify
from rag import RAGChatbot

app = Flask(__name__)
bot = RAGChatbot("data.txt")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    response = bot.get_answer(user_message)
    return jsonify({"answer": response})

if __name__ == "__main__":
    app.run(debug=True)