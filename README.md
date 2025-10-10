## 💬 Real-World Usage Scenario

Let’s say you want to **send a bulk message from your personal WhatsApp account** — for example, an event announcement, invitation, or update — to a large list of contacts. Doing this manually would take hours.

This Python script automates that process safely and efficiently using **WhatsApp Web** and **Selenium**.

---

### 🧩 What This Code Does

- It automatically opens WhatsApp Web in your browser.
- Reads all phone numbers from an Excel sheet (`contactsexcelsheet.xlsx`).
- Sends the **same message** to every contact listed there.
- You can fully customize the message in the Python file.
- Each message is sent one by one — not as a group chat — just like you would do manually.

---

### ⚠️ Important Safety & Usage Guidelines

WhatsApp has strict policies regarding bulk or automated messaging.

To avoid triggering spam filters or getting your account temporarily blocked, you **must** follow these safety practices:

1. **Send in small batches:**
    - Only keep **100 – 120 contacts** in the Excel file at one time in the day.
    - This keeps the messaging activity within normal user behavior.
2. **Delete old contacts after each batch:**
    - After sending messages to the first 100 – 120 people, remove those numbers from the Excel file.
    - Add your next batch of contacts, then repeat the process.
3. **Take long breaks between batches:**
    - After every batch of 100 – 120 messages,
        
        wait at least **3 – 4 hours** before sending again.
        
    - This mimics human use and prevents WhatsApp from flagging your account.
4. **Consider using different accounts for large campaigns:**
    - If you must message several hundred people, use separate verified accounts.
    - Never try to send thousands of messages in a single run.
5. **Respect WhatsApp policies:**
    - Always check WhatsApp’s official terms on bulk or automated messaging.
    - Do not use this for unsolicited messages, advertisements, or spam.
    - This script is meant for **personal, educational, and event-coordination purposes only**.

---

### 🧠 Example Workflow

1. Prepare an Excel file `contactsexcelsheet.xlsx` with ~100 contact numbers (including country codes).
2. Run the Python script:
    
    ```bash
    python automationcode.py
    
    ```
    
3. Scan the QR code to log in to WhatsApp Web.
4. The script automatically sends your predefined message to everyone in that Excel file.
5. When finished:
    - Delete those 100 – 120 numbers from Excel.
    - Add the next batch of contacts.
    - Wait 5-6 hours, then run the script again.

Following this cycle lets you safely reach a large audience over time **without getting your WhatsApp account flagged or blocked**.

---

### 🧩 Example Use Case

Suppose you’re organizing an event, like **EscalateX V2**, and you need to send an official update message to 500+ participants.

Here’s how you can do it safely:

1. Divide the 500 contacts into 5 Excel files, each with ~100 numbers.
2. Run the script for the first file.
3. Wait 5-6 hours.
4. Replace the Excel file contents with the next 100 contacts and run again.
5. Repeat until all participants have received the message.

This staged, careful approach keeps your account secure and ensures that everyone receives the intended information without issue.

---

### ✅ Summary

| Step | Action | Reason |
| --- | --- | --- |
| 1 | Keep only 100–120 numbers in Excel | Stay under WhatsApp’s safety limit |
| 2 | Delete old contacts after sending | Prevent duplicate sends |
| 3 | Wait 5-6 hours between batches | Mimic real user activity |
| 4 | Use multiple WhatsApp accounts if needed | Reduce account risk |
| 5 | Follow WhatsApp policies | Prevent bans or restrictions |

---

### 📄 Disclaimer

This tool is intended for **educational and productivity purposes** — such as managing event updates or reminders.


## ⚙️ Setup & Installation

### 1. Requirements

Install Python 3.8+ and the following dependencies:

## 1. Prerequisites

- **Python packages:**  
  Install required packages:
  ```bash
  pip install selenium pandas openpyxl
  ```
- **Google Chrome:**  
  [Download Chrome](https://www.google.com/chrome/)
- **ChromeDriver:**  
  ChromeDriver must be installed and added to your system PATH.  
  [Download ChromeDriver](https://chromedriver.chromium.org/downloads)

---

## 2. Folder Structure

```
whatsapp-bulk-messenger/
├── automationcode.py
├── contactsexcelsheet.xlsx
├── README.md
├── LICENSE
└── .gitignore
```

---

## 3. Excel File Format (`contactsexcelsheet.xlsx`)

Save your contacts in one column, like:

```
Contact Numbers
917777777777
15555555555
91111133333
```
- **Include the country code** (e.g., 91 for India).
- **No plus (+) sign.**

---

## 4. Running the Script

1. **Place** `contactsexcelsheet.xlsx` in the same folder as `automationcode.py`.
2. **Update** the message variable inside `automationcode.py` as you wish.
3. **Open a terminal** in the project folder and run:
   ```bash
   python automationcode.py
   ```
4. **Scan the QR code** when WhatsApp Web opens.
5. The script will automatically send your message to all numbers listed in the Excel file.

---

## 💬 Bulk Messaging Scenario (How to Use Safely)

WhatsApp enforces strict anti-spam measures.  
**Follow these safety steps to avoid account blocking:**

1. **Send messages in small batches (100–120 contacts at a time):**
   - Add only 100–120 numbers in your Excel file.
   - This keeps your activity looking natural.

2. **Delete old contacts after sending:**
   - Remove those 100–120 contacts from Excel after sending.
   - Add new contacts for the next batch.

3. **Wait before the next batch:**
   - Take a 3–4 hour gap between each run.

4. **Use multiple WhatsApp accounts if necessary:**
   - For large lists (500+), divide your contacts and use different accounts.

5. **Avoid repeated identical messages:**
   - Slightly vary your text or personalize it (e.g., “Hi [Name]”).

6. **Comply with WhatsApp’s policy:**
   - Only message users who have opted in or are part of your community.
   - **Do not use this for spam or promotions.**

---

## 🧩 Example Workflow

Suppose you need to message 500 event participants:

- **Divide** 500 numbers into 5 Excel files (~100 contacts each).
- **Run** the script for the first file.
- **Wait** 3–4 hours.
- **Replace** Excel contents with the next batch.
- **Repeat** until all are messaged.

---

## ✅ Summary Table

| Step | Action                             | Reason                       |
|------|------------------------------------|------------------------------|
| 1    | Keep only 100–120 contacts/batch   | Stay within safe limits      |
| 2    | Delete sent contacts, add new ones | Avoid duplicates             |
| 3    | Wait 3–4 hours between runs        | Mimic human use              |
| 4    | Use alternate accounts for big lists| Reduce flagging risk         |
| 5    | Respect WhatsApp’s policy          | Prevent bans                 |

---

## 🧩 Example Message (inside the code)

```python
message = '''Hi Participants,

We’re thrilled to have you onboard for EscalateX V2 – CTF Prescreening, organized by Cyberonites, happening on 11th October! ⚡

To ensure smooth communication and timely updates, please join our official groups:

🔗Discord: <https://discord.gg/Aaaaaaaaaaaaaa
   WhatsApp: <https://chat.whatsapp.com/Kkkkkkkkkkkkkkkkkkkkkkkk

Best regards,
Team Cyberonites
EscalateX V2 Organizing Team'''
```

---

## 📄 License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## ⚠️ Disclaimer

This project is for educational and productivity purposes only.  
The author does **not** encourage any misuse or violation of WhatsApp’s Terms of Service.

**Use responsibly. The author is not liable for any misuse, account bans, or policy violations resulting from improper use of this tool.**

---

## 👨‍💻 Author

**Pratyaksh Gupta**  
_Made with ❤️ using Python, Selenium, and GPT-powered assistance._

---

## ✅ Next Steps for You

1. Create a file named `README.md` in your project folder.
2. Paste the above text.
3. Add the `LICENSE`, `.gitignore`, and `requirements.txt` files as shared earlier.
4. Push to GitHub — your repository will look professional and complete.

---d in compliance with WhatsApp’s Terms of Service.

The author takes no responsibility for any misuse or policy violations.
