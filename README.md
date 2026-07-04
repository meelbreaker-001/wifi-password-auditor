# Wi-Fi Password Security Auditor

A Python-based tool to evaluate Wi-Fi password strength, analyze captured
WPA/WPA2 handshakes, and generate security audit reports.

## ⚠️ Legal & Ethical Disclaimer

**This tool is for educational purposes and authorized security testing only.**

- Only use the handshake capture and cracking features on networks **you own**
  or have **explicit written permission** to test.
- Unauthorized access to wireless networks is illegal under computer misuse /
  cybercrime laws in most countries.
- The **Password Strength Checker** module does NOT require any network access
  and is completely safe to use on any password string for demonstration,
  learning, and academic purposes.

## Features

- **Password Strength Checker** – entropy calculation, character variety
  analysis, common-password detection (no network access needed)
- **Handshake Analyzer** – wraps `aircrack-ng` / `hashcat` to test captured
  handshakes against wordlists (requires authorized capture file)
- **Report Generator** – produces a PDF/HTML summary with recommendations

## Project Structure

```
wifi-password-auditor/
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── setup.py
├── config/
│   └── settings.yaml
├── src/wifi_auditor/
│   ├── __init__.py
│   ├── main.py
│   ├── capture.py
│   ├── cracker.py
│   ├── strength_checker.py
│   ├── report.py
│   └── utils.py
├── wordlists/
│   └── README.md
├── tests/
│   ├── test_strength_checker.py
│   ├── test_cracker.py
│   └── test_utils.py
├── reports/
├── docs/
│   └── usage.md
└── .github/workflows/ci.yml
```

## Installation

```bash
git clone https://github.com/yourusername/wifi-password-auditor.git
cd wifi-password-auditor
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

### 1. Check password strength (safe, no special tools needed)

```bash
python -m src.wifi_auditor.main --check-strength "MyP@ssw0rd123"
```

### 2. Analyze a captured handshake (requires aircrack-ng/hashcat + authorized capture)

```bash
python -m src.wifi_auditor.main --analyze-handshake capture.cap --wordlist wordlists/rockyou.txt
```

### 3. Generate a PDF report

```bash
python -m src.wifi_auditor.main --check-strength "MyP@ssw0rd123" --report
```

## Requirements

- Python 3.9+
- (Optional, for handshake analysis) Kali Linux or any distro with:
  - `aircrack-ng`
  - `hashcat`
  - A wireless adapter supporting monitor mode

## License

MIT License – see `LICENSE` file.
