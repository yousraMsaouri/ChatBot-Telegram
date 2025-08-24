# telegram_bot.py

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# === CONFIGURATION ===
TELEGRAM_TOKEN = "8095470447:AAFRiTYrn7JSUhMl_8iMgZCN3rLw404SuMY"  # ← Mets ton vrai token ici !
OLLAMA_MODEL = "phi3"  # ou "phi3", etc.

# === CHATBOT LOCAL (Ollama + LangChain) ===
template = """
Tu es un assistant utile. Réponds toujours en français.

Règles strictes :
1. Si la question est simple (calcul, définition, traduction, capitale, etc.), réponds **directement et brièvement**.
2. Si l'utilisateur dit "explique", "développe", ou "en détail", alors donne une réponse plus complète.
3. Jamais d'explication non demandée.
4. Ne répète pas la question.
5. Ne dis pas "Réponse :".

Exemples :
- Question : "2+2" → Réponse : "4"
- Question : "Capitale de la France ?" → Réponse : "Paris"
- Question : "Qui est Einstein ?" → Réponse : "Physicien célèbre pour la relativité."
- Question : "Explique qui est Einstein" → Réponse : "Albert Einstein était un physicien théorique..."

Historique : {context}

Question : {question}

Réponse :
"""

model = OllamaLLM(model=OLLAMA_MODEL)
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Stocker l'historique par utilisateur (si plusieurs personnes parlent)
user_contexts = {}  # {user_id: "historique..."}

# === GESTION DES COMMANDES TELEGRAM ===

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_contexts[user_id] = ""  # Initialiser l'historique
    await update.message.reply_text("Hello! I'm your AI assistant. Ask me anything! 🤖")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_input = update.message.text

    # Initialiser l'historique si nouveau
    if user_id not in user_contexts:
        user_contexts[user_id] = ""

    context = user_contexts[user_id]

    try:
        # Faire répondre le modèle
        print(f"[User {user_id}] {user_input}")
        response = chain.invoke({"context": context, "question": user_input})
        response_text = str(response).strip()

        # Envoyer la réponse
        await update.message.reply_text(response_text)

        # Mettre à jour l'historique
        user_contexts[user_id] += f"\nUser: {user_input}\nAI: {response_text}"
        # Garder seulement les 2000 derniers caractères
        user_contexts[user_id] = user_contexts[user_id][-2000:]

    except Exception as e:
        print(f"Error: {e}")
        await update.message.reply_text("Sorry, I couldn't process your request.")

# === LANCEMENT DU BOT ===
if __name__ == "__main__":
    print("🚀 Starting Telegram bot...")

    # Créer l'application
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # Ajouter les gestionnaires
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Démarrer le bot
    print("✅ Bot is running... Waiting for messages.")
    app.run_polling()