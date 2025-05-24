# 🛡️ AI-Powered Smart Elephant Fencing System

## 📌 Project Overview
This AI-driven fencing system is designed to prevent human-elephant conflicts by detecting elephants in real-time and triggering automated deterrents. The system utilizes **YOLO (You Only Look Once) object detection**, combined with **sound, flashing lights, and shockwave deterrents**, to safely guide elephants away from human settlements.

## 🔥 Key Features

- **🐘 AI Detection (YOLO):** Real-time elephant detection using a YOLO-based deep learning model.
- **🚨 Automated Alerts:** Triggers **sound alarms, flashing lights**, and sends notifications via **email and SMS (Twilio)**.
- **🌐 Remote Monitoring:** Enables users to monitor detection logs and alerts remotely.
- **⚡ Smart Energy-Efficient Operation:** Only activates deterrents when necessary to conserve power.
- **📡 Portable & Scalable:** Designed to operate with multiple cameras and minimal hardware requirements.

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/Smart-Fencing.git
cd Smart-Elephant-Fencing
```

### 2️⃣ Install Dependencies
Ensure you have Python installed, then install required libraries:
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up Environment Variables
Create a `.env` file in the project directory and add the following credentials:
```
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_email_password
ALERT_EMAIL=alert_receiver@gmail.com

TWILIO_SID=your_twilio_sid
TWILIO_AUTH=your_twilio_auth_token
TWILIO_PHONE=your_twilio_phone_number
ALERT_PHONE=recipient_phone_number
```

### 4️⃣ Run the AI Detection System
```bash
python elephant_detection.py
```

---

## 🏗️ Project Structure
```
📂 Smart-Elephant-Fencing
 ┣ 📂 models            # Pre-trained YOLO models
 ┣ 📂 sounds            # Alarm sound files
 ┣ 📂 images            # Sample detection images
 ┣ 📜 elephant_detection.py   # Main AI detection script
 ┣ 📜 credentials.env    # Environment variables (Do not share!)
 ┣ 📜 requirements.txt   # Python dependencies
 ┣ 📜 README.md          # Project documentation
```

---

## 📬 Alerts & Notifications
- **📧 Email Alerts**: Uses Gmail SMTP to send email notifications when an elephant is detected.
- **📱 SMS Alerts (Twilio)**: Sends SMS messages to designated recipients for real-time alerts.

---

## ⚡ Future Improvements
- ✅ Cloud-based monitoring dashboard
- ✅ Integration with IoT devices for better control
- ✅ Advanced AI models for improved detection accuracy

---

## 👥 Contributors
- **Your Name** – [Sahal Murshid](https://github.com/SahalMurshid)
- Feel free to contribute by creating pull requests!

---

## 📜 License
This project is **open-source** under the **MIT License**.

---

### 🌟 Show Your Support
If you found this project helpful, consider giving it a **⭐ star** on GitHub!
