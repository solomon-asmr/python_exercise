# notification_manager.py
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    def __init__(self):
        self.client = Client(
            os.getenv("TWILIO_SID"),
            os.getenv("TWILIO_AUTH_TOKEN")
        )
        self.from_number = os.getenv("TWILIO_VIRTUAL_NUMBER")
        self.to_number = os.getenv("TWILIO_VERIFIED_NUMBER")

    def send_message(self, message):
        """Send SMS/WhatsApp message"""
        try:
            msg = self.client.messages.create(
                from_=self.from_number,
                body=message,
                to=self.to_number
            )
            print(f"✅ Message sent: SID={msg.sid}")
        except Exception as e:
            print(f"❌ Failed to send message: {e}")
