# 📱 WhatsApp Bulk Messenger

A Python automation script to send bulk messages through WhatsApp Web using Selenium. This tool helps you send the same message to multiple contacts efficiently and safely.

---

## 💬 Real-World Usage Scenario

Let's say you want to **send a bulk message from your personal WhatsApp account** — for example, an event announcement, invitation, or update — to a large list of contacts. Doing this manually would take hours.

This Python script automates that process safely and efficiently using **WhatsApp Web** and **Selenium**.

---

## 🧩 What This Code Does

- Automatically opens WhatsApp Web in your browser
- Reads all phone numbers from an Excel sheet (`contactsexcelsheet.xlsx`)
- Sends the **same message** to every contact listed
- Fully customizable message in the Python file
- Each message is sent one by one — not as a group chat — just like you would do manually

---

## ⚙️ Setup & Installation

### Prerequisites

Before running the script, ensure you have the following installed:

- **Python 3.8+**
- **Google Chrome Browser** - [Download Chrome](https://www.google.com/chrome/)
- **ChromeDriver** - Must be installed and added to your system PATH  
  [Download ChromeDriver](https://chromedriver.chromium.org/downloads)

### Install Required Python Packages

```bash
pip install selenium pandas openpyxl
```

---

## 📂 Folder Structure

```
whatsapp-bulk-messenger/
├── automationcode.py
├── contactsexcelsheet.xlsx
├── README.md
├── LICENSE
└── .gitignore
```

---

## 📋 Excel File Format

Create `contactsexcelsheet.xlsx` with phone numbers in the first column:

```
Contact Numbers
917777777777
15555555555
91111133333
```

**Important:**
- **Include the country code** (e.g., 91 for India, 1 for USA)
- **No plus (+) sign** before the number
- **No spaces or hyphens** in the numbers

---

## 🚀 Running the Script

1. **Place** `contactsexcelsheet.xlsx` in the same folder as `automationcode.py`
2. **Update** the message variable inside `automationcode.py` with your custom message
3. **Open a terminal** in the project folder and run:
   ```bash
   python automationcode.py
   ```
4. **Scan the QR code** when WhatsApp Web opens in the browser
5. The script will automatically send your message to all numbers listed in the Excel file

---

## ⚠️ Important Safety & Usage Guidelines

WhatsApp has **strict policies** regarding bulk or automated messaging. To avoid triggering spam filters or getting your account temporarily blocked, you **must** follow these safety practices:

### 1. Send in Small Batches
- Only keep **100 – 120 contacts** in the Excel file at one time
- This keeps the messaging activity within normal user behavior

### 2. Delete Old Contacts After Each Batch
- After sending messages to the first 100 – 120 people, remove those numbers from the Excel file
- Add your next batch of contacts, then repeat the process

### 3. Take Long Breaks Between Batches
- After every batch of 100 – 120 messages, wait at least **3 – 4 hours** before sending again
- This mimics human use and prevents WhatsApp from flagging your account

### 4. Consider Using Different Accounts for Large Campaigns
- If you must message several hundred people, use separate verified accounts
- Never try to send thousands of messages in a single run

### 5. Avoid Repeated Identical Messages
- Slightly vary your text or personalize it (e.g., "Hi [Name]")
- This makes messages appear more natural

### 6. Respect WhatsApp Policies
- Always check WhatsApp's official terms on bulk or automated messaging
- Do not use this for unsolicited messages, advertisements, or spam
- This script is meant for **personal, educational, and event-coordination purposes only**
- Only message users who have opted in or are part of your community

---

## 🧠 Example Workflow

### Scenario: Messaging 500 Event Participants

Suppose you're organizing an event like **EscalateX V2** and need to send an official update message to 500+ participants.

**Step-by-Step Process:**

1. **Prepare the first batch:**
   - Add 100 phone numbers to `contactsexcelsheet.xlsx`

2. **Run the script:**
   ```bash
   python automationcode.py
   ```

3. **Scan QR code** and wait for messages to be sent

4. **After sending:**
   - Delete those 100 numbers from Excel
   - Add the next batch of 100 contacts

5. **Wait 3-4 hours** before the next run

6. **Repeat** until all 500 participants have received the message

**Summary:** Divide 500 contacts into 5 batches of 100, running the script once every 3-4 hours over 2-3 days.

---

## ✅ Safety Guidelines Summary

| Step | Action | Reason |
|------|--------|--------|
| 1 | Keep only 100–120 numbers per batch | Stay under WhatsApp's safety limit |
| 2 | Delete old contacts after sending | Prevent duplicate sends |
| 3 | Wait 3–4 hours between batches | Mimic real user activity |
| 4 | Use multiple WhatsApp accounts if needed | Reduce account risk for large campaigns |
| 5 | Follow WhatsApp policies | Prevent bans or restrictions |
| 6 | Personalize messages when possible | Avoid spam detection |

---

## 🧩 Example Message

The message in `automationcode.py` can be customized like this:

```python
message = '''Hi Participants,

We're thrilled to have you onboard for EscalateX V2 – CTF Prescreening, organized by Cyberonites, happening on 11th October! ⚡

To ensure smooth communication and timely updates, please join our official groups:

🔗 Discord: https://discord.gg/YourDiscordLink
📱 WhatsApp: https://chat.whatsapp.com/YourWhatsAppLink

Best regards,
Team Cyberonites
EscalateX V2 Organizing Team'''
```

Simply edit this section in the script to match your needs.

---

## 📄 License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## ⚠️ Disclaimer

This project is for **educational and productivity purposes only** — such as managing event updates or reminders.

The author does **not** encourage any misuse or violation of WhatsApp's Terms of Service.

**Use responsibly. The author is not liable for any misuse, account bans, or policy violations resulting from improper use of this tool.**

Always ensure your messaging activities comply with WhatsApp's Terms of Service.

---

## 👨‍💻 Author

**Pratyaksh Gupta**  
_Made with ❤️ using Python, Selenium, and GPT-powered assistance._

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

---

## ⭐ Show Your Support

Give a ⭐ if this project helped you!

---

**Happy Messaging! 📱✨**
