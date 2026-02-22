# 🚀 Quick Start Guide

## Get Your CTF Challenge Running in 15 Minutes

---

## ⚡ Fast Track Deployment

### Step 1: Generate Artifacts (2 minutes)

```bash
cd /Users/dayananda/Dayananda/MCA/HTB

# Generate image artifact
python3 artifact_alpha.py

# Generate audio artifact
python3 artifact_beta.py
```

**Expected output:**
- `defaced_grade.jpg` (~2.4 MB)
- `rogue_signal.wav` (~1-2 MB)

---

### Step 2: Verify Files (1 minute)

```bash
# Check all required files exist
ls -1 *.html *.txt *.jpg *.wav

# Should see:
# student-portal.html
# it-alert.html
# dashboard.html
# portal_backup_2025.html
# robots.txt
# system_logs.txt
# defaced_grade.jpg
# rogue_signal.wav
```

---

### Step 3: Test Locally (5 minutes)

```bash
# Option A: Use Python's built-in server
python3 -m http.server 8000

# Option B: Use file:// protocol
open student-portal.html
```

**Quick Test:**
1. Open `http://localhost:8000/student-portal.html`
2. Login with: `sysadmin` / `2.1.447`
3. Should redirect to `it-alert.html`
4. Enter vault password: `OP-GRADE-SWAP-89`
5. Should unlock artifacts

---

### Step 4: Deploy to Server (5 minutes)

```bash
# Copy all files to your web server
scp *.html *.txt *.jpg *.wav user@server:/var/www/ctf/

# Or use your preferred deployment method
```

---

### Step 5: Configure CTFd (2 minutes)

Create 3 challenges in CTFd:

**Challenge 1: Image Forensics**
- Name: "Artifact Alpha - Image Analysis"
- Category: Forensics
- Points: 200
- Flag: `HTB{psg_grade_swap}`
- Description: "Analyze the intercepted screenshot for hidden data."

**Challenge 2: Audio Analysis**
- Name: "Artifact Beta - Audio Forensics"
- Category: Forensics
- Points: 300
- Flag: `HTB{psg_sonic_exfil}`
- Description: "Analyze the rogue audio broadcast for encoded data."

**Challenge 3: Data Exfiltration**
- Name: "Dashboard Investigation"
- Category: Web
- Points: 150
- Flag: `HTB{psg_data_exfil}`
- Description: "Investigate the fulfillment dashboard logs."

---

## 🎯 Quick Reference

### Real Flags
```
HTB{psg_grade_swap}    - Image EXIF (ROT13)
HTB{psg_sonic_exfil}   - Audio spectrogram (Caesar +7)
HTB{psg_data_exfil}    - Dashboard logs (Base64)
```

### Passwords
```
Portal:  sysadmin:2.1.447
Vault:   OP-GRADE-SWAP-89
```

### URLs
```
Entry:      /student-portal.html
Incident:   /it-alert.html
Dashboard:  /dashboard.html
Robots:     /robots.txt
```

---

## 🧪 Quick Test Commands

### Test Flag 1 (Image)
```bash
exiftool defaced_grade.jpg | grep "User Comment"
# Output: UGO{cft_tenqr_fjnc}
# ROT13 decode: HTB{psg_grade_swap}
```

### Test Flag 2 (Audio)
```bash
# Open in Audacity
# View spectrogram (15-20 kHz)
# Extract: OAI{wzn_zvupj_lempss}
# Caesar -7 decode: HTB{psg_sonic_exfil}
```

### Test Flag 3 (Dashboard)
```bash
# Find in dashboard.html logs:
# TX_PACKET_ID: SFRCe3BzZ19kYXRhX2V4ZmlsfQ==

echo "SFRCe3BzZ19kYXRhX2V4ZmlsfQ==" | base64 -d
# Output: HTB{psg_data_exfil}
```

---

## 🐛 Quick Troubleshooting

### Problem: Artifacts not generating
```bash
# Install dependencies
pip3 install pillow piexif numpy
```

### Problem: Portal login not working
- Check credentials: `sysadmin:2.1.447` (case-sensitive)
- Check JavaScript is enabled
- Check browser console for errors

### Problem: Vault not unlocking
- Check password: `OP-GRADE-SWAP-89` (uppercase, with hyphens)
- No spaces before/after
- Case-sensitive

### Problem: Can't extract EXIF
```bash
# Install exiftool
brew install exiftool  # macOS
apt-get install libimage-exiftool-perl  # Linux
```

### Problem: Can't see spectrogram
- Try Audacity: `brew install --cask audacity`
- Adjust frequency range to 15-20 kHz
- Increase contrast/brightness

---

## 📋 Pre-Event Checklist

Quick checklist before going live:

- [ ] Artifacts generated (`defaced_grade.jpg`, `rogue_signal.wav`)
- [ ] All HTML files accessible
- [ ] Portal login tested (`sysadmin:2.1.447`)
- [ ] Vault unlock tested (`OP-GRADE-SWAP-89`)
- [ ] All 3 flags verified
- [ ] CTFd challenges configured
- [ ] Test solve completed
- [ ] Backup of all files created

---

## 🎓 Player Instructions

Give players this starting point:

```
🎯 CTF Challenge: University Breach Investigation

You've been called to investigate a security breach at a university.
Multiple systems have been compromised, and evidence has been collected.

Your mission:
1. Access the compromised systems
2. Analyze the collected evidence
3. Extract the flags from the artifacts

Starting URL: http://[your-server]/student-portal.html

Tools you may need:
- Web browser with DevTools
- exiftool (for image analysis)
- Audacity (for audio analysis)
- Base64 decoder

Good luck! 🏴☠️
```

---

## 📚 Documentation Quick Links

- **Full Overview:** README.md
- **Solutions:** ADMIN_GUIDE.md
- **Testing:** TESTING_CHECKLIST.md
- **Flow Diagram:** CHALLENGE_FLOW.md
- **Changes:** REFACTORING_SUMMARY.md

---

## 🆘 Need Help?

### During Setup
1. Check TESTING_CHECKLIST.md
2. Verify all files are present
3. Test each component individually

### During Event
1. Check ADMIN_GUIDE.md for solutions
2. Use hint system if configured
3. Monitor player questions

### After Event
1. Collect feedback
2. Review solve statistics
3. Update documentation if needed

---

## ⚡ One-Command Deploy (Advanced)

If you have a configured server:

```bash
#!/bin/bash
# deploy.sh - Quick deployment script

# Generate artifacts
python3 artifact_alpha.py
python3 artifact_beta.py

# Deploy to server
rsync -avz --exclude '*.py' --exclude '*.md' \
  *.html *.txt *.jpg *.wav \
  user@server:/var/www/ctf/

echo "✅ Deployment complete!"
echo "🌐 Access at: http://your-server/student-portal.html"
```

---

## 🎉 You're Ready!

Your CTF challenge is now deployed and ready for players!

**Next Steps:**
1. ✅ Test the complete solve path
2. ✅ Brief your support team
3. ✅ Announce the challenge to players
4. ✅ Monitor for issues
5. ✅ Have fun! 🎯

---

**Deployment Time:** ~15 minutes  
**Difficulty:** Medium  
**Expected Solve Time:** 75-105 minutes  
**Recommended Points:** 900 total  

**Good luck with your CTF event! 🏴☠️🚀**
