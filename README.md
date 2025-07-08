# 🔐 Wordsmith – Smart Password Wordlist Generator for Cybersecurity

**Wordsmith** is a Python-based smart wordlist generator that mutates base words using leetspeak, years, symbols, and patterns — inspired by the famous `rockyou.txt`.

---

## ✅ Features

- 50,000+ password combinations
- Leetspeak converter (e.g. `a` → `@`, `s` → `$`)
- Base words from any custom `samples.txt` file
- Mutates with years, symbols, digits, and casing
- Prepares a strong wordlist in seconds
- Output saved in `output/wordlist.txt`
- Legal use only (see disclaimer)

---

## 🛠️ How It Works

1. Load your keywords from `samples.txt` (names, dates, places, etc.)
2. Wordsmith mutates each keyword using leetspeak and other rules
3. Appends common password patterns (e.g. `@123`, `1995`, `!`)
4. Saves all output to a `.txt` wordlist

## 📸 Screenshot

![Screenshot](screenshot.png)


---

## ⚡ Quick Start

### 🟢 One-Line Auto Install (Recommended)

```bash
curl -L https://raw.githubusercontent.com/talhatariq708/wordsmith-password-generator/main/install.sh | bash


🔧 Manual Install (Step-by-Step)

git clone https://github.com/talhatariq708/wordsmith-password-generator.git
cd wordsmith-password-generator
python3 main.py

(Optional) Add aliases to .bashrc or .zshrc:

alias wordsmith='python3 ~/wordsmith-password-generator/main.py'
alias wordsmith-update='cd ~/wordsmith-password-generator && git pull'
source ~/.bashrc

⚠️ Limitations

    Does not crack or brute force anything by default

    Focuses only on wordlist creation, not cracking

    You must test password lists responsibly

🛡️ Legal & Ethical Disclaimer

    This tool is for legal, educational, and research use only.

Using Wordsmith, you agree:

    ✅ You will not use it for illegal or unauthorized activity

    ✅ You have permission to test any systems or services involved

    ❌ The developer is not responsible for misuse or consequences

📄 Full disclaimer: LEGAL_USE_ONLY.txt

👨‍💻 Author

Talha Tariq
🔗 GitHub: @talhatariq708
📄 License: MIT License
🛠️ Version: v1.0.0

⭐ Like the Project?

If Wordsmith helps you:

    ⭐ Star the repo

    🧠 Suggest improvements

    🛠️ Contribute on GitHub
