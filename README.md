# 🔒 SILENT CYBER LAB - OSINT & RECON TOOLKIT

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Modules-11-green?style=for-the-badge" alt="Modules">
  <img src="https://img.shields.io/badge/API_Keys-Not_Required-success?style=for-the-badge" alt="No API Keys">
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20Mac%20%7C%20Windows-orange?style=for-the-badge" alt="Cross Platform">
</p>

<p align="center">
  <b>An all-in-one Open Source Intelligence & Reconnaissance toolkit built for ethical hackers, penetration testers, and cybersecurity professionals.</b>
</p>

---

## 📸 Preview 

```
  ███████╗██╗██╗     ███████╗███╗   ██╗████████╗
  ██╔════╝██║██║     ██╔════╝████╗  ██║╚══██╔══╝
  ███████╗██║██║     █████╗  ██╔██╗ ██║   ██║   
  ╚════██║██║██║     ██╔══╝  ██║╚██╗██║   ██║   
  ███████║██║███████╗███████╗██║ ╚████║   ██║   
  ╚══════╝╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   
           ██████╗██╗   ██╗██████╗ ███████╗██████╗ 
          ██╔════╝██║   ██║██╔══██╗██╔════╝██╔══██╗
          ██║     ██║   ██║██████╔╝█████╗  ██████╔╝
          ██║     ██║   ██║██╔══██╗██╔══╝  ██╔══██╗
          ╚██████╗╚██████╔╝██║  ██║███████╗██║  ██║
           ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
  ═══════════════════════════════════════════════════
  [ TEAM SILENT 313 ] :: OSINT & RECON TOOLKIT
  :: BUILD BY MR SILENT313 NASRU ::
  ══════════════════════════════════════════════════

  [ SYSTEM ONLINE ]  10:30:45 PM
  [ 11 MODULES LOADED ]  [ NO KEYS REQUIRED ]

  [ 1] IP LOOKUP
  [ 2] CVE SEARCH
  [ 3] SUBDOMAINS
  [ 4] DNS LOOKUP
  [ 5] WHOIS
  [ 6] HASH GEN
  [ 7] BASE64
  [ 8] PASS CHECK
  [ 9] QR CODE
  [10] USERNAME
  [11] PORT REF
  [ 0] EXIT

  SELECT MODULE >>
```

---

## 📖 About

**SILENT CYBER LAB** is a comprehensive Python-based OSINT (Open Source Intelligence) and Reconnaissance toolkit developed by **Mr Silent 313**. It consolidates 11 powerful modules into a single, easy-to-use command-line interface — no API keys required.

Whether you're conducting passive reconnaissance, analyzing vulnerabilities, or performing username enumeration across social platforms, this tool has you covered.

---

## ✨ Features

- 🚀 **Zero Configuration** — No API keys needed, just run and use
- 🎨 **Beautiful CLI Interface** — Color-coded output for better readability
- 📦 **11 Powerful Modules** — Covering IP, DNS, CVE, Subdomains, and more
- 🔍 **30+ Platform Username Check** — OSINT across major social media and dev platforms
- 🛡️ **Offline Capabilities** — Hash generation, Base64, password analysis work offline
- 📱 **Cross-Platform** — Works on Linux, macOS, Windows, and Termux

---

## 🧩 Modules Overview

| # | Module | Description |
|---|--------|-------------|
| 1 | **IP Lookup** | Geolocation, ISP, AS, and network info via ip-api.com |
| 2 | **CVE Search** | Search NVD database for CVE details and CVSS scores |
| 3 | **Subdomains** | Enumerate subdomains using an extensive wordlist |
| 4 | **DNS Lookup** | Query A, MX, NS, and TXT DNS records |
| 5 | **WHOIS** | Retrieve domain registration and ownership data |
| 6 | **Hash Generator** | Generate MD5, SHA1, SHA224, SHA256, SHA384, SHA512, BLAKE2b |
| 7 | **Base64** | Encode and decode Base64 strings |
| 8 | **Password Check** | Analyze password strength with entropy calculation |
| 9 | **QR Code** | Generate QR codes in ASCII or save as PNG |
| 10 | **Username OSINT** | Check username availability across 30+ platforms |
| 11 | **Port Reference** | Search ports by number or service name |


---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/mrsilent313-spec/313cyberlab.py.git
cd 313cyberlab.py
```

### Run the Tool

```bash
python3 313cyberlab.py
```

### Optional Dependencies

Some modules have optional dependencies for enhanced functionality:

```bash
# For QR Code PNG export
pip install qrcode[pil]

# For DNS records (MX, NS, TXT) - Linux/macOS
sudo apt install dnsutils        # Debian/Ubuntu
sudo yum install bind-utils      # CentOS/RHEL
brew install bind                # macOS

# For WHOIS lookup - Linux
sudo apt install whois           # Debian/Ubuntu
sudo yum install whois           # CentOS/RHEL
```

> **Note:** The tool works perfectly with just Python 3 standard library. Optional dependencies only unlock additional features.

---

## 📋 Requirements

- **Python 3.6+** (3.8+ recommended)
- **Internet Connection** (for IP lookup, CVE search, subdomain enumeration, username OSINT)
- **Standard Library Only** (core functionality)

---

## 📝 Module Details

### 1. IP Lookup
Retrieve detailed geolocation and network information for any IP address or domain. Uses the [ip-api.com](http://ip-api.com/) API.

```
Enter IP/Domain: 8.8.8.8
═══ IP INFORMATION ═══
IP:        8.8.8.8
Country:   United States (US)
Region:    Virginia
City:      Ashburn
ISP:       Google LLC
AS:        AS15169 Google LLC
```

### 2. CVE Search
Search the NIST National Vulnerability Database (NVD) for CVEs by ID or keyword.

```
Enter CVE ID or Keyword: CVE-2021-44228
═══ CVE RESULTS ═══
[1] CVE-2021-44228
CVSS Score: 10.0 (CRITICAL)
Description: Apache Log4j2 JNDI features do not protect against...
```

### 3. Subdomain Enumeration
Brute-force subdomains using an extensive built-in wordlist (700+ entries).

```
Enter Domain: example.com
[+] www.example.com         => 93.184.216.34
[+] mail.example.com        => 93.184.216.34
[+] Found 2 subdomains
```

### 4. DNS Lookup
Query multiple DNS record types for any domain.

### 5. WHOIS Lookup
Retrieve domain registration and ownership information.

### 6. Hash Generator
Generate 7 different hash types from any input text:
- MD5, SHA1, SHA224, SHA256, SHA384, SHA512, BLAKE2b

### 7. Base64 Tool
Encode text to Base64 or decode Base64 strings.

### 8. Password Strength Checker
Analyze password strength with:
- Length check
- Uppercase/Lowercase/Number/Special character detection
- Entropy calculation (bits)
- Overall strength rating (Weak/Moderate/Strong)

### 9. QR Code Generator
Generate QR codes from any text or URL:
- ASCII art output (default)
- PNG file export (requires `qrcode` module)

### 10. Username OSINT
Check if a username exists across 30+ platforms:
```
GitHub, Twitter/X, Instagram, Reddit, YouTube, TikTok, Facebook,
LinkedIn, Twitch, Steam, Spotify, GitLab, HackTheBox, TryHackMe,
and more...
```

### 11. Port Reference
Search a database of 150+ common ports:
- Search by port number
- Search by service name (partial match supported)

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Libraries:** `socket`, `hashlib`, `base64`, `json`, `urllib`, `subprocess`, `math`
- **External APIs:** ip-api.com, NVD API (NIST)
- **Optional:** `qrcode` (PIL)

---

## 👨‍💻 Author

**Mr Silent 313 (Nasru)**
- 🏷️ Professional Cybersecurity Engineer 
- 🎯 Ethical Hacker
- 🏢 Team [elite hackers](https://chat.whatsapp.com/BQkrsSjc9Nj1lbzvnqjEZx) << whatsapp community

<p align="center">
  <b>⭐ If you find this tool useful, please give it a star! ⭐</b>
</p>

---

## ⚖️ Disclaimer

> **IMPORTANT:** This tool is intended for **educational purposes** and **authorized security testing only**. The author assumes no liability and is not responsible for any misuse or damage caused by this program. Always obtain proper authorization before testing any system. Use responsibly and ethically.

---

## 📜 License

This project is licensed under the **Apache-2.0 License** — see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  <b>MR SILENT 313 © 2026</b>
</p>
