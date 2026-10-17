dortmund_events = {
    # Night of Museums (Dortmunder Museumsnacht) - 19th September 2026
    "Dortmunder U - Museunacht: Rooftop Beats & Immersive Art": "2026-09-19",
    "German Football Museum - Night of Museums: Fan Heritage & Trophy Tours": "2026-09-19",
    "Museum Ostwall - Museumsnacht: Fluxus Performance & Interactive Workshops": "2026-09-19",
    "DASA Working World Exhibition - Museumsnacht: High-Voltage Science Show": "2026-09-19",
    "LWL-Museum Zeche Zollern - Museumsnacht: Mining Heritage & Light Installations": "2026-09-19",
    "Museum für Kunst und Kulturgeschichte (MKK) - Museumsnacht: Midnight Concert": "2026-09-19",
    "Brauerei-Museum Dortmund - Museumsnacht: Craft History & Tasting Tour": "2026-09-19",
    "Kokerei Hansa - Museumsnacht: Coking Plant Illumination & Night Walk": "2026-09-19",
    "Naturmuseum Dortmund - Museumsnacht: Prehistoric Dioramas by Torchlight": "2026-09-19",
    "St. Reinoldi - Museumsnacht: Steeple Ascent & Organ Soundscape": "2026-09-19",

    # Other non-Museumsnacht events in Dortmund for calendar contrast
    "Westfalenpark - Juicy Beats Festival": "2026-07-24",
    "Signal Iduna Park - BVB Bundesliga Season Kickoff": "2026-08-22",
    "Westfalenhallen - Mayday Electronic Music Festival": "2026-04-30",
    "Hansaplatz - Dortmund International Christmas Market": "2026-11-26",
}

for event, date in dortmund_events.items():
  if date=="2026-09-19" and "Museumsnacht" in event:
    print(event)
  