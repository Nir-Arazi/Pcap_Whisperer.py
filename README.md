# 🦈 Pcap_Whisperer

A lightweight Python-based PCAP analysis tool that runs Snort signature detection against `.pcap` / `.pcapng` files and delivers a clear malicious/clean verdict — straight from your terminal.

---

## 🔍 What It Does

Point it at a capture file. It whispers back what's hiding inside.

Pcap_Whisperer automates the full pipeline:
1. **Downloads** a custom Snort ruleset from GitHub (once, on first run)
2. **Installs Snort** automatically if it's not already present
3. **Runs Snort** against your pcap in fast-alert mode
4. **Parses and deduplicates** the output — no noise, just unique hits
5. **Prints a verdict** — clean or malicious, with color-coded results

---

## ⚙️ Requirements

- Linux (tested on Kali)
- Python 3
- `sudo` privileges (required for Snort)
- Internet access on first run (to pull the rules)

---

## 🚀 Usage

```bash
sudo python Pcap_Whisperer.py <file.pcap>
```

**Example:**
```bash
sudo python Pcap_Whisperer.py week6.pcap
```

---

## 📤 Output Examples

**Clean file:**
```
No rules were triggered for this pcap file!
```

**Malicious file:**
```
Malicious activity was detected.
-------------------------------------------------------------------------------
 "MALWARE Cobalt Strike DNS Beacon Alt Port" [**] [Priority 0] {TCP} 172.16.2.201 → 172.16.2.4
 "DNS TUNNEL Base64 Encoded Subdomain" [**] [Priority 0] {UDP} 172.16.2.4 → 8.8.8.8
 "LATERAL MOVEMENT Admin Share C$" [**] [Priority 0] {TCP} 172.16.2.201 → 172.16.2.4
 "CREDENTIAL THEFT SYSTEM Hive Access via SMB" [**] [Priority 0] {TCP} 172.16.2.201 → 172.16.2.4
 ...
-------------------------------------------------------------------------------
```

Each alert shows:
- Rule name and category
- Priority level
- Protocol (TCP/UDP)
- Source → Destination IP

---

## 📁 How It Works

```
Pcap_Whisperer.py
│
├── Checks if Snort is installed → installs if missing
├── Checks if local.rules exists → downloads from GitHub if missing
├── Runs: snort -c snort.lua -R local.rules -r <file> -A fast -q
├── Pipes output through awk + sed + sort for clean deduplication
└── Prints color-coded verdict to terminal
```

---

## 📜 Rules

The tool pulls its detection rules from:
👉 [github.com/Nir-Arazi/Snort_Rules](https://github.com/Nir-Arazi/Snort_Rules)

Rules cover threats including:
- Malware / C2 beaconing (Cobalt Strike, etc.)
- DNS tunneling
- Lateral movement (SMB, IPC$, svcctl)
- Credential theft
- Reconnaissance (SYN sweeps, LDAP enumeration)
- Web attacks (LFI, RFI, SQLi, SSRF, Path Traversal)
- Log4J exploitation
- File exfiltration

---

## 👤 Author

**Nir Arazi** — SOC Analyst | Threat Detection  
[GitHub](https://github.com/Nir-Arazi)
