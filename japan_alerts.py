from datetime import datetime, timedelta

# Content for the Booking Reminders ICS file
# We use \\r\\n for strict ICS compliance
ics_content = "BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//Travel Buddy//Japan Booking Reminders PST//EN\nCALSCALE:GREGORIAN\nMETHOD:PUBLISH\n"


def create_reminder(summary, description, start_dt):
    # Format dates for ICS: YYYYMMDDTHHMMSS
    fmt = "%Y%m%dT%H%M%S"
    end_dt = start_dt + timedelta(hours=1)

    # CRITICAL FIX: Replace actual newlines with escaped \\n characters
    # This prevents the file from breaking when imported
    safe_description = description.replace("\n", "\\n")

    return f"""BEGIN:VEVENT
SUMMARY:🔔 {summary}
DESCRIPTION:{safe_description}
DTSTART:{start_dt.strftime(fmt)}
DTEND:{end_dt.strftime(fmt)}
STATUS:CONFIRMED
BEGIN:VALARM
TRIGGER:-PT15M
DESCRIPTION:Booking Reminder
ACTION:DISPLAY
END:VALARM
END:VEVENT
"""


# Current simulated time: Dec 4, 2025.
# These dates are calculated for PST (UTC-8)

reminders = [
    {
        "task": "URGENT: Book teamLab Planets & Tempura Endo",
        "desc": "Check IMMEDIATELY. These booking windows are already open.",
        "date": datetime(2025, 12, 5, 9, 0),  # Tomorrow morning
    },
    {
        "task": "Book Odakyu Romancecar (Front Seats)",
        "desc": "Release: Dec 15, 10:00 AM JST.\nPST Time: Dec 14, 5:00 PM.\nLog in 5 mins early!",
        "date": datetime(2025, 12, 14, 17, 0),  # Dec 14, 5:00 PM PST
    },
    {
        "task": "Book Shinkansen: Tokyo -> Kyoto",
        "desc": "Release: Dec 17, 10:00 AM JST.\nPST Time: Dec 16, 5:00 PM.\nBook 'Oversized Baggage' seat if needed.",
        "date": datetime(2025, 12, 16, 17, 0),  # Dec 16, 5:00 PM PST
    },
    {
        "task": "Book Cup Noodles Museum Osaka",
        "desc": "Check for 'My Cupnoodles Factory' slots. Release times vary, check now and daily.",
        "date": datetime(2025, 12, 5, 9, 30),  # Check ASAP
    },
    {
        "task": "Book Shinkansen: Kyoto -> Tokyo",
        "desc": "Release: Dec 21, 10:00 AM JST.\nPST Time: Dec 20, 5:00 PM.",
        "date": datetime(2025, 12, 20, 17, 0),  # Dec 20, 5:00 PM PST
    },
    {
        "task": "Book Shibuya Sky (Sunset Slot)",
        "desc": "Release: Jan 7, Midnight JST (14 days prior).\nPST Time: Jan 6, 7:00 AM.\nSunset slots vanish in minutes.",
        "date": datetime(2026, 1, 6, 7, 0),  # Jan 6, 7:00 AM PST
    },
]

for item in reminders:
    ics_content += create_reminder(item["task"], item["desc"], item["date"])

ics_content += "END:VCALENDAR"

filename = "Japan_Booking_Alerts_PST_Fixed.ics"
with open(filename, "w", encoding="utf-8") as f:
    f.write(ics_content)

print(f"Successfully created {filename} (Fixed for Import)")
