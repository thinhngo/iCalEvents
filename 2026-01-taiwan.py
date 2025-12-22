from datetime import datetime

def create_13_day_taiwan_itinerary():
    # Timezone for Taiwan
    tz = "Asia/Taipei"
    
    # Complete 13-Day Event List (Jan 27 - Feb 8)
    # Format: [Summary, Start Time, End Time, Location, Description]
    events = [
        ["🏠 Arrival: Base Camp Taipei", "2026-01-27 09:00", "2026-01-27 12:00", "Xinyi District, Taipei", "LAX group arrives. Base camp for both groups. Focus on recovery and baby supplies."],
        ["🍽️ Lunch: Din Tai Fung (Taipei 101)", "2026-01-27 13:00", "2026-01-27 15:00", "Taipei 101, B1", "Highly accessible branch. Best nursing rooms located in the 101 basement mall."],
        ["🌳 Daan Forest Park Stroll", "2026-01-27 15:30", "2026-01-27 17:00", "Daan District, Taipei", "100% flat and paved. Perfect for light exercise to combat jet lag for the LAX group."],
        ["🏮 Dihua St & Longshan Temple", "2026-01-28 10:00", "2026-01-28 16:00", "Datong & Wanhua District", "Lunar New Year market + spiritual visit. Use side ramps at Longshan for strollers/seniors."],
        ["♨️ Beitou Hot Springs & Thermal Valley", "2026-01-29 10:00", "2026-01-29 14:00", "Beitou District", "Book a private family hot spring room. Thermal Valley is a flat paved walk nearby."],
        ["🌊 Yehliu & Jiufen (No-Stairs Hack)", "2026-01-30 09:00", "2026-01-30 17:30", "North Coast", "Driver drop-off at Shengping Theater for Jiufen to avoid the 200+ central stairs."],
        ["🌸 Yangmingshan Cherry Blossoms", "2026-01-31 10:00", "2026-01-31 13:00", "Lane 42, Pingjing St", "View early blooms from flat roadside; no steep hiking required for senior group members."],
        ["🚄 HSR to Taichung (Car 7 Priority)", "2026-02-01 11:00", "2026-02-01 12:00", "Taipei Main Station", "Book priority Car 7 (extra space, near elevators). Ticket booking opens 28 days prior."],
        ["🌅 Gaomei Wetlands Sunset", "2026-02-01 16:30", "2026-02-01 18:30", "Qingshui, Taichung", "100% flat wooden boardwalk nature walk over marshes. Stroller friendly."],
        ["⛴️ Sun Moon Lake Private Charter", "2026-02-02 10:00", "2026-02-02 15:00", "Shuishe Pier", "Private boat avoids ramps/crowds. Flat food street at Ita Thao for aboriginal snacks."],
        ["🎨 Taichung: Rainbow Village & Flower Park", "2026-02-03 10:00", "2026-02-03 15:00", "Nantun & Houli", "Colorful accessible art spot + expansive flat flower park. Senior citizen and baby friendly."],
        ["🍦 Miyahara Ice Cream & HSR Return", "2026-02-04 11:00", "2026-02-04 15:00", "Central Taichung", "Stunning historic building (fully accessible). Return to Taipei via HSR after."],
        ["🚠 Maokong Gondola & Mountain Tea", "2026-02-05 14:00", "2026-02-05 18:00", "Wenshan District", "Glass-floor 'Crystal' cabins. Tea at Yaoyue Tea House (accessible with mountain views)."],
        ["🏛️ National Palace Museum", "2026-02-06 10:00", "2026-02-06 14:00", "Shilin District", "Senior-paced visit. Use museum high-capacity elevators and baby nursing rooms."],
        ["🛒 Nanmen Market & Final Feast", "2026-02-07 10:00", "2026-02-07 18:00", "Taipei City", "New market shopping (AM) + Farewell Din Tai Fung (Xinyi A13 Branch) for dinner."],
        ["🍽️ Farewell Dinner: Din Tai Fung (A13)", "2026-02-07 18:30", "2026-02-07 20:30", "Xinyi A13 Mall", "Final group dinner. This mall has the best nursing/changing facilities in the city."],
        ["✈️ Departure Logistics", "2026-02-08 09:00", "2026-02-08 14:00", "Taoyuan Airport (TPE)", "Private van transfer to TPE terminal for both groups. Coordinate based on flight times."],
        ["🔔 REMINDER: LAX Flight Check", "2025-12-20 09:00", "2025-12-20 10:00", "Booking Phase", "Ensure LAX group departs night of Jan 25 (local time) to arrive Jan 27 morning."],
        ["🔔 REMINDER: HSR Booking (28 Days Out)", "2025-12-31 09:00", "2025-12-31 10:00", "Online", "Book Car 7 for the Feb 1 and Feb 4 HSR journeys exactly 28 days in advance."]
    ]

    # Generating the ICS file content
    ics_content = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Travel Buddy//13 Day Taiwan Family Trip//EN",
        "METHOD:PUBLISH"
    ]

    for title, start, end, loc, desc in events:
        s = datetime.strptime(start, "%Y-%m-%d %H:%M").strftime("%Y%m%dT%H%M%S")
        e = datetime.strptime(end, "%Y-%m-%d %H:%M").strftime("%Y%m%dT%H%M%S")
        
        # Escaping special characters for ICS format
        desc_esc = desc.replace(",", "\\,").replace("\n", "\\n")
        loc_esc = loc.replace(",", "\\,")
        
        ics_content.extend([
            "BEGIN:VEVENT",
            f"SUMMARY:{title}",
            f"DTSTART;TZID={tz}:{s}",
            f"DTEND;TZID={tz}:{e}",
            f"LOCATION:{loc_esc}",
            f"DESCRIPTION:{desc_esc}",
            "STATUS:CONFIRMED",
            "BEGIN:VALARM",
            "TRIGGER:-PT30M",
            "ACTION:DISPLAY",
            "DESCRIPTION:Reminder",
            "END:VALARM",
            "END:VEVENT"
        ])

    ics_content.append("END:VCALENDAR")
    
    # Save to file
    with open("Taiwan_13Day_Family_Trip.ics", "w", encoding="utf-8") as f:
        f.write("\n".join(ics_content))
    
    print("Success: 'Taiwan_13Day_Family_Trip.ics' has been generated.")

if __name__ == "__main__":
    create_13_day_taiwan_itinerary()