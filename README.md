# 🚗 Sentiment-Driven Chatbot for the Automotive Industry

This project is developed as part of the **AI for Human-Computer Interaction** course. It demonstrates how AI-powered sentiment analysis can enhance user interaction in the automotive service domain. Users provide feedback, and the chatbot responds with emotionally appropriate replies using Microsoft Azure's language services.

## 🎯 Problem Statement

Car dealerships and service providers often receive large volumes of unstructured customer feedback through surveys or reviews. Most of this feedback is never analyzed, leading to missed opportunities for improvement. This project addresses that gap by implementing a real-time sentiment-aware chatbot that can both analyze and respond to customer sentiment.

## 📌 Project Scope

- Input: Single-turn English text messages related to automotive experiences.
- Output: A chatbot response reflecting positive, negative, or neutral sentiment, along with a confidence score.
- Tools: Azure Text Analytics (free-tier), Flask, Microsoft Bot Framework Emulator.
- Constraints: No persistent storage, no multi-turn memory, no multilingual support.

## ⚙️ Features

- 💬 Real-time sentiment classification (positive, negative, neutral)
- ⚡ Instant feedback via Bot Framework Emulator
- 🌐 Cloud-backed processing via Azure Language API
- 🧪 One-shot feedback processing for quick validation
- 🔐 Credential management via `.env` (excluded from version control)

## 🛠 Technologies Used

- Python 3
- Flask
- Azure Cognitive Services (Text Analytics API)
- Microsoft Bot Framework Emulator
- `python-dotenv` for config handling

## 🗂 Project Structure

```
📦 Sentiment Chatbot
 ┣ 📄 app.py           # Main Flask API and bot logic
 ┣ 📄 config.env       # Local credentials (excluded from Git)
 ┣ 📄 requirements.txt # Python dependency list
 ┗ 📄 README.md        # Project documentation
```

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/SBathio/msai631-azure-sentiment-chatbot-auto-users.git
cd msai631-azure-sentiment-chatbot-auto-users
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Azure Credentials
In a `.env` or `config.env` file:
```env
AZURE_LANGUAGE_ENDPOINT=your_endpoint_here
AZURE_LANGUAGE_KEY=your_key_here
```

### 4. Run the Chatbot Server
```bash
python app.py
```

Server runs at `http://localhost:3978`

### 5. Test the Bot
Use the [Bot Framework Emulator](https://github.com/microsoft/BotFramework-Emulator)  
Connect to: `http://localhost:3978/api/messages`

## 💬 Example Interaction

**User:** “The team was helpful, but the repair took too long.”  
**Bot:** “I'm sorry to hear that. We'll look into it. (Confidence: 0.92)”

**User:** “The process was smooth and the staff was friendly.”  
**Bot:** “Great to hear that! 😊 (Confidence: 0.89)”

## 📏 Design Justification

- **Flask**: Lightweight and easy to deploy/test.
- **Azure Text Analytics**: Cloud-based, accurate NLP for sentiment.
- **Bot Framework Emulator**: Allows controlled simulation of conversational interfaces.
- **No storage layer**: Keeps the application focused and low-latency.

## ⚠️ Known Limitations

- English-only support
- Single-turn interaction (no memory of past inputs)
- No sarcasm/idiom detection
- Azure API usage is subject to free-tier rate limits

## ✅ Success Criteria

- Correct sentiment classification with confidence scores
- Natural and context-aware replies
- Robust error handling and input validation
- Local testing with clear results in the emulator

## 👥 Team Members

- [Sigou Bathily]
- [Kemal Emir Urey] 
- [Akhil Dasyam]
- [Shishir Pathak]
- [Asfandiyar Afrasiab]

## 📄 License

This project was developed for academic purposes as part of the **MSAI 631 - AI for HCI** coursework.

---

## 📌 Future Work

This system lays the groundwork for future improvements like:
- Multi-turn conversations
- Multilingual input
- Voice-based interaction
- Sentiment trend analysis over time
