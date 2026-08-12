# Getting Started with EAS Weather Alert System

## Overview

This is an Emergency Alert System (EAS) weather alert system for the USA that generates and manages severe weather notifications.

## System Components

### 1. Alert Generator (`src/alert_generator.py`)
Generates EAS weather alerts with specified parameters:
- Event codes (Tornado, Severe Thunderstorm, Flash Flood, etc.)
- Severity levels (Extreme, Severe, Moderate, Minor)
- Urgency levels (Immediate, Expected, Future)
- Affected geographic areas (states and counties)

### 2. Alert Templates (`alerts/eas_alert_template.json`)
JSON template for standardizing alert format and structure

### 3. Weather Events Configuration (`config/weather_events.json`)
Pre-defined weather event types with:
- Duration specifications
- Safety instructions
- Severity classifications
- US regional definitions

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/baxleychris9-spec/Eas-Weather-alert-for-USA.git
cd Eas-Weather-alert-for-USA

# Install Python dependencies (if any)
pip install -r requirements.txt
```

### Creating an Alert

```python
from src.alert_generator import EASAlertGenerator, EventCode, AlertSeverity, AlertUrgency

# Initialize generator
generator = EASAlertGenerator()

# Create a tornado warning alert
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

# Export as JSON
print(generator.export_alert_json(alert))
```

## Alert Types

Supported weather event codes:

- **TOR** - Tornado Warning
- **SVR** - Severe Thunderstorm Warning
- **FFW** - Flash Flood Warning
- **WSW** - Winter Storm Warning
- **EWW** - Extreme Wind Warning
- **EXT** - Extreme Temperature Warning
- **DSW** - Dust Storm Warning
- **HSW** - Heavy Snow Warning

## Alert Severity Levels

- **Extreme** - Most severe, immediate danger
- **Severe** - Significant threat to life and property
- **Moderate** - Potential for property damage
- **Minor** - Possible inconvenience or minor damage

## Development

See the main README.md for project structure and contribution guidelines.

## Support

For issues or questions, please open an issue on the GitHub repository.