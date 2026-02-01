import requests
from skyfield.api import load, EarthSatellite

def load_tle_group(url):
    r = requests.get(url)
    lines = r.text.splitlines()
    sats = []

    ts = load.timescale()

    for i in range(0, len(lines) - 2, 3):
        name = lines[i].strip()
        line1 = lines[i + 1]
        line2 = lines[i + 2]

        try:
            sats.append(EarthSatellite(line1, line2, name, ts))
        except:
            pass

    return sats

def load_satellite(name):
    url = "https://celestrak.org/NORAD/elements/stations.txt"
    sats = load_tle_group(url)

    for sat in sats:
        if name.upper() in sat.name.upper():
            return sat

    return None

def load_debris():
    # Real debris groups
    debris_urls = [
        "https://celestrak.org/NORAD/elements/cosmos-2251-debris.txt",
        "https://celestrak.org/NORAD/elements/iridium-33-debris.txt"
    ]

    debris_objects = []
    for url in debris_urls:
        debris_objects.extend(load_tle_group(url))

    return debris_objects