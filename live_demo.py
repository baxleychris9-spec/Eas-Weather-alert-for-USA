#!/usr/bin/env python3
"""
EAS Weather Alert System - Interactive Live Demo
Run on Chromebook: python3 live_demo.py

This interactive demo allows you to:
- Create weather alerts in real-time
- View different alert types
- Export alerts to JSON
- Manage active alerts
"""

import json
import sys
from datetime import datetime, timedelta
from enum import Enum
from src.alert_generator import EASAlertGenerator, EventCode, AlertSeverity, AlertUrgency


class Color:
    """Terminal color codes"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def clear_screen():
    """Clear terminal screen"""
    print("\033[2J\033[H", end="")


def print_header(text):
    """Print formatted header"""
    print(f"\n{Color.HEADER}{Color.BOLD}{'='*60}{Color.END}")
    print(f"{Color.HEADER}{Color.BOLD}{text.center(60)}{Color.END}")
    print(f"{Color.HEADER}{Color.BOLD}{'='*60}{Color.END}\n")


def print_success(text):
    """Print success message"""
    print(f"{Color.GREEN}✓ {text}{Color.END}")


def print_error(text):
    """Print error message"""
    print(f"{Color.RED}✗ {text}{Color.END}")


def print_info(text):
    """Print info message"""
    print(f"{Color.CYAN}ℹ {text}{Color.END}")


def print_alert_preview(alert):
    """Print alert in readable format"""
    print(f"\n{Color.BOLD}{Color.BLUE}Alert ID:{Color.END} {alert['alert_id']}")
    print(f"{Color.BOLD}{Color.BLUE}Event:{Color.END} {alert['event_code']}")
    print(f"{Color.BOLD}{Color.BLUE}Severity:{Color.END} {alert['severity']}")
    print(f"{Color.BOLD}{Color.BLUE}Urgency:{Color.END} {alert['urgency']}")
    print(f"{Color.BOLD}{Color.BLUE}States:{Color.END} {', '.join(alert['affected_areas']['states'])}")
    print(f"{Color.BOLD}{Color.BLUE}Counties:{Color.END} {', '.join(alert['affected_areas']['counties'])}")
    print(f"{Color.BOLD}{Color.BLUE}Duration:{Color.END} {alert['duration_minutes']} minutes")
    print(f"{Color.BOLD}{Color.BLUE}Headline:{Color.END} {alert['headline']}")
    print(f"{Color.BOLD}{Color.BLUE}Description:{Color.END} {alert['description']}")
    print(f"{Color.BOLD}{Color.BLUE}Instruction:{Color.END} {alert['instruction']}")
    print(f"{Color.BOLD}{Color.BLUE}Effective:{Color.END} {alert['effective_date']}")
    print(f"{Color.BOLD}{Color.BLUE}Expires:{Color.END} {alert['expiration_date']}")


def demo_menu():
    """Display main menu"""
    print(f"\n{Color.BOLD}Main Menu:{Color.END}")
    print("  1. Create a Tornado Warning")
    print("  2. Create a Severe Thunderstorm Warning")
    print("  3. Create a Flash Flood Warning")
    print("  4. Create a Winter Storm Warning")
    print("  5. Create an Extreme Wind Warning")
    print("  6. Create a Custom Alert")
    print("  7. View Active Alerts")
    print("  8. Export Alert to JSON File")
    print("  9. Cancel an Alert")
    print("  10. View Sample Alerts")
    print("  11. Exit Demo")
    print()


def create_tornado_warning(generator):
    """Create tornado warning alert"""
    print_info("Creating Tornado Warning Alert...")
    
    alert = generator.create_alert(
        event_code=EventCode.TORNADO_WARNING,
        severity=AlertSeverity.EXTREME,
        urgency=AlertUrgency.IMMEDIATE,
        affected_states=["OK", "KS"],
        affected_counties=["40017", "20001"],
        headline="TORNADO WARNING",
        description="A tornado has been sighted and is moving northeast at 40 mph. Significant damage is expected.",
        instruction="Move to an interior room on the lowest floor of a sturdy building. Avoid windows. If in a mobile home, evacuate immediately to a sturdy shelter.",
        duration_minutes=30
    )
    
    print_success("Tornado Warning Alert Created!")
    print_alert_preview(alert)
    return alert


def create_thunderstorm_warning(generator):
    """Create severe thunderstorm warning"""
    print_info("Creating Severe Thunderstorm Warning Alert...")
    
    alert = generator.create_alert(
        event_code=EventCode.SEVERE_THUNDERSTORM_WARNING,
        severity=AlertSeverity.SEVERE,
        urgency=AlertUrgency.IMMEDIATE,
        affected_states=["TX", "OK"],
        affected_counties=["48201", "40017"],
        headline="SEVERE THUNDERSTORM WARNING",
        description="Severe thunderstorms are occurring with damaging winds, large hail up to 2 inches, and isolated tornadoes.",
        instruction="Take shelter in a sturdy building away from windows. If outdoors, move away from trees and metal objects.",
        duration_minutes=60
    )
    
    print_success("Severe Thunderstorm Warning Alert Created!")
    print_alert_preview(alert)
    return alert


def create_flood_warning(generator):
    """Create flash flood warning"""
    print_info("Creating Flash Flood Warning Alert...")
    
    alert = generator.create_alert(
        event_code=EventCode.FLASH_FLOOD_WARNING,
        severity=AlertSeverity.SEVERE,
        urgency=AlertUrgency.IMMEDIATE,
        affected_states=["LA", "TX"],
        affected_counties=["22001", "48201"],
        headline="FLASH FLOOD WARNING",
        description="Flash flooding is imminent or already occurring. Water is rising rapidly in creeks, streams, and urban areas.",
        instruction="Move to higher ground immediately. Do not attempt to cross flooded roads or streams. Turn around - don't drown!",
        duration_minutes=60
    )
    
    print_success("Flash Flood Warning Alert Created!")
    print_alert_preview(alert)
    return alert


def create_winter_storm_warning(generator):
    """Create winter storm warning"""
    print_info("Creating Winter Storm Warning Alert...")
    
    alert = generator.create_alert(
        event_code=EventCode.WINTER_STORM_WARNING,
        severity=AlertSeverity.SEVERE,
        urgency=AlertUrgency.EXPECTED,
        affected_states=["CO", "WY"],
        affected_counties=["08001", "56001"],
        headline="WINTER STORM WARNING",
        description="Heavy snow, ice, and blizzard conditions are expected. Visibility will be near zero at times. Significant snow accumulation expected.",
        instruction="Avoid travel if possible. If travel is necessary, use extreme caution and keep emergency supplies in your vehicle.",
        duration_minutes=480
    )
    
    print_success("Winter Storm Warning Alert Created!")
    print_alert_preview(alert)
    return alert


def create_wind_warning(generator):
    """Create extreme wind warning"""
    print_info("Creating Extreme Wind Warning Alert...")
    
    alert = generator.create_alert(
        event_code=EventCode.EXTREME_WIND_WARNING,
        severity=AlertSeverity.EXTREME,
        urgency=AlertUrgency.IMMEDIATE,
        affected_states=["CA", "NV"],
        affected_counties=["06001", "32001"],
        headline="EXTREME WIND WARNING",
        description="Extreme winds capable of producing significant damage are occurring or imminent. Winds will exceed 60 mph.",
        instruction="Secure loose objects and trash cans. Stay indoors and away from windows. Be prepared for widespread power outages.",
        duration_minutes=45
    )
    
    print_success("Extreme Wind Warning Alert Created!")
    print_alert_preview(alert)
    return alert


def create_custom_alert(generator):
    """Create custom alert with user input"""
    print_info("Creating Custom Alert...")
    print()
    
    # Event code selection
    print(f"{Color.BOLD}Available Event Codes:{Color.END}")
    codes = {
        "1": (EventCode.TORNADO_WARNING, "Tornado Warning"),
        "2": (EventCode.SEVERE_THUNDERSTORM_WARNING, "Severe Thunderstorm Warning"),
        "3": (EventCode.FLASH_FLOOD_WARNING, "Flash Flood Warning"),
        "4": (EventCode.WINTER_STORM_WARNING, "Winter Storm Warning"),
        "5": (EventCode.EXTREME_WIND_WARNING, "Extreme Wind Warning"),
        "6": (EventCode.EXTREME_TEMPERATURE_WARNING, "Extreme Temperature Warning"),
    }
    
    for key, (code, name) in codes.items():
        print(f"  {key}. {name}")
    
    code_choice = input("\nSelect event code (1-6): ").strip()
    if code_choice not in codes:
        print_error("Invalid selection")
        return None
    
    event_code, code_name = codes[code_choice]
    
    # Severity selection
    print(f"\n{Color.BOLD}Severity Levels:{Color.END}")
    severities = {
        "1": AlertSeverity.EXTREME,
        "2": AlertSeverity.SEVERE,
        "3": AlertSeverity.MODERATE,
        "4": AlertSeverity.MINOR,
    }
    
    for key, sev in severities.items():
        print(f"  {key}. {sev.value}")
    
    sev_choice = input("\nSelect severity (1-4): ").strip()
    if sev_choice not in severities:
        print_error("Invalid selection")
        return None
    
    severity = severities[sev_choice]
    
    # Get affected states
    states = input("\nEnter affected states (comma-separated, e.g., OK,KS): ").strip().split(",")
    states = [s.strip().upper() for s in states]
    
    # Get affected counties
    counties = input("Enter affected counties (comma-separated FIPS codes, e.g., 40017,20001): ").strip().split(",")
    counties = [c.strip() for c in counties]
    
    # Get headline
    headline = input("Enter alert headline: ").strip()
    
    # Get description
    description = input("Enter alert description: ").strip()
    
    # Get instruction
    instruction = input("Enter safety instruction: ").strip()
    
    # Get duration
    try:
        duration = int(input("Enter duration in minutes (e.g., 30): ").strip())
    except ValueError:
        duration = 30
    
    # Create the alert
    alert = generator.create_alert(
        event_code=event_code,
        severity=severity,
        urgency=AlertUrgency.IMMEDIATE,
        affected_states=states,
        affected_counties=counties,
        headline=headline,
        description=description,
        instruction=instruction,
        duration_minutes=duration
    )
    
    print_success("Custom Alert Created!")
    print_alert_preview(alert)
    return alert


def view_active_alerts(generator):
    """Display all active alerts"""
    active = generator.get_active_alerts()
    
    if not active:
        print_error("No active alerts at this time")
        return
    
    print_success(f"Found {len(active)} active alert(s)")
    
    for i, alert in enumerate(active, 1):
        print(f"\n{Color.BOLD}{Color.CYAN}Alert {i}:{Color.END}")
        print_alert_preview(alert)


def export_alert_to_file(generator, alert=None):
    """Export alert to JSON file"""
    active = generator.get_active_alerts()
    
    if not active:
        print_error("No active alerts to export")
        return
    
    if len(active) == 1:
        alert = active[0]
        filename = f"alert_{alert['alert_id'].replace(':', '_').replace('-', '_')}.json"
    else:
        print(f"\n{Color.BOLD}Available Alerts:{Color.END}")
        for i, alert in enumerate(active, 1):
            print(f"  {i}. {alert['alert_id']} ({alert['event_code']})")
        
        try:
            choice = int(input("\nSelect alert number to export: ").strip())
            if 1 <= choice <= len(active):
                alert = active[choice - 1]
                filename = f"alert_{alert['alert_id'].replace(':', '_').replace('-', '_')}.json"
            else:
                print_error("Invalid selection")
                return
        except ValueError:
            print_error("Invalid input")
            return
    
    try:
        with open(filename, 'w') as f:
            json.dump(alert, f, indent=2)
        print_success(f"Alert exported to {filename}")
        
        # Show file info
        import os
        size = os.path.getsize(filename)
        print_info(f"File size: {size} bytes")
        
        # Ask to view
        view = input("\nView file contents? (y/n): ").strip().lower()
        if view == 'y':
            with open(filename, 'r') as f:
                print(f"\n{Color.BOLD}File Contents:{Color.END}")
                print(f.read())
    except Exception as e:
        print_error(f"Failed to export: {str(e)}")


def cancel_alert(generator):
    """Cancel an active alert"""
    active = generator.get_active_alerts()
    
    if not active:
        print_error("No active alerts to cancel")
        return
    
    print(f"\n{Color.BOLD}Active Alerts:{Color.END}")
    for i, alert in enumerate(active, 1):
        print(f"  {i}. {alert['alert_id']} ({alert['event_code']})")
    
    try:
        choice = int(input("\nSelect alert number to cancel (0 to skip): ").strip())
        if choice == 0:
            print_info("Cancellation skipped")
            return
        elif 1 <= choice <= len(active):
            alert = active[choice - 1]
            if generator.cancel_alert(alert['alert_id']):
                print_success(f"Alert {alert['alert_id']} has been cancelled")
            else:
                print_error("Failed to cancel alert")
        else:
            print_error("Invalid selection")
    except ValueError:
        print_error("Invalid input")


def show_sample_alerts():
    """Display sample alerts"""
    samples = [
        {
            "title": "Tornado Warning",
            "code": "TOR",
            "severity": "Extreme",
            "description": "A tornado has been sighted and is moving northeast at 40 mph.",
            "instruction": "Move to an interior room on the lowest floor of a sturdy building."
        },
        {
            "title": "Severe Thunderstorm Warning",
            "code": "SVR",
            "severity": "Severe",
            "description": "Severe thunderstorms with damaging winds and large hail.",
            "instruction": "Take shelter in a sturdy building away from windows."
        },
        {
            "title": "Flash Flood Warning",
            "code": "FFW",
            "severity": "Severe",
            "description": "Flash flooding is imminent or already occurring.",
            "instruction": "Move to higher ground immediately. Turn around - don't drown!"
        },
        {
            "title": "Winter Storm Warning",
            "code": "WSW",
            "severity": "Severe",
            "description": "Heavy snow and blizzard conditions are expected.",
            "instruction": "Avoid travel. Keep emergency supplies in vehicle."
        }
    ]
    
    print(f"\n{Color.BOLD}Sample Alert Types:{Color.END}\n")
    for i, sample in enumerate(samples, 1):
        print(f"{Color.BOLD}{Color.CYAN}{i}. {sample['title']}{Color.END}")
        print(f"   Code: {sample['code']}")
        print(f"   Severity: {sample['severity']}")
        print(f"   Description: {sample['description']}")
        print(f"   Instruction: {sample['instruction']}")
        print()


def main():
    """Main demo loop"""
    clear_screen()
    print_header("EAS Weather Alert System - Live Demo")
    
    print(f"{Color.CYAN}Welcome to the EAS Weather Alert System!{Color.END}")
    print("This interactive demo allows you to create and manage weather alerts.")
    print(f"\n{Color.YELLOW}Press Enter to continue...{Color.END}")
    input()
    
    generator = EASAlertGenerator()
    last_alert = None
    
    while True:
        clear_screen()
        print_header("EAS Weather Alert System - Live Demo")
        
        if generator.get_active_alerts():
            active_count = len(generator.get_active_alerts())
            print_info(f"Currently {active_count} active alert(s)")
        
        demo_menu()
        choice = input(f"{Color.BOLD}Enter your choice (1-11):{Color.END} ").strip()
        
        if choice == "1":
            clear_screen()
            print_header("Tornado Warning Alert")
            last_alert = create_tornado_warning(generator)
        
        elif choice == "2":
            clear_screen()
            print_header("Severe Thunderstorm Warning Alert")
            last_alert = create_thunderstorm_warning(generator)
        
        elif choice == "3":
            clear_screen()
            print_header("Flash Flood Warning Alert")
            last_alert = create_flood_warning(generator)
        
        elif choice == "4":
            clear_screen()
            print_header("Winter Storm Warning Alert")
            last_alert = create_winter_storm_warning(generator)
        
        elif choice == "5":
            clear_screen()
            print_header("Extreme Wind Warning Alert")
            last_alert = create_wind_warning(generator)
        
        elif choice == "6":
            clear_screen()
            print_header("Create Custom Alert")
            last_alert = create_custom_alert(generator)
        
        elif choice == "7":
            clear_screen()
            print_header("Active Alerts")
            view_active_alerts(generator)
        
        elif choice == "8":
            clear_screen()
            print_header("Export Alert to JSON")
            export_alert_to_file(generator, last_alert)
        
        elif choice == "9":
            clear_screen()
            print_header("Cancel Alert")
            cancel_alert(generator)
        
        elif choice == "10":
            clear_screen()
            print_header("Sample Alert Types")
            show_sample_alerts()
        
        elif choice == "11":
            clear_screen()
            print_header("Thank You!")
            print("Thanks for using the EAS Weather Alert System Live Demo!")
            print(f"Total alerts created: {len(generator.alerts)}")
            print(f"Active alerts: {len(generator.get_active_alerts())}")
            print("\nGoodbye! 👋")
            break
        
        else:
            print_error("Invalid choice. Please try again.")
        
        print(f"\n{Color.YELLOW}Press Enter to continue...{Color.END}")
        input()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Color.YELLOW}Demo interrupted by user. Goodbye!{Color.END}")
        sys.exit(0)
    except Exception as e:
        print_error(f"An error occurred: {str(e)}")
        sys.exit(1)
