"""
EAS Weather Alert Generator
Generates Emergency Alert System notifications for severe weather
"""

from datetime import datetime, timedelta
from enum import Enum
import json
from typing import Dict, List, Optional


class AlertSeverity(Enum):
    """Alert severity levels"""
    EXTREME = "Extreme"
    SEVERE = "Severe"
    MODERATE = "Moderate"
    MINOR = "Minor"


class AlertUrgency(Enum):
    """Alert urgency levels"""
    IMMEDIATE = "Immediate"
    EXPECTED = "Expected"
    FUTURE = "Future"
    PAST = "Past"
    UNKNOWN = "Unknown"


class EventCode(Enum):
    """EAS Event Codes"""
    TORNADO_WARNING = "TOR"
    SEVERE_THUNDERSTORM_WARNING = "SVR"
    FLASH_FLOOD_WARNING = "FFW"
    WINTER_STORM_WARNING = "WSW"
    EXTREME_WIND_WARNING = "EWW"
    EXTREME_TEMPERATURE_WARNING = "EXT"
    DUST_STORM_WARNING = "DSW"
    HEAVY_SNOW_WARNING = "HSW"


class EASAlertGenerator:
    """Generate EAS weather alerts"""

    def __init__(self):
        self.alerts: List[Dict] = []

    def create_alert(
        self,
        event_code: EventCode,
        severity: AlertSeverity,
        urgency: AlertUrgency,
        affected_states: List[str],
        affected_counties: List[str],
        headline: str,
        description: str,
        instruction: str,
        duration_minutes: int = 60,
        originator: str = "NWS",
    ) -> Dict:
        """
        Create an EAS weather alert

        Args:
            event_code: Type of weather event
            severity: Severity level of alert
            urgency: Urgency level
            affected_states: List of state codes affected
            affected_counties: List of county FIPS codes
            headline: Alert headline
            description: Detailed description
            instruction: Safety instructions
            duration_minutes: Duration of alert validity
            originator: Originating agency code

        Returns:
            Dictionary containing alert data
        """
        now = datetime.utcnow()
        expiration = now + timedelta(minutes=duration_minutes)

        alert = {
            "alert_id": f"EAS-{now.strftime('%Y%m%d%H%M%S')}-{event_code.value}",
            "event_code": event_code.value,
            "originator_code": originator,
            "timestamp": now.isoformat() + "Z",
            "effective_date": now.isoformat() + "Z",
            "expiration_date": expiration.isoformat() + "Z",
            "duration_minutes": duration_minutes,
            "affected_areas": {
                "states": affected_states,
                "counties": affected_counties,
            },
            "severity": severity.value,
            "urgency": urgency.value,
            "headline": headline,
            "description": description,
            "instruction": instruction,
            "certainty": "Observed",
        }

        self.alerts.append(alert)
        return alert

    def get_active_alerts(self) -> List[Dict]:
        """Get all currently active alerts"""
        now = datetime.utcnow()
        return [
            alert
            for alert in self.alerts
            if alert["expiration_date"] > now.isoformat() + "Z"
        ]

    def export_alert_json(self, alert: Dict) -> str:
        """Export alert as JSON"""
        return json.dumps(alert, indent=2)

    def cancel_alert(self, alert_id: str) -> bool:
        """Cancel an active alert"""
        for alert in self.alerts:
            if alert["alert_id"] == alert_id:
                alert["expiration_date"] = datetime.utcnow().isoformat() + "Z"
                return True
        return False


# Example usage
if __name__ == "__main__":
    generator = EASAlertGenerator()

    # Create a tornado warning
    tornado_alert = generator.create_alert(
        event_code=EventCode.TORNADO_WARNING,
        severity=AlertSeverity.EXTREME,
        urgency=AlertUrgency.IMMEDIATE,
        affected_states=["OK", "KS"],
        affected_counties=["40017", "20001"],
        headline="TORNADO WARNING",
        description="A tornado has been sighted and is moving northeast at 40 mph.",
        instruction="Move to an interior room on the lowest floor of a sturdy building. Avoid windows.",
        duration_minutes=30,
    )

    print("EAS Alert Generated:")
    print(generator.export_alert_json(tornado_alert))