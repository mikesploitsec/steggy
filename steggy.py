#!/usr/bin/env python3

import subprocess

def brute_force_steg(file_path, wordlist_path):
    with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
        passwords = f.read().splitlines()

    for password in passwords:
        print(f"[*] Trying: {password}")
        try:
            result = subprocess.run(
                ["steghide", "extract", "-sf", file_path, "-p", password],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            if "wrote extracted data" in result.stdout.lower():
                print(f"[+] Password cracked! --> {password}")
                return password
        except Exception as e:
            print(f"[!] Error: {e}")

    print("[-] Password not found.")
    return None

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Steghide password brute-forcer.")
    parser.add_argument("-f", "--file", required=True, help="Path to steghide file (e.g., hidden.jpg)")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to wordlist (e.g., rockyou.txt)")

    args = parser.parse_args()

    brute_force_steg(args.file, args.wordlist)
