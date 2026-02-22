# 🔑 CTF Challenge - Quick Reference Guide

## For Challenge Administrators Only

---

## 🚩 REAL FLAGS (Submit These)

| # | Flag | Location | Method |
|---|------|----------|--------|
| 1 | `HTB{psg_grade_swap}` | defaced_grade.jpg | EXIF UserComment → ROT13 decode |
| 2 | `HTB{psg_sonic_exfil}` | rogue_signal.wav | Spectrogram → Caesar -7 decode |
| 3 | `HTB{psg_data_exfil}` | dashboard.html | TX_PACKET_ID in logs → Base64 decode |

---

## 🔐 PASSWORDS & CREDENTIALS

### Portal Login (student-portal.html → it-alert.html)
- **Username:** `sysadmin`
- **Password:** `2.1.447`
- **How to find:**
  - Meta tag: `<meta name="auth-version" content="2.1.4">`
  - Subtitle text: `Node: 192.168.10.47`
  - Must extract version (2.1.4) and last octet (47)
  - Combine: 2.1.4 + 47 = 2.1.447
  - **NO HASH COMPARISON** - Pure DOM-based logic
  - **NO EXPLICIT FORMAT** - Must deduce from elements

**Interactive Hints:**
- Focus on username field → System info hint
- Focus on password field → Metadata hint
- Triple-click on title → Debug info
- Hover on build info → Analysis hint
- Ctrl+Shift+D → System information
- Double-click logo → Network info

### Evidence Vault (it-alert.html)
- **Password:** `OP-GRADE-SWAP-89`
- **How to find:**
  - OP = Operation type (inferred from incident context)
  - GRADE = Target (from incident summary: "grade alterations")
  - SWAP = Method (from forensic notes: mentions "swap")
  - 89 = Workstation (from network logs table: 192.168.10.89)
  - **NO HASH COMPARISON** - Pure DOM parsing logic
  - **NO EXPLICIT FORMAT** - Must correlate information

**Interactive Hints:**
- Focus on password field → Vault analysis hint
- Hover on network logs → IP address tip
- Click on incident summary → Forensic analysis
- Ctrl+Shift+V → Vault analysis
- Right-click on vault form → Component hint

---

## 🎭 DECOY FLAGS (Wrong - Don't Submit)

1. `HTB{psg_fake_portal}` - student-portal.html (HTML comment)
2. `HTB{psg_admin_panel}` - student-portal.html (JS config)
3. `HTB{psg_test_mode}` - student-portal.html (JS variable)
4. `HTB{psg_debug_access}` - student-portal.html (test creds)
5. `HTB{psg_incident_report}` - it-alert.html (HTML comment)
6. `HTB{psg_forensic_vault}` - it-alert.html (HTML comment)
7. `HTB{psg_evidence_access}` - it-alert.html (JS config)
8. `HTB{psg_warehouse_logs}` - dashboard.html (HTML comment)
9. `HTB{psg_api_endpoint}` - dashboard.html (JS config)
10. `HTB{psg_config_leak}` - dashboard.html (JS config)
11. `HTB{psg_robots_file}` - robots.txt
12. `HTB{psg_old_backup}` - portal_backup_2025.html
13. `HTB{psg_legacy_auth}` - portal_backup_2025.html
14. `HTB{psg_backup_creds}` - portal_backup_2025.html
15. `HTB{psg_system_logs}` - system_logs.txt
16. `HTB{psg_log_analysis}` - system_logs.txt

---

## 📝 SOLUTION WALKTHROUGH

### Step 1: Portal Access
1. Open `student-portal.html`
2. View page source or inspect element
3. Find meta tag: `<meta name="auth-version" content="2.1.4">`
4. Find subtitle: `Node: 192.168.10.47`
5. Check console for hint about format
6. Optionally check `robots.txt` for example
7. Construct password: `2.1.4` + `47` = `2.1.447`
8. Login with `sysadmin:2.1.447`
9. Redirected to `it-alert.html`

### Step 2: Evidence Vault
1. Read incident report carefully
2. Note "grade alterations" in summary (TARGET = GRADE)
3. Check network activity log table
4. Find suspicious IP: 192.168.10.89 (WORKSTATION = 89)
5. Note "grade swap" in forensic notes (METHOD = SWAP)
6. Understand operation context (OPERATION = OP)
7. Construct password: `OP-GRADE-SWAP-89`
8. Enter in vault form
9. Artifacts unlocked for download

### Step 3: Image Forensics
1. Download `defaced_grade.jpg`
2. Extract EXIF metadata:
   ```bash
   exiftool defaced_grade.jpg | grep "User Comment"
   ```
3. Find: `UGO{cft_tenqr_fjnc}`
4. Recognize ROT13 encoding
5. Decode: `HTB{psg_grade_swap}`
6. Submit flag ✅

### Step 4: Audio Analysis
1. Download `rogue_signal.wav`
2. Open in Audacity or Sonic Visualiser
3. View spectrogram (Analyze → Plot Spectrum)
4. Look in 15-20 kHz frequency range
5. See encoded text: `OAI{wzn_zvupj_lempss}`
6. Recognize Caesar cipher (shift +7)
7. Decode: `HTB{psg_sonic_exfil}`
8. Submit flag ✅

### Step 5: Dashboard Investigation
1. Open `dashboard.html`
2. Scroll to "Transmission Logs" section
3. Find log entry with TX_PACKET_ID
4. Extract: `SFRCe3BzZ19kYXRhX2V4ZmlsfQ==`
5. Recognize Base64 encoding
6. Decode:
   ```bash
   echo "SFRCe3BzZ19kYXRhX2V4ZmlsfQ==" | base64 -d
   ```
7. Result: `HTB{psg_data_exfil}`
8. Submit flag ✅

---

## 🛠️ REQUIRED TOOLS

### Essential
- Web browser with DevTools
- Text editor
- Base64 decoder (online or CLI)
- ROT13/Caesar cipher decoder (online or CLI)

### For Artifacts
- `exiftool` (for EXIF extraction)
  ```bash
  # Install on macOS
  brew install exiftool
  
  # Install on Linux
  apt-get install libimage-exiftool-perl
  ```

- Audacity or Sonic Visualiser (for spectrogram)
  ```bash
  # Install Audacity on macOS
  brew install --cask audacity
  ```

### Optional
- Python with PIL/piexif (to regenerate artifacts)
- CyberChef (for encoding/decoding)
- Burp Suite (for web analysis)

---

## 🔄 REGENERATE ARTIFACTS

If you need to regenerate the artifact files:

```bash
# Generate image with EXIF flag
python3 artifact_alpha.py

# Generate audio with spectrogram flag
python3 artifact_beta.py
```

**Note:** Requires Python 3 with PIL/piexif and numpy

---

## 💡 HINTS (If Players Get Stuck)

### Hint 1 - Portal Access (50 points penalty)
"The password isn't stored anywhere. Look at the page structure - what information is displayed about the system? Try interacting with different elements. Keyboard shortcuts might help (try Ctrl+Shift+D)."

### Hint 2 - Vault Password (75 points penalty)
"The vault password isn't stored anywhere - you must construct it from the incident report. Read everything carefully: the incident summary, network logs table, and forensic notes. Try Ctrl+Shift+V for analysis help."

### Hint 3 - Image Flag (25 points penalty)
"EXIF metadata can hide information in images. Use exiftool to extract all metadata and look for the UserComment field. The flag is encoded with ROT13."

### Hint 4 - Audio Flag (50 points penalty)
"Open the audio file in a spectrogram viewer like Audacity. Look in the high frequency range (15-20 kHz). The visible text is Caesar cipher encoded."

### Hint 5 - Dashboard Flag (25 points penalty)
"One of the log entries in the Transmission Logs section contains a TX_PACKET_ID. That string is Base64 encoded."

---

## 📊 SCORING RECOMMENDATION

| Challenge | Points | Difficulty |
|-----------|--------|------------|
| Portal Access | 100 | Easy-Medium |
| Evidence Vault | 150 | Medium |
| Image Forensics | 200 | Medium |
| Audio Analysis | 300 | Medium-Hard |
| Dashboard Flag | 150 | Easy-Medium |
| **TOTAL** | **900** | **Medium** |

---

## ⏱️ EXPECTED SOLVE TIMES

- **Speed run (experienced):** 20-30 minutes
- **Average player:** 1-2 hours
- **Beginner:** 2-4 hours
- **With hints:** 45-90 minutes

---

## 🐛 TROUBLESHOOTING

### Players can't login to portal
- Check they're using `sysadmin` not `admin`
- Verify password is `2.1.447` (no spaces)
- Ensure JavaScript is enabled

### Vault won't unlock
- Password is case-sensitive: `OP-GRADE-SWAP-89`
- Must be exact format with hyphens
- No spaces before/after

### Can't extract EXIF
- Ensure they have exiftool installed
- Try: `exiftool -UserComment defaced_grade.jpg`
- Alternative: Use online EXIF viewer

### Can't see spectrogram
- Ensure audio file downloaded completely
- Try different spectrogram tool
- Adjust frequency range to 15-20 kHz
- Increase contrast/brightness

### Base64 won't decode
- Ensure they copied the full string
- Check for extra spaces or line breaks
- Try online decoder if CLI fails

---

## 📞 SUPPORT CONTACTS

For technical issues during the event:
- Event organizer: [Your contact]
- Technical support: [Your contact]
- CTFd platform: [Platform URL]

---

## ✅ PRE-EVENT CHECKLIST

- [ ] All HTML files deployed and accessible
- [ ] Artifacts (JPG, WAV) generated and available for download
- [ ] CTFd configured with 3 flag challenges
- [ ] Flags tested and verified
- [ ] Hint system configured (optional)
- [ ] Scoring values set
- [ ] Time limits set (if any)
- [ ] Backup of all files created
- [ ] Test solve completed successfully
- [ ] Support team briefed

---

**Good luck with your CTF event! 🎯**
