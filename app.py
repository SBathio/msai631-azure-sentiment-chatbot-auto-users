import os
from flask import Flask, request, Response
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

from botbuilder.schema import Activity
from botbuilder.core import (
    BotFrameworkAdapterSettings,
    TurnContext,
    BotFrameworkAdapter
)

# Load environment variables
load_dotenv(dotenv_path="config.env")
endpoint = os.getenv("AZURE_LANGUAGE_ENDPOINT")
key = os.getenv("AZURE_LANGUAGE_KEY")

# Initialize Azure client
client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# Setup Flask
app = Flask(__name__)

# Setup Bot Adapter
adapter_settings = BotFrameworkAdapterSettings("", "")
adapter = BotFrameworkAdapter(adapter_settings)

# Define bot logic
async def process_turn(turn_context: TurnContext):
    user_input = turn_context.activity.text.strip()
    if not user_input:
        await turn_context.send_activity("Please enter a message.")
        return

    sentiment_result = client.analyze_sentiment([user_input])[0]
    sentiment = sentiment_result.sentiment
    scores = sentiment_result.confidence_scores

    if sentiment == "positive":
        reply = f"Great to hear that! 😊 (Confidence: {scores.positive:.2f})"
    elif sentiment == "negative":
        reply = f"I'm sorry to hear that. We'll look into it. (Confidence: {scores.negative:.2f})"
    else:
        reply = f"Thanks for your feedback. (Neutral confidence: {scores.neutral:.2f})"

    await turn_context.send_activity(reply)

# Flask route
@app.route("/api/messages", methods=["POST"])
def messages():
    if "application/json" in request.headers["Content-Type"]:
        body = request.json
    else:
        return Response(status=415)

    activity = Activity().deserialize(body)
    auth_header = request.headers.get("Authorization", "")

    async def call_bot_adapter():
        await adapter.process_activity(activity, auth_header, process_turn)

    try:
        import asyncio
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(call_bot_adapter())
        return Response(status=200)
    except Exception as e:
        print(f"Error occurred: {e}")
        return Response(f"Exception: {e}", status=500)

if __name__ == "__main__":
    app.run(port=3978)