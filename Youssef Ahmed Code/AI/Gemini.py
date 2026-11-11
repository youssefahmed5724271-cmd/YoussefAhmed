from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# HTML & CSS Chat Interface template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YAG System - AI Chatbot</title>
    <style>
        body {
            background-color: #f0f2f5;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .chat-container {
            width: 480px;
            height: 620px;
            background: white;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }
        .chat-header {
            background-color: #007bff;
            color: white;
            padding: 20px;
            text-align: center;
            font-size: 20px;
            font-weight: bold;
        }
        .chat-box {
            flex: 1;
            padding: 20px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 12px;
            background-color: #f8f9fa;
        }
        .message {
            max-width: 75%;
            padding: 10px 14px;
            border-radius: 10px;
            font-size: 14px;
            line-height: 1.4;
            word-wrap: break-word;
        }
        .user-message {
            background-color: #007bff;
            color: white;
            align-self: flex-end;
            border-bottom-right-radius: 2px;
        }
        .bot-message {
            background-color: #e9ecef;
            color: #333;
            align-self: flex-start;
            border-bottom-left-radius: 2px;
            white-space: pre-line;
        }
        .chat-input-area {
            display: flex;
            padding: 15px;
            background: white;
            border-top: 1px solid #dee2e6;
        }
        .chat-input-area input {
            flex: 1;
            padding: 10px 14px;
            border: 1px solid #ced4da;
            border-radius: 20px;
            outline: none;
            font-size: 14px;
        }
        .chat-input-area button {
            background-color: #007bff;
            color: white;
            border: none;
            padding: 10px 20px;
            margin-left: 10px;
            border-radius: 20px;
            cursor: pointer;
            font-weight: bold;
        }
        .chat-input-area button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="chat-container">
        <div class="chat-header">Welcome to YAG System</div>
        <div class="chat-box" id="chatBox">
            <div class="message bot-message">Hi! I am YAG System. Ask me anything or type 'help'!</div>
        </div>
        <div class="chat-input-area">
            <input type="text" id="userInput" placeholder="Type your message..." onkeypress="handleKeyPress(event)">
            <button onclick="sendMessage()">Send</button>
        </div>
    </div>

    <script>
        const chatBox = document.getElementById('chatBox');
        const userInput = document.getElementById('userInput');

        function appendMessage(text, sender) {
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${sender}-message`;
            messageDiv.innerText = text;
            chatBox.appendChild(messageDiv);
            chatBox.scrollTop = chatBox.scrollHeight;
        }

        function sendMessage() {
            const text = userInput.value.trim();
            if (!text) return;

            appendMessage(text, 'user');
            userInput.value = '';

            fetch('/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: text })
            })
            .then(response => response.json())
            .then(data => {
                appendMessage(data.response, 'bot');
            })
            .catch(error => {
                appendMessage('Error communicating with server.', 'bot');
            });
        }

        function handleKeyPress(event) {
            if (event.key === 'Enter') {
                sendMessage();
            }
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip().lower()
    
    # Chatbot logic handling
    response_text = get_bot_response(user_message)
    return jsonify({"response": response_text})

def get_bot_response(user_message):
    if user_message in {"hi", "hello", "hey"}:
        return "Hi, I am your chatbot!"
    elif user_message == "who are you":
        return "I am your chatbot, ask me anything."
    elif user_message == "what is your name":
        return "I am your chatbot, YAG System."
    elif user_message == "how are you":
        return "I am fine, thank you!"
    elif user_message == "what can you do":
        return "I can chat with you, answer questions, tell jokes, and give code examples."
    elif user_message == "tell me a joke":
        return "Why did the scarecrow win an award? Because he was outstanding in his field!"
    elif user_message == "tell me a fun fact":
        return "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs over 3,000 years old that are still edible!"
    elif user_message == "what is the capital of france":
        return "The capital of France is Paris."
    elif user_message == "what is 2 plus 2":
        return "2 plus 2 is 4."
    elif user_message == "help":
        return "I can answer general knowledge questions, tell jokes, provide fun facts, and give simple code examples. Just type your question!"
    elif user_message == "thank you":
        return "You are welcome!"
    elif user_message == "what programming language are you written in":
        return "I am written in Python using Flask."
    elif user_message == "what is the name of your programmer":
        return "My programmer is Youssef Ahmed Heilmy."
    else:
        return f"I received your message: '{user_message}'. Try asking me for a joke, fun fact, or type 'help'!"

if __name__ == "__main__":
    app.run(debug=True, port=5000)