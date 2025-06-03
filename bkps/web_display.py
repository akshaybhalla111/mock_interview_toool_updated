# from flask import Flask, render_template, request

# app = Flask(__name__)
# response_text = ""

# @app.route("/")
# def index():
    # return render_template("index.html", response=response_text)

# @app.route("/update", methods=["POST"])
# def update():
    # global response_text
    # response_text = request.form["response"]
    # return "OK"

# def run_web_display():
    # app.run(host='0.0.0.0', port=5000)
    

from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

latest_response = ""

html_template = """
<!doctype html>
<html>
<head>
    <title>Mock Interview Assistant</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: Arial, sans-serif; padding: 1em; background-color: #f9f9f9; }
        .container { max-width: 800px; margin: auto; }
        .response-box {
            background: #fff;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            padding: 1em;
            white-space: pre-wrap;
            overflow-wrap: break-word;
            margin-top: 1em;
        }
        .copy-btn {
            float: right;
            background: #007bff;
            color: white;
            border: none;
            padding: 5px 10px;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 5px;
        }
        code {
            background: #f4f4f4;
            padding: 2px 4px;
            border-radius: 4px;
            font-family: monospace;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>📱 Mock Interview Assistant (Mobile)</h2>
        <button class="copy-btn" onclick="copyText()">Copy</button>
        <div class="response-box" id="response">Waiting for question...</div>
    </div>
    <script>
        function copyText() {
            const text = document.getElementById("response").innerText;
            navigator.clipboard.writeText(text).then(() => {
                alert("Copied!");
            });
        }

        function updateResponse() {
            fetch("/latest")
                .then(res => res.json())
                .then(data => {
                    document.getElementById("response").innerText = data.response || "Waiting for question...";
                });
        }

        setInterval(updateResponse, 3000); // Poll every 3 seconds
        updateResponse(); // Initial load
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(html_template)

@app.route("/latest")
def latest():
    return jsonify({"response": latest_response})

@app.route("/update", methods=["POST"])
def update():
    global latest_response
    latest_response = request.form["response"]
    return "OK"

def run_web_display():
    app.run(host="0.0.0.0", port=5000)

