# main.py

from generator import generate_passwords

def load_base_words(filename="samples.txt"):
    try:
        with open(filename, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("❌ 'samples.txt' not found.")
        return []

def save_to_file(passwords, filename="output/wordlist.txt"):
    with open(filename, "w") as f:
        for pwd in passwords:
            f.write(pwd + "\n")
    print(f"✅ Generated {len(passwords)} passwords and saved to {filename}")

def print_banner():
    print(r"""
 __      __                _       _     _     
 \ \    / /               | |     (_)   | |    
  \ \  / /_ _ _ __  _ __  | | ___  _  __| |___ 
   \ \/ / _` | '_ \| '_ \ | |/ _ \| |/ _` / __|
    \  / (_| | |_) | |_) || | (_) | | (_| \__ \
     \/ \__,_| .__/| .__(_)_|\___/|_|\__,_|___/
             | |   | |                        
             |_|   |_|         Talha
""")

def main():
    print_banner()

    base_words = load_base_words()
    if not base_words:
        print("❌ No base words found.")
        return

    passwords = generate_passwords(base_words)
    save_to_file(passwords)

if __name__ == "__main__":
    main()
