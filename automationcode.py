from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# Load Excel
data = pd.read_excel("contactsexcelsheet.xlsx", header=None)
numbers = data[0].astype(str).tolist()

# Open browser once
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
input("📱 Scan the QR code and press Enter here...")

# Message
message = '''Hi Participants,

We’re thrilled to have you onboard for EscalateX V2 – CTF Prescreening, organized by Cyberonites, happening on 11th October! ⚡

To ensure smooth communication and timely updates regarding the event, please join our official groups using the links below:

🔗 Discord: https://discord.gg/AxvUpzTUsd
📱 WhatsApp: https://chat.whatsapp.com/KUqx77sOFHm7cg4fJUyNSe?mode=ems_copy_t

All important announcements, guidelines, and discussions will be shared there — so make sure you join both groups at the earliest.

Get ready to test your skills, collaborate, and dive deep into challenges that await you at EscalateX V2! 💻🔥

Best regards,
Team Cyberonites
EscalateX V2 Organizing Team'''

for number in numbers:
    phone = f"+{number.strip()}"
    driver.get(f"https://web.whatsapp.com/send?phone={phone}&text={message}")
    time.sleep(8)  # wait for chat to load

    # Press Enter to send
    try:
        send_btn = driver.find_element(By.XPATH, '//div[@aria-label="Send"]')
        send_btn.click()
        time.sleep(3)
        print(f"✅ Sent to {phone}")
    except Exception as e:
        print(f"❌ Failed to send to {phone}: {e}")
    time.sleep(2)
    

driver.quit()
