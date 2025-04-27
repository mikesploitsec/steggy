# Steggy: Steganography Password Brute-Forcer

Built by: mikesploit

License: CC BY-NC 4.0 (Non-Commercial)

Contact: mikesploit@proton.me

# Summary:

Steggy is a lightweight Python tool designed to automate brute-forcing password-protected steghide containers. It was created during the Brooklyn Nine Nine CTF to solve a real-world steganography challenge where no off-the-shelf solutions fit the need.

# Features

- Simple command-line interface.

- Brute-forces steghide password-protected images or audio files.

- Supports custom wordlists.

- Quick feedback on successful or failed attempts.

# Usage
```
python3 steggy.py --file <stegfile> --wordlist <wordlist.txt>
```
Example:
```
python3 steggy.py --file brooklyn99.jpg --wordlist /usr/share/wordlists/rockyou.txt
```
# Requirements

- steghide must be installed and accessible from the terminal.

- Python 3.x

You can install steghide on Debian/Ubuntu with:
```
sudo apt update
sudo apt install steghide
```
# Why Steggy?

Most brute-forcing approaches for steghide are either too bloated, outdated, or broken.Steggy was built to:

- Be easy to run during CTFs or pentests.
- Focus only on password extraction — no extra noise.
- Stay minimalistic and fast.

### Disclaimer

Steggy is intended for educational and lawful penetration testing purposes only.Unauthorized use of this tool against systems you don't own is illegal and unethical.
