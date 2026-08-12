# Offline Review Guide for Chromebook

This guide explains how to review the EAS Weather Alert system offline on a Chromebook without needing an internet connection.

## Prerequisites for Chromebook

- Chromebook with Linux (Beta) enabled
- Git installed in Linux container
- Python 3.7+ installed in Linux container
- Text editor (nano, vim, or VS Code via Linux)

## Setting Up Linux on Your Chromebook

### Step 1: Enable Linux (Beta)

1. Open **Settings** on your Chromebook
2. Click **Advanced** on the left sidebar
3. Select **Developers** → **Linux development environment**
4. Click **Turn on**
5. Follow the setup wizard (this may take a few minutes)
6. A Linux terminal window will open

### Step 2: Install Required Tools

Open the Linux terminal and run:

```bash
# Update package manager
sudo apt update

# Install Git
sudo apt install -y git

# Install Python and pip
sudo apt install -y python3 python3-pip

# Verify installations
git --version
python3 --version
```

## Cloning the Repository on Chromebook

### Step 1: Create a Project Directory

```bash
# Create a directory for your projects
mkdir -p ~/projects
cd ~/projects
```

### Step 2: Clone the Repository

```bash
git clone https://github.com/baxleychris9-spec/Eas-Weather-alert-for-USA.git
cd Eas-Weather-alert-for-USA
```

### Step 3: Verify the Clone

```bash
# List files to confirm clone was successful
ls -la

# You should see:
# - README.md
# - docs/
# - src/
# - config/
# - alerts/
```

## Reviewing Code on Chromebook

### Using the Terminal Text Editor

**Option 1: Nano (Easiest for Beginners)**

```bash
# View alert generator
nano src/alert_generator.py

# View configuration
nano config/weather_events.json

# View template
nano alerts/eas_alert_template.json

# Press Ctrl+X to exit
```

**Option 2: Vim (Advanced)**

```bash
# View with Vim
vim src/alert_generator.py

# Press :q to exit
```

### Using VS Code on Chromebook

If you have VS Code installed in Linux:

```bash
# Open the project in VS Code
code .

# Or open a specific file
code src/alert_generator.py
```

**Setting up VS Code on Chromebook:**
1. Open Linux terminal
2. Install VS Code:
   ```bash
   sudo apt install -y code
   ```
3. Navigate to project and run `code .`

## File Structure to Review

```
Eas-Weather-alert-for-USA/
├── README.md                          # Project overview
├── docs/
│   ├── GETTING_STARTED.md            # Quick start guide
│   ├── OFFLINE_REVIEW.md             # General offline guide
│   └── CHROMEBOOK_REVIEW.md          # This guide
├── src/
│   └── alert_generator.py            # Main alert generation logic
├── config/
│   └── weather_events.json           # Weather event configurations
└── alerts/
    └── eas_alert_template.json       # Alert template structure
```

## Viewing Files on Chromebook

### Quick View with Cat Command

```bash
# Quick view of files without opening editor
cat src/alert_generator.py
cat config/weather_events.json
cat README.md
```

### Search Within Files

```bash
# Search for specific text in files
grep -r "EventCode" src/

# Search for "Tornado" in configuration
grep -i "tornado" config/weather_events.json

# Count lines in a file
wc -l src/alert_generator.py
```

## Testing on Chromebook

### Run the Alert Generator

```bash
# Navigate to project directory
cd ~/projects/Eas-Weather-alert-for-USA

# Run the example in alert_generator.py
python3 src/alert_generator.py
```

**Expected Output:**
```
EAS Alert Generated:
{
  "alert_id": "EAS-20260812T023059-TOR",
  "event_code": "TOR",
  "originator_code": "NWS",
  "timestamp": "2026-08-12T02:30:59Z",
  "effective_date": "2026-08-12T02:30:59Z",
  "expiration_date": "2026-08-12T02:31:59Z",
  "duration_minutes": 30,
  "affected_areas": {
    "states": ["OK", "KS"],
    "counties": ["40017", "20001"]
  },
  "severity": "Extreme",
  "urgency": "Immediate",
  "headline": "TORNADO WARNING",
  "description": "A tornado has been sighted and is moving northeast at 40 mph.",
  "instruction": "Move to an interior room on the lowest floor of a sturdy building. Avoid windows.",
  "certainty": "Observed"
}
```

### Create a Test Script on Chromebook

Create a new test file:

```bash
# Create test file
nano test_offline.py
```

Paste this content:

```python
#!/usr/bin/env python3
"""
Offline testing script for EAS Weather Alert system
Run on Chromebook: python3 test_offline.py
"""

from src.alert_generator import EASAlertGenerator, EventCode, AlertSeverity, AlertUrgency
import json

def test_tornado_alert():
    """Test tornado warning creation"""
    generator = EASAlertGenerator()
    alert = generator.create_alert(
        event_code=EventCode.TORNADO_WARNING,
        severity=AlertSeverity.EXTREME,
        urgency=AlertUrgency.IMMEDIATE,
        affected_states=["OK", "KS"],
        affected_counties=["40017", "20001"],
        headline="TORNADO WARNING",
        description="A tornado has been sighted and is moving northeast at 40 mph.",
        instruction="Move to an interior room on the lowest floor of a sturdy building.",
        duration_minutes=30
    )
    print("✓ Tornado alert created successfully")
    print(json.dumps(alert, indent=2))

def test_flood_alert():
    """Test flood warning creation"""
    generator = EASAlertGenerator()
    alert = generator.create_alert(
        event_code=EventCode.FLASH_FLOOD_WARNING,
        severity=AlertSeverity.SEVERE,
        urgency=AlertUrgency.IMMEDIATE,
        affected_states=["TX", "LA"],
        affected_counties=["48201", "22001"],
        headline="FLASH FLOOD WARNING",
        description="Flash flooding is expected in low-lying areas.",
        instruction="Move to higher ground immediately.",
        duration_minutes=60
    )
    print("✓ Flood alert created successfully")
    print(json.dumps(alert, indent=2))

def test_multiple_events():
    """Test multiple event types"""
    generator = EASAlertGenerator()
    events = [
        (EventCode.TORNADO_WARNING, AlertSeverity.EXTREME, "Tornado"),
        (EventCode.SEVERE_THUNDERSTORM_WARNING, AlertSeverity.SEVERE, "Thunderstorm"),
        (EventCode.WINTER_STORM_WARNING, AlertSeverity.SEVERE, "Winter Storm"),
    ]
    
    for event_code, severity, name in events:
        alert = generator.create_alert(
            event_code=event_code,
            severity=severity,
            urgency=AlertUrgency.IMMEDIATE,
            affected_states=["OK"],
            affected_counties=["40017"],
            headline=f"{name.upper()} WARNING",
            description=f"Testing {name}",
            instruction="Seek shelter",
            duration_minutes=30
        )
        print(f"✓ {name} alert created")

if __name__ == "__main__":
    print("=" * 50)
    print("EAS Weather Alert System - Chromebook Offline Tests")
    print("=" * 50)
    print()
    
    test_tornado_alert()
    print()
    
    test_flood_alert()
    print()
    
    test_multiple_events()
    print()
    
    print("=" * 50)
    print("All Chromebook offline tests completed!")
    print("=" * 50)
```

Save (Ctrl+O, Enter, Ctrl+X) and run:

```bash
python3 test_offline.py
```

## Chromebook-Specific Commands

### Useful Terminal Commands for Chromebook

```bash
# Navigate to project
cd ~/projects/Eas-Weather-alert-for-USA

# List all files
ls -la

# Check file size
du -sh *

# View line count
wc -l src/alert_generator.py config/weather_events.json

# Search for keywords
grep -n "Severe" config/weather_events.json

# Copy a file for backup
cp src/alert_generator.py src/alert_generator.py.bak

# View git history
git log --oneline

# Check current branch
git branch

# View differences between files
diff -u alerts/eas_alert_template.json config/weather_events.json
```

## Code Review Checklist for Chromebook

Print or save this checklist:

```bash
# Create checklist file
nano CHROMEBOOK_REVIEW_CHECKLIST.md
```

Contents:

```markdown
# Chromebook Code Review Checklist

## Code Quality
- [ ] Code is well-organized
- [ ] Indentation is consistent (Python uses 4 spaces)
- [ ] Comments explain complex logic
- [ ] Variable names are descriptive
- [ ] No duplicate code

## Alert Generator (src/alert_generator.py)
- [ ] All event codes are defined
- [ ] Severity levels are clearly categorized
- [ ] Timestamp format is correct (ISO 8601)
- [ ] Expiration calculation is accurate
- [ ] JSON export works properly

## Configuration (config/weather_events.json)
- [ ] All weather events are defined
- [ ] Safety instructions are clear
- [ ] Regional definitions are complete
- [ ] Duration values are reasonable
- [ ] JSON is valid (no syntax errors)

## Template (alerts/eas_alert_template.json)
- [ ] All required fields are present
- [ ] Placeholder names are consistent
- [ ] JSON structure is valid

## Documentation
- [ ] README explains purpose clearly
- [ ] Getting Started guide is complete
- [ ] Code comments explain logic
- [ ] Examples are runnable

## Testing
- [ ] alert_generator.py runs without errors
- [ ] test_offline.py produces expected output
- [ ] Alert objects are created correctly
- [ ] JSON output is valid

## Issues Found
(List any problems here)
1. 
2. 
3. 

## Suggestions for Improvement
(List suggestions here)
1. 
2. 
3. 
```

## Taking Notes on Chromebook

Create a notes file:

```bash
# Create review notes
nano REVIEW_NOTES.md
```

Use this format:

```markdown
# Review Notes - [Your Date]

## File: src/alert_generator.py
- Line 15-20: Alert creation logic is clear
- Line 45: Consider adding validation for county codes
- Overall: Well-structured and readable

## File: config/weather_events.json
- All weather types are covered
- Safety instructions are comprehensive
- Suggest adding more detailed descriptions

## File: alerts/eas_alert_template.json
- Template structure is logical
- All necessary fields included

## Summary
- Project is well-organized
- Code is readable and maintainable
- Documentation is helpful

## Action Items
- [ ] Test with custom weather data
- [ ] Verify all safety instructions
- [ ] Check for edge cases in timestamp handling
```

## Managing Projects on Chromebook

### Switching Between Files

```bash
# Open different files for comparison
nano src/alert_generator.py
# Exit (Ctrl+X)
nano config/weather_events.json
# Exit (Ctrl+X)
nano alerts/eas_alert_template.json
```

### Using Split Screen

1. Open your files app
2. Drag the Linux terminal to one side
3. Open a text editor on the other side
4. Review side-by-side

### Screenshot for Documentation

```bash
# Use Chromebook's built-in screenshot
# Press: Ctrl + Show Windows (F5)
# Select area to capture
```

## Backing Up Your Review

```bash
# Create backup of your notes
cp REVIEW_NOTES.md REVIEW_NOTES.md.backup

# Create compressed archive of entire project
tar -czf Eas-Weather-alert-backup.tar.gz Eas-Weather-alert-for-USA/

# List backup
ls -lh Eas-Weather-alert-backup.tar.gz
```

## Syncing with Internet (When Available)

```bash
# Check current status
git status

# View recent commits
git log --oneline -5

# When connected to internet:
git fetch origin
git pull origin main

# Push your notes if you've made commits
git push origin main
```

## Chromebook Tips & Tricks

### Opening Terminal Quickly
- Press: `Ctrl + Alt + T`

### Using Command History
- Press: `Up Arrow` to see previous commands
- Press: `Down Arrow` to see next commands

### Clear Terminal
```bash
clear
```

### Get Help on Any Command
```bash
man python3
man git
man grep

# Exit help: press q
```

### Create Quick Notes
```bash
# Use echo to append to file quickly
echo "Found issue with timestamp handling" >> NOTES.txt
echo "- Consider adding UTC validation" >> NOTES.txt
cat NOTES.txt
```

## Troubleshooting on Chromebook

### Python Not Found
```bash
# Use python3 instead of python
python3 --version
python3 src/alert_generator.py
```

### Permission Denied
```bash
# Add execute permission to scripts
chmod +x test_offline.py
./test_offline.py
```

### Out of Space
```bash
# Check disk usage
df -h

# Remove old backups
rm *.backup
```

### Terminal Won't Close
```bash
# Type exit or press Ctrl+D
exit
```

## Recommended Workflow on Chromebook

1. **Setup (5 minutes)**
   ```bash
   cd ~/projects/Eas-Weather-alert-for-USA
   ```

2. **Review Code (20-30 minutes)**
   ```bash
   nano src/alert_generator.py
   nano config/weather_events.json
   ```

3. **Test Functionality (10 minutes)**
   ```bash
   python3 src/alert_generator.py
   python3 test_offline.py
   ```

4. **Document Findings (10 minutes)**
   ```bash
   nano REVIEW_NOTES.md
   ```

5. **Create Backup (5 minutes)**
   ```bash
   tar -czf review-backup.tar.gz .
   ```

## Total Time: ~1 Hour Completely Offline

---

**Note:** This guide is optimized for Chromebook Linux environment. All commands work in the Linux terminal without internet connection after initial clone.

For questions or issues specific to Chromebook setup, check the Chromebook Help Center: https://support.google.com/chromebook/

