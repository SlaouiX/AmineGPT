from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Appel de ChatGPT avec la clé API 
openai.api_key = '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'

# Définir la route pour la page HTML
@app.route("/")
def home():
    return render_template("index.html")

# Définir la route pour l'interaction avec le code Python
@app.route("/ask_gpt", methods=["POST"])
def ask_gpt():
    user_input = request.json["user_input"]
    response = ask_gpt_from_openai(user_input)
    return jsonify({"response": response})

# Fonction pour interroger ChatGPT avec un prompt donné
def ask_gpt_from_openai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  
         messages=[{"role": "user", "content": prompt}],
        max_tokens= 100  # Nombre maximum de tokens pour la réponse
    )
    text = response["choices"][0]["message"]["content"]
    print(text.strip())
    return text.strip()

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 80)
