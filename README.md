# 🎯 CTF Challenge: University Breach Investigation

## Overview
This is a fully static HTML/CSS/JS CTF challenge simulating a university system breach investigation. Players must investigate multiple artifacts, decode hidden messages, and piece together clues to find the real flags.

## Challenge Structure

### Entry Points
1. **student-portal.html** - Login portal (requires credential discovery)
2. **dashboard.html** - Fulfillment center dashboard (contains encoded flag)
3. **it-alert.html** - Incident report (requires vault password)

### Challenge Flow
```
student-portal.html 
    ↓ (discover credentials from page metadata)
it-alert.html 
    ↓ (construct vault password from incident details)
Download artifacts (defaced_grade.jpg, rogue_signal.wav)
    ↓ (analyze EXIF metadata and audio spectrogram)
Decode Caesar ciphers
    ↓
Submit flags
```

## 🚩 Real Flags (HTB{psg_xxxx} format)

### Flag 1: Portal Access
- **Location**: `student-portal.html`
- **Method**: Discover credentials from page metadata
- **Credentials**: `sysadmin:2.1.447`
  - Derived from: Build version (2.1.4) + Node IP last octet (47)
  - Hint in console: "Emergency override format: sysadmin:[BUILD_VERSION][NODE_IP_LAST_OCTET]"
  - Meta tags contain: `auth-version="2.1.4"` and subtitle shows `Node: 192.168.10.47`
- **Flag**: Access to next stage (no flag submission here)

### Flag 2: Evidence Vault
- **Location**: `it-alert.html`
- **Method**: Construct vault password from incident details
- **Password**: `OP-GRADE-SWAP-89`
  - OP = Operation (mentioned in incident)
  - GRADE = Target (grade database)
  - SWAP = Method (grade swap attack)
  - 89 = Workstation number (from network logs: 192.168.10.89)
- **Flag**: Access to download artifacts (no flag submission here)

### Flag 3: Image Metadata
- **Location**: `defaced_grade.jpg` (EXIF UserComment)
- **Method**: Extract EXIF metadata and decode ROT13
- **Encoded**: `UGO{cft_tenqr_fjnc}`
- **Real Flag**: `HTB{psg_grade_swap}`
- **Commands**:
  ```bash
  exiftool defaced_grade.jpg | grep "User Comment"
  # Apply ROT13 decoding
  ```

### Flag 4: Audio Spectrogram
- **Location**: `rogue_signal.wav` (spectrogram analysis)
- **Method**: Analyze audio spectrogram to extract encoded text
- **Encoded**: `OAI{wzn_zvupj_lempss}` (Caesar +7)
- **Real Flag**: `HTB{psg_sonic_exfil}`
- **Tools**: Audacity, Sonic Visualiser, or Python scipy
- **Steps**:
  1. Open audio in spectrogram viewer
  2. Look for frequency patterns in 15-20 kHz range
  3. Extract visible text
  4. Apply Caesar -7 decoding

### Flag 5: Dashboard Logs
- **Location**: `dashboard.html` (transmission logs)
- **Method**: Find base64 encoded string in logs and decode
- **Encoded**: `SFRCe3BzZ19kYXRhX2V4ZmlsfQ==`
- **Real Flag**: `HTB{psg_data_exfil}`
- **Command**:
  ```bash
  echo "SFRCe3BzZ19kYXRhX2V4ZmlsfQ==" | base64 -d
  ```

## 🎭 Decoy Flags (Intentionally Wrong)

These flags are scattered throughout to mislead players:

1. `HTB{psg_fake_portal}` - In student-portal.html HTML comment
2. `HTB{psg_admin_panel}` - In student-portal.html JS config
3. `HTB{psg_test_mode}` - In student-portal.html JS variable
4. `HTB{psg_debug_access}` - In student-portal.html test credentials
5. `HTB{psg_incident_report}` - In it-alert.html HTML comment
6. `HTB{psg_forensic_vault}` - In it-alert.html HTML comment
7. `HTB{psg_evidence_access}` - In it-alert.html JS config
8. `HTB{psg_warehouse_logs}` - In dashboard.html HTML comment
9. `HTB{psg_api_endpoint}` - In dashboard.html JS config
10. `HTB{psg_config_leak}` - In dashboard.html JS config
11. `HTB{psg_robots_file}` - In robots.txt
12. `HTB{psg_old_backup}` - In portal_backup_2025.html
13. `HTB{psg_legacy_auth}` - In portal_backup_2025.html
14. `HTB{psg_backup_creds}` - In portal_backup_2025.html
15. `HTB{psg_system_logs}` - In system_logs.txt
16. `HTB{psg_log_analysis}` - In system_logs.txt

## 📁 File Structure

```
HTB/
├── student-portal.html          # Entry point - login portal
├── it-alert.html                # Incident report with evidence vault
├── dashboard.html               # Fulfillment dashboard with encoded flag
├── defaced_grade.jpg            # Artifact with EXIF flag
├── rogue_signal.wav             # Artifact with spectrogram flag
├── robots.txt                   # Contains hints and decoys
├── portal_backup_2025.html      # Old backup with decoy flags
├── system_logs.txt              # System logs with hints
├── artifact_alpha.py            # Generator for defaced_grade.jpg
├── artifact_beta.py             # Generator for rogue_signal.wav
└── README.md                    # This file

```

## 🔧 Setup Instructions

### Generate Artifacts
```bash
# Generate the image artifact with EXIF flag
python3 artifact_alpha.py

# Generate the audio artifact with spectrogram flag
python3 artifact_beta.py
```

### Deploy to CTFd
1. Host all HTML files on a web server (or use file:// protocol for local testing)
2. Ensure artifacts (JPG, WAV) are accessible for download
3. Configure CTFd with 5 flag challenges:
   - Challenge 1: "Portal Access" (no flag, just progression)
   - Challenge 2: "Evidence Vault" (no flag, just progression)
   - Challenge 3: "Image Forensics" → `HTB{psg_grade_swap}`
   - Challenge 4: "Audio Analysis" → `HTB{psg_sonic_exfil}`
   - Challenge 5: "Data Exfiltration" → `HTB{psg_data_exfil}`

## 🎓 Learning Objectives

Players will learn:
- Web application reconnaissance
- HTML/JS source code analysis
- Metadata extraction (robots.txt, HTML meta tags)
- EXIF metadata analysis
- Audio spectrogram analysis
- Caesar cipher / ROT13 decoding
- Base64 encoding/decoding
- Clue correlation and logical deduction
- Distinguishing real evidence from decoys

## 🛠️ Tools Needed

- Web browser with Developer Tools
- `exiftool` or Python PIL for EXIF extraction
- Audacity or Sonic Visualiser for audio analysis
- Base64 decoder (command line or online)
- ROT13/Caesar cipher decoder
- Text editor for source code review

## 🔐 Security Notes

- All authentication is client-side (intentionally weak for CTF purposes)
- No actual backend or database
- All flags are embedded in static files
- Passwords are obfuscated but not truly secure
- This is for educational purposes only

## 📝 Hints System (Optional)

If players get stuck, provide progressive hints:

### Hint 1 (Portal Access)
"Check the page metadata and system information. The password format is mentioned in the console."

### Hint 2 (Vault Password)
"The vault password has 4 components. Look at the incident report details and network activity logs."

### Hint 3 (Image Flag)
"EXIF metadata can contain hidden information. Try exiftool and look for the UserComment field."

### Hint 4 (Audio Flag)
"Open the audio file in a spectrogram viewer. Look in the ultrasonic frequency range (15-20 kHz)."

### Hint 5 (Dashboard Flag)
"Check the transmission logs carefully. One log entry contains a base64 encoded string."

## 🎯 Difficulty Level

**Medium** - Requires:
- Basic web reconnaissance skills
- Understanding of metadata
- Familiarity with encoding schemes
- Audio/image forensics knowledge
- Logical thinking to connect clues

## 📊 Expected Solve Time

- Fast players: 30-45 minutes
- Average players: 1-2 hours
- Beginners: 2-4 hours

## 🏆 Scoring Suggestion

- Portal Access: 50 points (progression)
- Evidence Vault: 100 points (progression)
- Image Forensics: 200 points
- Audio Analysis: 300 points
- Data Exfiltration: 150 points
- **Total**: 800 points

---

**Created for educational cybersecurity training**
**All flags follow format: HTB{psg_xxxx}**
