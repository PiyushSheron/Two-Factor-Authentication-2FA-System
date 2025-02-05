# Two-Factor Authentication (2FA) System

## 📌 Overview
This project implements a **Two-Factor Authentication (2FA) System** that sends a **One-Time Password (OTP)** via **email and SMS** for enhanced security. The user must enter the OTP within 5 minutes to complete authentication.

## 🚀 Features
✔ **Generates a secure 6-digit OTP**  
✔ **Sends OTP via Email & SMS (Twilio)**  
✔ **Allows 3 attempts for verification**  
✔ **OTP expires after 5 minutes**  
✔ **Secure authentication flow**

## 📦 Installation
### **1️⃣ Install Dependencies**
```bash
pip install twilio
```

### **2️⃣ Configure Email & Twilio API**
- **Email Configuration:**
  - Replace `your_email@gmail.com` and `your_password` in the script.
  - Enable **Less Secure Apps** or **App Passwords** in Gmail settings.

- **Twilio SMS Configuration:**
  - Sign up at [Twilio](https://www.twilio.com/console) to get an **Account SID**, **Auth Token**, and a **Twilio Phone Number**.
  - Replace `your_twilio_account_sid`, `your_twilio_auth_token`, and `your_twilio_phone_number` in the script.

## 🛠 Usage
### **Run the script**
```bash
python two_factor_auth.py
```

### **Authentication Flow**
1. **User enters their email & phone number**
2. **OTP is sent via Email & SMS**
3. **User enters the OTP**
4. **If OTP is correct → Authentication successful** ✅
5. **If OTP is incorrect → 3 attempts allowed** ❌
6. **OTP expires after 5 minutes**

### **Example Output**
```
Enter your email to receive an OTP: user@example.com
Enter your phone number to receive an OTP: +1234567890
[+] OTP sent successfully via email!
[+] OTP sent successfully via SMS!
Enter the OTP sent to your email/SMS: 123456
[+] OTP Verified! Login successful.
```

## ⚠️ Disclaimer
This tool is for **educational and security research purposes only**. Ensure proper security practices and **do not share OTP credentials**. Unauthorized use is **illegal**.

🔒 **Stay secure!**

