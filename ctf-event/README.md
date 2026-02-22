# CTF Event - University Breach Investigation

## Project Structure

```
ctf-event/
├── round-1/
│   └── challenge-portal/
│       ├── student-portal.html       # Entry point
│       ├── it-alert.html             # Incident report
│       ├── dashboard.html            # Dashboard with flag
│       ├── portal_backup_2025.html   # Backup file (decoys)
│       ├── artifacts/
│       │   ├── defaced_grade.jpg     # Image with EXIF flag
│       │   └── rogue_signal.wav      # Audio with spectrogram flag
│       ├── generators/
│       │   ├── artifact_alpha.py     # Generate image artifact
│       │   └── artifact_beta.py      # Generate audio artifact
│       └── documentation/
│           └── system_logs.txt       # System logs with hints
├── round-2/
│   └── (placeholder for future challenges)
├── common/
│   └── robots.txt                    # Shared robots.txt
├── README.md                         # This file
├── ADMIN_GUIDE.md                    # Solutions and passwords
└── QUICKSTART.md                     # Quick deployment guide
```

## Quick Start

### 1. Generate Artifacts
```bash
cd round-1/challenge-portal/generators
python3 artifact_alpha.py
python3 artifact_beta.py
```

### 2. Deploy
```bash
cd round-1/challenge-portal
python3 -m http.server 8000
```

### 3. Access
Open: http://localhost:8000/student-portal.html

## Real Flags
- HTB{psg_grade_swap} - Image EXIF (ROT13)
- HTB{psg_sonic_exfil} - Audio spectrogram (Caesar +7)
- HTB{psg_data_exfil} - Dashboard logs (Base64)

## Passwords
- Portal: sysadmin:2.1.447
- Vault: OP-GRADE-SWAP-89

See ADMIN_GUIDE.md for complete solutions.
