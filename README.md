# 🔐 Data-Breach-Checker

A command-line based Python tool that checks whether an email address or username appears in known data breaches using the BreachDirectory API.

It helps users identify exposed credentials, leaked passwords, SHA-1 hashes, and breach sources.

---

## 🚀 Features

- 🔎 Search leaked credentials by email/username
- 🔐 Detect exposed plaintext passwords
- 🧾 Display SHA-1 password hashes
- 📂 Show breach sources
- 💾 Export results to files
- ⚡ Fast API-based scanning
- 🖥️ Lightweight CLI tool

---

## 🛠️ Technologies Used

- Python 3
- Requests Library
- Argparse
- JSON
- RapidAPI
- BreachDirectory API

---

## 📂 Project Structure

```
Data-Breach-Checker/

│── BreachCheck.py
│── conf.json
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/sheshi-1234/Data-Breach-Checker.git
```

Enter folder:

```bash
cd Data-Breach-Checker
```

---

## 🐧 Linux / Kali Setup

Create virtual environment:

```bash
python3 -m venv venv
```

Activate environment:

```bash
source venv/bin/activate
```

Install requirements:

```bash
pip install -r requirements.txt
```

---

## 🔑 API Configuration

Create a RapidAPI account and subscribe to BreachDirectory API.

Open:

```
conf.json
```

Add your API key:

```json
{
    "BreachedDirectory":"YOUR_API_KEY"
}
```

Save the file.

---

# ▶️ Usage

Basic scan:

```bash
python3 BreachCheck.py -t example@gmail.com
```

Example:

```bash
python3 BreachCheck.py -t user@test.com
```

---

## 💾 Save Output

Save full API response:

```bash
python3 BreachCheck.py -t example@gmail.com -oR result.json
```

Save password/hash list:

```bash
python3 BreachCheck.py -t example@gmail.com -oN passwords.txt
```

---

## Example Output

```
[+] Successful API call to BreachDirectory

[+] Found target in 5 data breaches


[+] Plaintext Passwords

[+] Website: leakedpassword123


[+] SHA1 Passwords

[+] Website: A94A8FE5CC...
```

---

## ⚠️ Disclaimer

This project is created for:

- Cybersecurity learning
- OSINT research
- Security awareness
- Personal breach checking

Do not use this tool for unauthorized access, illegal activities, or attacking others.

The developer is not responsible for misuse.

---

## 👨‍💻 Developer

**Korra Sheshi Kumar**

GitHub:  
https://github.com/sheshi-1234

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
