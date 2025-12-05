from datetime import datetime

# --- ICS File Header ---
ics_content = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Travel Buddy//Japan Itinerary 2026 Final (Osaka Back)//EN
CALSCALE:GREGORIAN
METHOD:PUBLISH
"""


def create_event(summary, description, location, start_dt, end_dt):
    fmt = "%Y%m%dT%H%M%S"
    return f"""BEGIN:VEVENT
SUMMARY:{summary}
DESCRIPTION:{description}
LOCATION:{location}
DTSTART:{start_dt.strftime(fmt)}
DTEND:{end_dt.strftime(fmt)}
STATUS:CONFIRMED
END:VEVENT
"""


year = 2026
events = [
    # --- KYOTO BASE (Jan 17-21) ---
    {
        "summary": "Shinkansen to Kyoto",
        "desc": "Travel to Kyoto. Dinner at Pontocho Alley.",
        "loc": "Kyoto Station",
        "start": datetime(year, 1, 17, 10, 0),
        "end": datetime(year, 1, 17, 13, 0),
    },
    {
        "summary": "Nara Day Trip (Sunday)",
        "desc": "Train to Nara (~45 min). Nakatanidou Mochi Open Today! Feed deer.",
        "loc": "Nara Park",
        "start": datetime(year, 1, 18, 10, 0),
        "end": datetime(year, 1, 18, 15, 0),
    },
    # --- OSAKA DAY (Monday) ---
    {
        "summary": "Cup Noodles Museum Osaka Ikeda",
        "desc": "Make your own Cup Noodle! (Closed Tue, so go Mon).",
        "loc": "Cup Noodles Museum Osaka Ikeda",
        "start": datetime(year, 1, 19, 10, 30),
        "end": datetime(year, 1, 19, 12, 30),
    },
    {
        "summary": "Umeda Sky Building",
        "desc": "Floating Garden Observatory.",
        "loc": "Umeda Sky Building",
        "start": datetime(year, 1, 19, 14, 0),
        "end": datetime(year, 1, 19, 15, 30),
    },
    {
        "summary": "Dotonbori Food Crawl",
        "desc": "Takoyaki, Kushikatsu, and Glico Man sign.",
        "loc": "Dotonbori, Osaka",
        "start": datetime(year, 1, 19, 16, 30),
        "end": datetime(year, 1, 19, 20, 0),
    },
    # --------------------------
    {
        "summary": "Arashiyama & Tempura Endo (Tuesday)",
        "desc": "Monkey Park & Bamboo. Lunch reservation at Tempura Endo.",
        "loc": "Arashiyama Bamboo Forest",
        "start": datetime(year, 1, 20, 8, 30),
        "end": datetime(year, 1, 20, 14, 0),
    },
    {
        "summary": "Fushimi Inari Sunset",
        "desc": "Thousands of gates at sunset.",
        "loc": "Fushimi Inari Taisha",
        "start": datetime(year, 1, 20, 15, 30),
        "end": datetime(year, 1, 20, 17, 30),
    },
]

for event in events:
    ics_content += create_event(
        event["summary"], event["desc"], event["loc"], event["start"], event["end"]
    )

ics_content += "END:VCALENDAR"

filename = "Japan_Jan_2026_Final_With_Osaka.ics"
with open(filename, "w", encoding="utf-8") as f:
    f.write(ics_content)

print(f"Successfully created {filename}")
