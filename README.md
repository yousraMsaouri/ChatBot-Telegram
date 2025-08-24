# 💬 ChatBot IA Local avec Telegram

Assistant IA privé, local, contrôlé via Telegram, basé sur Ollama et LangChain.

![Telegram Bot](demo.png) <!-- Optionnel : ajoute une capture d'écran -->

---

## 🎯 Objectif

Développer un **assistant conversationnel intelligent** fonctionnant **100 % en local**, sans envoi de données vers le cloud, et accessible via **Telegram**.  
Le but est de combiner confidentialité, simplicité d'utilisation et capacités d'IA moderne.

---

## 🧠 Fonctionnalités

- ✅ Réponses en **français**
- ✅ Mémoire de conversation (contexte)
- ✅ Modèle IA local (via Ollama)
- ✅ Interface via Telegram (accessible depuis mobile)
- ✅ Réponses courtes ou détaillées selon la demande
- ✅ Calculs simples gérés efficacement

---

## 🛠️ Technologies utilisées

| Outil | Rôle |
|------|------|
| `Ollama` | Exécute des modèles IA localement |
| `phi3:mini-4k-instruct-q4_K_M` | Modèle léger et performant |
| `LangChain` | Orchestration du prompt et chaîne de traitement |
| `python-telegram-bot` | Connexion avec Telegram |
| `Python` | Langage principal |

---

## 🚀 Comment lancer le projet

### 1. Cloner le dépôt
```bash
git clone https://github.com/TonPseudo/chatBoot.git
cd chatBoot
```

## Créer un environnement virtuel
```bash
python -m venv chatbot
.\chatbot\Scripts\Activate.ps1
```

## Installer les dépendances
```bash
pip install -r requirements.txt
```

## Lancer Ollama (dans un autre terminal)
```bash
ollama run phi3
```

## Lancer le bot Telegram
```bash
python telegram_bot.py
```

💡 Assure-toi d’avoir configuré ton token Telegram dans le code. 

## 🔐 Configuration du bot Telegram

- Parle à @BotFather sur Telegram
- Crée un nouveau bot et récupère le token
- Dans telegram_bot.py, remplace :

```bash
TELEGRAM_TOKEN = "ton_token_ici"
```

## 📦 Modèle utilisé
Modèle : phi3
Taille : ~3.8 Go de RAM
Avantage : Très bon équilibre entre performance et légèreté sur machines modestes
🔽 Télécharge-le avec : 
```bash
ollama pull phi3
```

## 📸 Capture d'écran (exemple)



## 🎓 Pourquoi ce projet ?

✅ Confidentialité : Aucune donnée n’est envoyée à une API externe
✅ Autonomie : Fonctionne sans internet (sauf pour Telegram)
✅ Pédagogie : Bonne introduction aux LLMs, LangChain, et bots

## 📂 Structure du projet
```bash
chatBoot/
├── telegram_bot.py       # Le bot principal
├── requirements.txt      # Dépendances Python
├── .gitignore            # Fichiers ignorés
└── README.md             # Ce fichier
```

## 🙌 Remerciements
Merci à Ollama, Microsoft (Phi-3), LangChain et python-telegram-bot pour leurs outils open-source.

## 📬 Contact
Yousra : yousramsaouri13@gmail.com