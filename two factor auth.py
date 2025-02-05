import random
import smtplib
import time
from twilio.rest import Client

# Function to generate a random 6-digit OTP
def generate_otp():
    return str(random.randint(100000, 999999))

# Function to send OTP via email
def send_otp_email(receiver_email, otp):
    sender_email = "your_email@gmail.com"  # Replace with your email
    sender_password = "your_password"  # Replace with your email password
    
    subject = "Your OTP Code"
    body = f"Your One-Time Password (OTP) is: {otp}. It will expire in 5 minutes."
    
    message = f"Subject: {subject}\n\n{body}"
    
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)
        server.quit()
        print("[+] OTP sent successfully via email!")
    except Exception as e:
        print("[-] Error sending OTP via email:", e)

# Function to send OTP via SMS
def send_otp_sms(receiver_phone, otp):
    account_sid = "your_twilio_account_sid"  # Replace with your Twilio SID
    auth_token = "your_twilio_auth_token"  # Replace with your Twilio Auth Token
    twilio_phone = "your_twilio_phone_number"  # Replace with your Twilio phone number
    
    client = Client(account_sid, auth_token)
    
    try:
        message = client.messages.create(
            body=f"Your OTP Code is: {otp}. It will expire in 5 minutes.",
            from_=twilio_phone,
            to=receiver_phone
        )
        print("[+] OTP sent successfully via SMS!")
    except Exception as e:
        print("[-] Error sending OTP via SMS:", e)

# Function to verify OTP
def verify_otp(sent_otp):
    attempts = 3
    while attempts > 0:
        user_otp = input("Enter the OTP sent to your email/SMS: ")
        if user_otp == sent_otp:
            print("[+] OTP Verified! Login successful.")
            return True
        else:
            attempts -= 1
            print(f"[-] Incorrect OTP. Attempts remaining: {attempts}")
    print("[!] Maximum attempts reached. Try again later.")
    return False

if __name__ == "__main__":
    email = input("Enter your email to receive an OTP: ")
    phone = input("Enter your phone number to receive an OTP (with country code, e.g., +1234567890): ")
    otp = generate_otp()
    
    send_otp_email(email, otp)
    send_otp_sms(phone, otp)
    
    # Allow OTP verification within 5 minutes
    start_time = time.time()
    while time.time() - start_time < 300:  # 300 seconds = 5 minutes
        if verify_otp(otp):
            break
    else:
        print("[!] OTP expired. Request a new one.")
