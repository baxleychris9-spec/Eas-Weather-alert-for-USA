# Offline Review Guide

This guide explains how to review the EAS Weather Alert system offline without needing an internet connection.

## Prerequisites

- Git installed on your system
- Python 3.7+ (for running the alert generator)
- A text editor or IDE

## Setup for Offline Review

### 1. Clone the Repository

```bash
git clone https://github.com/baxleychris9-spec/Eas-Weather-alert-for-USA.git
cd Eas-Weather-alert-for-USA
```

This creates a complete local copy of the project with full git history.

### 2. Verify Offline Access

Once cloned, you have complete access to:
- All source code files
- Configuration files
- Documentation
- Full commit history
- All branches and tags

No internet connection is required after cloning.

## Reviewing the Code Offline

### File Structure to Review

```
Eas-Weather-alert-for-USA/
├── README.md                          # Project overview
├── docs/
│   ├── GETTING_STARTED.md            # Quick start guide
│   └── OFFLINE_REVIEW.md             # This file
├── src/
│   └── alert_generator.py            # Main alert generation logic
├── config/
│   └── weather_events.json           # Weather event configurations
└── alerts/
    └── eas_alert_template.json       # Alert template structure
```

### Key Files to Review

1. **src/alert_generator.py** - Core functionality
   - Review the `EASAlertGenerator` class
   - Check the `create_alert()` method
   - Examine event codes and severity levels
   - Verify timestamp and expiration logic

2. **config/weather_events.json** - Configuration
   - Review supported weather event types
   - Check safety instructions
   - Verify regional definitions
   - Examine duration settings

3. **alerts/eas_alert_template.json** - Template
   - Verify alert structure
   - Check required fields
   - Review placeholder variables

## Testing Offline

### Run the Alert Generator

```bash
# Navigate to the project directory
cd Eas-Weather-alert-for-USA

# Run the example in alert_generator.py
python src/alert_generator.py
```

**Expected Output:**
```json
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

### Create a Test Script

Create a file named `test_offline.py` to run custom tests:

```python
#!/usr/bin/env python3
"""
Offline testing script for EAS Weather Alert system
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

def test_active_alerts():
    """Test retrieving active alerts"""
    generator = EASAlertGenerator()
    
    # Create multiple alerts
    alert1 = generator.create_alert(
        event_code=EventCode.TORNADO_WARNING,
        severity=AlertSeverity.EXTREME,
        urgency=AlertUrgency.IMMEDIATE,
        affected_states=["OK"],
        affected_counties=["40017"],
        headline="TORNADO WARNING",
        description="Tornado sighting",
        instruction="Take shelter",
        duration_minutes=30
    )
    
    alert2 = generator.create_alert(
        event_code=EventCode.WINTER_STORM_WARNING,
        severity=AlertSeverity.SEVERE,
        urgency=AlertUrgency.EXPECTED,
        affected_states=["CO"],
        affected_counties=["08001"],
        headline="WINTER STORM WARNING",
        description="Heavy snow expected",
        instruction="Avoid travel",
        duration_minutes=480
    )
    
    active = generator.get_active_alerts()
    print(f"✓ {len(active)} active alerts found")

if __name__ == "__main__":
    print("=" * 50)
    print("EAS Weather Alert System - Offline Tests")
    print("=" * 50)
    print()
    
    test_tornado_alert()
    print()
    
    test_flood_alert()
    print()
    
    test_active_alerts()
    print()
    
    print("=" * 50)
    print("All offline tests completed!")
    print("=" * 50)
```

Run the test script:
```bash
python test_offline.py
```

## Code Review Checklist

Use this checklist while reviewing offline:

- [ ] Alert generator correctly implements all event codes
- [ ] Severity and urgency enums are properly defined
- [ ] Timestamp generation uses UTC format correctly
- [ ] Expiration date calculations are accurate
- [ ] Alert JSON structure matches template
- [ ] Weather events configuration is comprehensive
- [ ] Safety instructions are clear and actionable
- [ ] Regional definitions cover all US states
- [ ] Documentation is clear and complete
- [ ] Code follows Python best practices

## Documentation Review

Read these files in order:

1. `README.md` - Understand the project purpose
2. `docs/GETTING_STARTED.md` - Learn how to use the system
3. `src/alert_generator.py` - Review the implementation
4. `config/weather_events.json` - Examine configurations
5. `alerts/eas_alert_template.json` - Verify alert structure

## Making Notes Offline

Create a file to document your review findings:

```bash
# Create a review notes file
touch REVIEW_NOTES.md
```

Example format:
```markdown
# Offline Review Notes - [Date]

## Code Quality
- [x] Code is well-organized
- [x] Documentation is clear
- [ ] Consider adding unit tests

## Functionality
- [x] Alert generation works correctly
- [x] All event types are supported
- [ ] Consider adding alert filtering by region

## Suggestions
1. Add logging for alert creation
2. Create validation for county FIPS codes
3. Add alert persistence to database

## Issues Found
- None at this time
```

## Syncing Changes

When you're ready to sync your review:

```bash
# Check status
git status

# View changes since last sync
git log --oneline -10

# When connected to internet:
git fetch origin
git pull origin main
git push origin [your-branch-name]
```

## Additional Resources

- Python Documentation: https://docs.python.org/3/
- Git Documentation: https://git-scm.com/doc
- EAS Information: https://www.fema.gov/emergency-managers/hazards/eas

---

**Note:** This guide enables complete offline review and testing of the EAS Weather Alert system. No internet connection is required after the initial clone.
