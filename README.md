# PhantomReply  

> **MULTI-ORIGIN TACTICAL DISPATCH SYSTEM**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-green?logo=linux)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Version](https://img.shields.io/badge/Version-1.0-orange)
---

## Overview
PhantomReply is a lightweight Python tool for executing multi-origin tactical email deployments through Gmail’s secure SMTP system (App Passwords + 2FA).

It supports:

- HTML or plain-text messages  
- Clean human-styled templates  
- Validation of sender + receiver emails  
- Group emailing via config  
- Automatic virtual environment setup  
- Scalable folder structure (templates, static, config)

---

## Gmail Setup (REQUIRED)

### **1. Enable 2FA on your gmail account**
Go to:  
https://myaccount.google.com/security

### **2. Create an App Password**
Required because Gmail blocks normal SMTP passwords.

Go to:  
https://myaccount.google.com/apppasswords

---

## Clone the Repo
```bash
git clone https://github.com/cyb2rS2c/PhantomReply.git
cd PhantomReply
```

Edit the file: `config.json`.

## Config File (`assets/config.json`)

Create or modify:

```json
{
  "senders": ["your_first_email@gmail.com","your_second_email@gmail.com"],
  "groups": {
    "group1": ["recipient1@example.com", "recipient2@example.com"]
  },
  "message": {
    "subject": "Test Email",
    "content": "this is a test",
    "load_file": "test.txt",
    "text_type": "plain"
  },
  "server": "smtp.gmail.com",
  "app_password": "change it"
}

- senders: list of valid Gmail addresses
- app_password: 16-character Gmail App Password
- groups: you can create unlimited groups(receivers)
- text_type: "plain" or "html"
- load_file: the path to your message contained in the file.txt (Optional)
```
## Run
```bash
chmod +x setup.sh;./setup.sh
```

## Features

- Gmail SMTP (secure)
- Email validation for sender & receivers
- HTML template loading from templates/
- CSS support from static/
- Config-based message management
- Group email support
- Error handling and safe execution
- Scalable project structure

## Screenshots
<img width="650" height="445" alt="image" src="https://github.com/user-attachments/assets/c3169dc0-2232-4cb5-abad-db3d5c0544db" />

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer
The software is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.
