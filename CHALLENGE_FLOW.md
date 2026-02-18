# 🗺️ CTF Challenge Flow Diagram

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         CHALLENGE START                                  │
│                    Player receives challenge URL                         │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                      STAGE 1: RECONNAISSANCE                             │
│                                                                          │
│  Files to explore:                                                       │
│  • student-portal.html (main entry point)                               │
│  • dashboard.html (alternative entry)                                   │
│  • robots.txt (hints and file discovery)                                │
│  • portal_backup_2025.html (decoy flags)                                │
│  • system_logs.txt (hints and context)                                  │
│                                                                          │
│  Actions:                                                                │
│  ✓ View page source                                                     │
│  ✓ Inspect HTML meta tags                                               │
│  ✓ Check browser console                                                │
│  ✓ Read robots.txt                                                      │
│  ✓ Explore backup files                                                 │
│                                                                          │
│  Decoy flags encountered: 6-8 fake flags                                │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                   STAGE 2: PORTAL ACCESS                                 │
│                     (student-portal.html)                                │
│                                                                          │
│  Objective: Discover login credentials                                  │
│                                                                          │
│  Clues to find:                                                          │
│  1. Meta tag: auth-version="2.1.4"                                      │
│  2. Subtitle: "Node: 192.168.10.47"                                     │
│  3. Console hint: Format explanation                                    │
│  4. robots.txt: Example format                                          │
│                                                                          │
│  Solution:                                                               │
│  Username: sysadmin                                                      │
│  Password: 2.1.447 (from version 2.1.4 + node IP last octet 47)        │
│                                                                          │
│  Decoy flags: 4 fake flags in source                                    │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    │ Login successful
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                   STAGE 3: INCIDENT INVESTIGATION                        │
│                        (it-alert.html)                                   │
│                                                                          │
│  Objective: Unlock evidence vault                                       │
│                                                                          │
│  Information to gather:                                                  │
│  • Incident summary: "grade alterations" → TARGET = GRADE               │
│  • Network logs: IP 192.168.10.89 → WORKSTATION = 89                   │
│  • Forensic notes: "grade swap" → METHOD = SWAP                         │
│  • Context: Operation type → OPERATION = OP                             │
│  • Vault form: Format hint displayed                                    │
│                                                                          │
│  Solution:                                                               │
│  Vault password: OP-GRADE-SWAP-89                                       │
│                                                                          │
│  Decoy flags: 3 fake flags in source                                    │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    │ Vault unlocked
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                   STAGE 4: ARTIFACT ANALYSIS                             │
│                                                                          │
│  Two artifacts available for download:                                  │
│  1. defaced_grade.jpg                                                   │
│  2. rogue_signal.wav                                                    │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    ▼                               ▼
┌──────────────────────────────┐    ┌──────────────────────────────┐
│   ARTIFACT ALPHA (Image)     │    │   ARTIFACT BETA (Audio)      │
│   defaced_grade.jpg          │    │   rogue_signal.wav           │
│                              │    │                              │
│  Tool: exiftool              │    │  Tool: Audacity/Sonic Vis    │
│                              │    │                              │
│  Command:                    │    │  Steps:                      │
│  exiftool defaced_grade.jpg  │    │  1. Open in spectrogram      │
│  | grep "User Comment"       │    │  2. View 15-20 kHz range     │
│                              │    │  3. Extract visible text     │
│  Result:                     │    │                              │
│  UGO{cft_tenqr_fjnc}         │    │  Result:                     │
│                              │    │  OAI{wzn_zvupj_lempss}       │
│  Encoding: ROT13             │    │                              │
│                              │    │  Encoding: Caesar +7         │
│  Decode:                     │    │                              │
│  HTB{psg_grade_swap}         │    │  Decode:                     │
│                              │    │  HTB{psg_sonic_exfil}        │
│  ✅ FLAG 1                   │    │  ✅ FLAG 2                   │
└──────────────────────────────┘    └──────────────────────────────┘
                    │                               │
                    └───────────────┬───────────────┘
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                   STAGE 5: DASHBOARD ANALYSIS                            │
│                       (dashboard.html)                                   │
│                                                                          │
│  Objective: Find hidden flag in logs                                    │
│                                                                          │
│  Location: Transmission Logs section                                    │
│                                                                          │
│  Clue: Log entry with TX_PACKET_ID                                      │
│  "[2026-02-16 14:21:58] INFO System monitoring services started |       │
│   TX_PACKET_ID: SFRCe3BzZ19kYXRhX2V4ZmlsfQ=="                          │
│                                                                          │
│  Encoding: Base64                                                        │
│                                                                          │
│  Command:                                                                │
│  echo "SFRCe3BzZ19kYXRhX2V4ZmlsfQ==" | base64 -d                       │
│                                                                          │
│  Result:                                                                 │
│  HTB{psg_data_exfil}                                                    │
│                                                                          │
│  ✅ FLAG 3                                                              │
│                                                                          │
│  Decoy flags: 3 fake flags in source                                    │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                         CHALLENGE COMPLETE                               │
│                                                                          │
│  Flags collected:                                                        │
│  ✅ HTB{psg_grade_swap}    - Image EXIF (ROT13)                        │
│  ✅ HTB{psg_sonic_exfil}   - Audio spectrogram (Caesar +7)             │
│  ✅ HTB{psg_data_exfil}    - Dashboard logs (Base64)                   │
│                                                                          │
│  Decoy flags avoided: 16 fake flags                                     │
│                                                                          │
│  Skills demonstrated:                                                    │
│  • Web reconnaissance                                                    │
│  • Metadata analysis                                                     │
│  • Credential discovery                                                  │
│  • Log analysis                                                          │
│  • EXIF extraction                                                       │
│  • Audio forensics                                                       │
│  • Encoding/decoding (ROT13, Caesar, Base64)                            │
│  • Critical thinking                                                     │
│  • Decoy identification                                                  │
│                                                                          │
│  🏆 CONGRATULATIONS! 🏆                                                 │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 📊 Challenge Statistics

### Difficulty Breakdown

```
Stage 1: Reconnaissance        ████░░░░░░ 40% - Easy
Stage 2: Portal Access         ██████░░░░ 60% - Medium
Stage 3: Incident Investigation ███████░░░ 70% - Medium
Stage 4: Artifact Analysis     ████████░░ 80% - Medium-Hard
Stage 5: Dashboard Analysis    █████░░░░░ 50% - Easy-Medium

Overall Difficulty: ██████░░░░ 60% - Medium
```

### Skill Requirements

```
Web Reconnaissance:     ████████░░ 80%
Forensics:              ████████░░ 80%
Cryptography:           ██████░░░░ 60%
Log Analysis:           ███████░░░ 70%
Tool Usage:             ████████░░ 80%
Critical Thinking:      █████████░ 90%
```

### Time Investment

```
Reconnaissance:         ████░░░░░░ 15-20 min
Portal Access:          ███░░░░░░░ 10-15 min
Incident Investigation: ████░░░░░░ 15-20 min
Artifact Analysis:      ████████░░ 30-40 min
Dashboard Analysis:     ██░░░░░░░░ 5-10 min

Total (Average):        ███████░░░ 75-105 min
```

---

## 🎯 Alternative Paths

Players can approach the challenge in different orders:

### Path A: Linear (Recommended)
```
Portal → Incident → Artifacts → Dashboard
```

### Path B: Dashboard First
```
Dashboard → Portal → Incident → Artifacts
```

### Path C: Parallel Investigation
```
Portal + Dashboard (parallel) → Incident → Artifacts
```

All paths lead to the same 3 flags, but the linear path provides the best narrative experience.

---

## 🔍 Key Decision Points

```
┌─────────────────────────────────────────────────────────────┐
│ Decision Point 1: Where to start?                           │
│ • student-portal.html (main entry)                          │
│ • dashboard.html (alternative)                              │
│ • robots.txt (reconnaissance)                               │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ Decision Point 2: How to find portal credentials?           │
│ • Brute force (won't work - hashed)                         │
│ • Source code analysis (correct)                            │
│ • Decoy credentials (wrong)                                 │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ Decision Point 3: How to unlock vault?                      │
│ • Guess password (unlikely)                                 │
│ • Read incident report carefully (correct)                  │
│ • Try decoy passwords (wrong)                               │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ Decision Point 4: Which flags are real?                     │
│ • Test all flags (time-consuming)                           │
│ • Validate through proper extraction (correct)              │
│ • Submit decoys (wrong)                                     │
└─────────────────────────────────────────────────────────────┘
```

---

## 📈 Learning Curve

```
Player Skill Level vs Challenge Difficulty

Difficulty
    ▲
100%│                                    ╱─────
    │                               ╱────
 75%│                          ╱────
    │                     ╱────
 50%│                ╱────
    │           ╱────
 25%│      ╱────
    │ ╱────
  0%└──────────────────────────────────────────▶
    Beginner  Intermediate  Advanced  Expert
    
    Beginner:     Will struggle, needs hints
    Intermediate: Perfect difficulty level
    Advanced:     Moderate challenge
    Expert:       Quick solve (20-30 min)
```

---

## 🎓 Educational Value

### Skills Taught

1. **Web Application Security**
   - Source code analysis
   - Metadata extraction
   - Client-side authentication weaknesses

2. **Digital Forensics**
   - EXIF metadata analysis
   - Audio spectrogram analysis
   - Log file investigation

3. **Cryptography**
   - ROT13 cipher
   - Caesar cipher
   - Base64 encoding

4. **Investigation Methodology**
   - Clue correlation
   - Information gathering
   - Logical deduction
   - Decoy identification

5. **Tool Proficiency**
   - exiftool
   - Audacity/Sonic Visualiser
   - Browser DevTools
   - Command-line utilities

---

**This challenge provides a comprehensive learning experience in cybersecurity investigation! 🎯**
