# ✅ CTF Challenge Testing Checklist

## Pre-Deployment Testing

Use this checklist to verify everything works correctly before deploying to players.

---

## 🔧 SETUP VERIFICATION

### File Generation
- [ ] Run `python3 artifact_alpha.py` successfully
- [ ] Verify `defaced_grade.jpg` created (should be ~2.4 MB)
- [ ] Run `python3 artifact_beta.py` successfully
- [ ] Verify `rogue_signal.wav` created (should be ~4.5 seconds)
- [ ] Check all HTML files are present
- [ ] Check all documentation files are present

### File Integrity
- [ ] All HTML files open without errors
- [ ] No broken links between pages
- [ ] All CSS loads correctly
- [ ] All JavaScript executes without console errors
- [ ] Images display correctly
- [ ] Audio file plays correctly

---

## 🚩 FLAG VERIFICATION

### Real Flags (Must Work)

#### Flag 1: Image EXIF
- [ ] Extract EXIF from `defaced_grade.jpg`:
  ```bash
  exiftool defaced_grade.jpg | grep "User Comment"
  ```
- [ ] Verify output: `UGO{cft_tenqr_fjnc}`
- [ ] Decode ROT13: `HTB{psg_grade_swap}`
- [ ] Confirm flag format is correct

#### Flag 2: Audio Spectrogram
- [ ] Open `rogue_signal.wav` in Audacity
- [ ] View spectrogram (Analyze → Plot Spectrum)
- [ ] Verify visible text in 15-20 kHz range
- [ ] Extract: `OAI{wzn_zvupj_lempss}`
- [ ] Decode Caesar -7: `HTB{psg_sonic_exfil}`
- [ ] Confirm flag format is correct

#### Flag 3: Dashboard Logs
- [ ] Open `dashboard.html`
- [ ] Find TX_PACKET_ID in logs
- [ ] Extract: `SFRCe3BzZ19kYXRhX2V4ZmlsfQ==`
- [ ] Decode Base64:
  ```bash
  echo "SFRCe3BzZ19kYXRhX2V4ZmlsfQ==" | base64 -d
  ```
- [ ] Verify output: `HTB{psg_data_exfil}`
- [ ] Confirm flag format is correct

### Decoy Flags (Must NOT Work)
- [ ] Verify all 16 decoy flags are present
- [ ] Confirm decoy flags follow format but are marked as wrong
- [ ] Test that decoys don't accidentally match real flags

---

## 🔐 AUTHENTICATION TESTING

### Portal Login (student-portal.html)

#### Correct Credentials
- [ ] Open `student-portal.html`
- [ ] Enter username: `sysadmin`
- [ ] Enter password: `2.1.447`
- [ ] Click "Sign In"
- [ ] Verify redirect to `it-alert.html`
- [ ] Verify no error message appears

#### Incorrect Credentials
- [ ] Try username: `admin`, password: `override` (old credentials)
- [ ] Verify error message appears
- [ ] Verify no redirect occurs
- [ ] Try username: `admin`, password: `2.1.447`
- [ ] Verify error message appears
- [ ] Try username: `sysadmin`, password: `wrong`
- [ ] Verify error message appears

#### Clue Verification
- [ ] Verify meta tag shows: `auth-version="2.1.4"`
- [ ] Verify subtitle shows: `Node: 192.168.10.47`
- [ ] Open browser console
- [ ] Verify hint message appears about format
- [ ] Check `robots.txt` for example format

### Evidence Vault (it-alert.html)

#### Correct Password
- [ ] Open `it-alert.html` (after portal login)
- [ ] Enter vault password: `OP-GRADE-SWAP-89`
- [ ] Click "Decrypt"
- [ ] Verify vault form disappears
- [ ] Verify artifact cards appear
- [ ] Verify download links work

#### Incorrect Password
- [ ] Try password: `OP-GRADE-SWAP-99` (wrong workstation)
- [ ] Verify error message appears
- [ ] Verify vault remains locked
- [ ] Try password: `op-grade-swap-89` (lowercase)
- [ ] Verify error message appears
- [ ] Try password: `OP-GRADE-SWAP` (missing component)
- [ ] Verify error message appears

#### Clue Verification
- [ ] Verify incident summary mentions "grade alterations"
- [ ] Verify network logs show IP 192.168.10.89
- [ ] Verify forensic notes mention "grade swap"
- [ ] Verify vault form shows format hint
- [ ] Check `system_logs.txt` for example

---

## 🎨 UI/UX TESTING

### Visual Appearance
- [ ] All pages render correctly on desktop
- [ ] All pages render correctly on mobile
- [ ] Colors and styling are consistent
- [ ] Text is readable (contrast, size)
- [ ] Buttons are clickable and responsive
- [ ] Forms are properly aligned
- [ ] Tables display correctly
- [ ] Animations work smoothly

### Interactive Elements
- [ ] Login form accepts input
- [ ] Password fields hide text
- [ ] Submit buttons trigger actions
- [ ] Error messages display correctly
- [ ] Error messages auto-hide after 3 seconds
- [ ] Hover effects work on cards
- [ ] Tooltips appear on hover (where applicable)
- [ ] Download links work

### Browser Compatibility
- [ ] Test in Chrome/Chromium
- [ ] Test in Firefox
- [ ] Test in Safari
- [ ] Test in Edge
- [ ] Verify JavaScript works in all browsers
- [ ] Verify CSS renders correctly in all browsers

---

## 📝 CONTENT VERIFICATION

### Text Accuracy
- [ ] No spelling errors in HTML
- [ ] No grammar errors in descriptions
- [ ] Timestamps are consistent
- [ ] IP addresses are consistent
- [ ] System names are consistent
- [ ] All technical details are realistic

### Clue Consistency
- [ ] Portal password clues match solution
- [ ] Vault password clues match solution
- [ ] All hints point to correct answers
- [ ] No contradictory information
- [ ] Decoy flags are clearly wrong (to admin)

### Documentation
- [ ] README.md is complete and accurate
- [ ] ADMIN_GUIDE.md has correct solutions
- [ ] REFACTORING_SUMMARY.md explains changes
- [ ] CHALLENGE_FLOW.md shows correct path
- [ ] All documentation is up-to-date

---

## 🔍 SECURITY TESTING

### Client-Side Security
- [ ] No real passwords in plaintext
- [ ] Hashes are used for comparison
- [ ] No sensitive data in comments (except intentional clues)
- [ ] Console logs don't reveal solutions
- [ ] Source code doesn't make challenge trivial

### Decoy Effectiveness
- [ ] Decoy flags look realistic
- [ ] Decoys are scattered throughout
- [ ] Decoys don't accidentally work
- [ ] Players must validate flags
- [ ] Simple grep won't reveal real flags easily

---

## 🛠️ TOOL TESTING

### EXIF Extraction
- [ ] Test with exiftool:
  ```bash
  exiftool defaced_grade.jpg
  ```
- [ ] Test with online EXIF viewer
- [ ] Test with Python PIL:
  ```python
  from PIL import Image
  import piexif
  exif = piexif.load('defaced_grade.jpg')
  print(exif['Exif'][piexif.ExifIFD.UserComment])
  ```

### Audio Analysis
- [ ] Test with Audacity (spectrogram view)
- [ ] Test with Sonic Visualiser
- [ ] Test with Python scipy:
  ```python
  import scipy.io.wavfile as wav
  import matplotlib.pyplot as plt
  rate, data = wav.read('rogue_signal.wav')
  plt.specgram(data, Fs=rate)
  plt.show()
  ```

### Encoding/Decoding
- [ ] Test ROT13 decoder (online or CLI)
- [ ] Test Caesar cipher decoder (shift -7)
- [ ] Test Base64 decoder:
  ```bash
  echo "SFRCe3BzZ19kYXRhX2V4ZmlsfQ==" | base64 -d
  ```

---

## 🎯 CHALLENGE FLOW TESTING

### Complete Walkthrough
- [ ] Start from `student-portal.html`
- [ ] Discover portal credentials
- [ ] Login successfully
- [ ] Read incident report
- [ ] Discover vault password
- [ ] Unlock evidence vault
- [ ] Download both artifacts
- [ ] Extract flag from image
- [ ] Extract flag from audio
- [ ] Find flag in dashboard
- [ ] Verify all 3 flags are correct
- [ ] Time the complete walkthrough

### Alternative Paths
- [ ] Test starting from `dashboard.html`
- [ ] Test finding dashboard flag first
- [ ] Test accessing `it-alert.html` directly (should work)
- [ ] Verify all paths lead to same flags

---

## 📊 PERFORMANCE TESTING

### Load Times
- [ ] HTML pages load in < 2 seconds
- [ ] Images load in < 3 seconds
- [ ] Audio file downloads in < 10 seconds
- [ ] JavaScript executes without lag
- [ ] No memory leaks in browser

### File Sizes
- [ ] HTML files are reasonable size (< 100 KB each)
- [ ] Image file is ~2-3 MB
- [ ] Audio file is ~1-2 MB
- [ ] Total challenge size is < 10 MB

---

## 🐛 ERROR HANDLING

### Edge Cases
- [ ] Test empty username/password
- [ ] Test very long username/password
- [ ] Test special characters in input
- [ ] Test SQL injection attempts (should be safe - no backend)
- [ ] Test XSS attempts (should be safe)
- [ ] Test direct URL access to all pages

### Error Messages
- [ ] Login error message is clear
- [ ] Vault error message is clear
- [ ] No JavaScript errors in console
- [ ] No 404 errors for resources
- [ ] No broken images or links

---

## 📱 ACCESSIBILITY TESTING

### Screen Readers
- [ ] Test with screen reader (NVDA, JAWS, or VoiceOver)
- [ ] Verify form labels are readable
- [ ] Verify buttons are announced correctly
- [ ] Verify error messages are announced

### Keyboard Navigation
- [ ] Tab through all interactive elements
- [ ] Enter key submits forms
- [ ] Escape key closes modals (if any)
- [ ] Focus indicators are visible

---

## 🎓 EDUCATIONAL VALUE

### Learning Objectives
- [ ] Challenge teaches web reconnaissance
- [ ] Challenge teaches metadata analysis
- [ ] Challenge teaches encoding/decoding
- [ ] Challenge teaches forensic analysis
- [ ] Challenge teaches critical thinking
- [ ] Difficulty is appropriate for target audience

### Hint System (Optional)
- [ ] Hints are helpful but not spoilers
- [ ] Hints are progressive (easy → hard)
- [ ] Hint penalties are fair
- [ ] Hints don't reveal full solution

---

## 📋 DEPLOYMENT CHECKLIST

### Pre-Deployment
- [ ] All tests above passed
- [ ] Backup of all files created
- [ ] Documentation reviewed
- [ ] Solutions verified
- [ ] Scoring configured in CTFd
- [ ] Time limits set (if any)

### Deployment
- [ ] Files uploaded to web server
- [ ] URLs are accessible
- [ ] Download links work
- [ ] CTFd challenges created
- [ ] Flags configured in CTFd
- [ ] Test submission works

### Post-Deployment
- [ ] Test complete solve from player perspective
- [ ] Verify all flags submit correctly
- [ ] Check CTFd scoreboard updates
- [ ] Monitor for issues
- [ ] Support team ready

---

## 🔄 REGRESSION TESTING

If you make any changes, re-test:
- [ ] All authentication still works
- [ ] All flags still extract correctly
- [ ] All clues still point to correct solutions
- [ ] No new bugs introduced
- [ ] Documentation updated

---

## ✅ FINAL SIGN-OFF

- [ ] All tests passed
- [ ] No critical issues found
- [ ] Documentation complete
- [ ] Ready for deployment
- [ ] Support team briefed
- [ ] Backup plan in place

**Tested by:** ___________________  
**Date:** ___________________  
**Approved by:** ___________________  
**Date:** ___________________  

---

## 🆘 TROUBLESHOOTING GUIDE

### Common Issues

**Issue:** Portal login doesn't work
- **Check:** JavaScript enabled?
- **Check:** Correct credentials? (sysadmin:2.1.447)
- **Check:** Browser console for errors?

**Issue:** Vault won't unlock
- **Check:** Correct password? (OP-GRADE-SWAP-89)
- **Check:** Case-sensitive? (must be uppercase)
- **Check:** No extra spaces?

**Issue:** Can't extract EXIF
- **Check:** exiftool installed?
- **Check:** File downloaded completely?
- **Check:** Try online EXIF viewer?

**Issue:** Can't see spectrogram
- **Check:** Audio file downloaded completely?
- **Check:** Correct frequency range? (15-20 kHz)
- **Check:** Try different tool?

**Issue:** Base64 won't decode
- **Check:** Full string copied?
- **Check:** No extra spaces or line breaks?
- **Check:** Try online decoder?

---

**Testing complete! Challenge ready for deployment! 🚀**
