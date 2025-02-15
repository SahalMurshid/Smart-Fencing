import cv2
import time
from ultralytics import YOLO
import pygame
import smtplib
from email.message import EmailMessage
from twilio.rest import Client
from dotenv import load_dotenv
import os
import geocoder  # For getting the live location (latitude and longitude)

# ✅ Load credentials from .env file
load_dotenv("credentials.env")

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
ALERT_EMAIL = os.getenv("ALERT_EMAIL")

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH = os.getenv("TWILIO_AUTH")
TWILIO_PHONE = os.getenv("TWILIO_PHONE")
ALERT_PHONE = os.getenv("ALERT_PHONE")

# ✅ Load YOLO model
model = YOLO("models/yolov8n.pt")

# ✅ Initialize camera
cap = cv2.VideoCapture(0)  
if not cap.isOpened():
    print("❌ Error: Could not open camera. Try changing camera index (e.g., 1 or 2).")
    exit()

# ✅ Initialize Sound System
pygame.mixer.init()
alert_sound = "sounds/alert.mp3"

# ✅ Function to get live location (latitude and longitude)
def get_location():
    g = geocoder.ip('me')  # Get location based on IP address
    if g.latlng:
        return f"Latitude: {g.latlng[0]}, Longitude: {g.latlng[1]}"
    else:
        return "Location not available"

# ✅ Function to send Email alert
def send_email(location):
    try:
        msg = EmailMessage()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = ALERT_EMAIL
        msg["Subject"] = "🚨 Elephant Alert!"
        msg.set_content(f"An elephant is near the fence! Please take action immediately.\nLocation: {location}")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        print("📧 Email Alert Sent!")
    except Exception as e:
        print(f"❌ Email Sending Failed: {e}")

# ✅ Function to send SMS alert using Twilio
def send_sms(location):
    try:
        client = Client(TWILIO_SID, TWILIO_AUTH)
        message = client.messages.create(
            body=f"🚨 Elephant Detected! It is near the fencing. Take action immediately!\nLocation: {location}",
            from_=TWILIO_PHONE,
            to=ALERT_PHONE
        )
        print(f"📱 SMS Alert Sent! Message SID: {message.sid}")
    except Exception as e:
        print(f"❌ SMS Sending Failed: {e}")

# ✅ Function to play warning sound (avoids overlapping)
def play_warning_sound():
    try:
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(alert_sound)
            pygame.mixer.music.play()
            print("🔊 Warning Sound Played!")
    except Exception as e:
        print(f"❌ Sound Error: {e}")

# ✅ Function to flash lights (Simulated for now)
def flash_lights():
    print("💡 Flashing Lights ON")
    for _ in range(5):  
        print("💡 ON")
        time.sleep(0.5)
        print("💡 OFF")
        time.sleep(0.5)
    print("💡 Flashing Lights OFF")

# ✅ Function to activate shockwave deterrent
def activate_shockwave():
    print("⚡ Shockwave Activated!")

# ✅ Detection Loop
alert_level = 0  # 0 = Safe, 1 = Warning, 2 = Danger

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO detection
    results = model(frame)

    new_alert_level = 0  # Default is Safe Zone

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            confidence = float(box.conf[0])
            label = r.names[int(box.cls[0])]

            if label == "elephant" and confidence > 0.5:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.putText(frame, f"Elephant {confidence:.2f}", (x1, y1 - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

                size = x2 - x1  # Approximate elephant size in frame

                if size < 150:  
                    new_alert_level = max(new_alert_level, 0)  # Safe Zone
                elif 150 <= size < 300:  
                    new_alert_level = max(new_alert_level, 1)  # Warning Zone
                else:  
                    new_alert_level = max(new_alert_level, 2)  # Danger Zone

    # 🚨 Apply actions based on alert level changes
    if new_alert_level == 1 and alert_level < 1:  # Entering Warning Zone
        print("⚠️ Elephant Approaching (Warning Zone)")
        play_warning_sound()
        flash_lights()

    if new_alert_level == 2 and alert_level < 2:  # Entering Danger Zone
        print("🚨 Elephant VERY CLOSE (Danger Zone)")

        # Get current live location and send alerts
        location = get_location()

        # Send email and SMS with live location
        send_email(location)
        send_sms(location)

        # Activate shockwave
        activate_shockwave()

    alert_level = new_alert_level  # Update alert level

    cv2.imshow("Elephant Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
