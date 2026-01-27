# Task 2: Keylogger Simulation

## Description
This project simulates a keylogger that records keystrokes locally in a text file. The goal is to understand how malware captures sensitive data and how to defend against such attacks.

## Security Analysis & Risks
During this task, the following risks were analyzed:
* **Credential Theft:** Capturing login data at the input level bypasses many network-level encryptions.
* **Data Persistence:** Logs provide a permanent record of unsaved or deleted sensitive text.
* **Detection Evasion:** Basic keyloggers can run silently in the background, making them difficult for average users to detect without security software.

## Mitigation Strategies
* Use of **Multi-Factor Authentication (MFA)**.
* Regular system scans with **Antivirus/EDR** tools.
* Use of **Virtual Keyboards** for highly sensitive financial transactions.

## Setup
Run the script and press `ESC` to stop logging.
