# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.

def print_star_names():
    for star in targets.keys():
        print(star) 
print(print_star_names())
# 2) Write a function that uses a loop to print the name of each star with its spectral type.

def print_star_spectral_types():
    for star, info in targets.items():
        print(f"{star}: {info['Spectral Type']}")
print(print_star_spectral_types())  
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.

def find_bright_stars():
    bright_stars = []
    for star, info in targets.items():
        if info["Magnitude"] > 0.1:
            bright_stars.append(star)
    return bright_stars
print(find_bright_stars())

# 5) Write a function that finds the brightest star whose Declination is closest to 20°.

def find_brightest_near_declination(target_dec=20):
    closest_star = None
    closest_dec_diff = float('inf')
    brightest_magnitude = float('inf')
    
    for star, info in targets.items():
        dec_str = info["Dec"]
        dec_value = float(dec_str.split('°')[0].replace('+', '').replace('−', '-'))
        dec_diff = abs(dec_value - target_dec)
        
        if dec_diff < closest_dec_diff or (dec_diff == closest_dec_diff and info["Magnitude"] < brightest_magnitude):
            closest_dec_diff = dec_diff
            brightest_magnitude = info["Magnitude"]
            closest_star = star
            
    return closest_star

print(find_brightest_near_declination())

# 6) What is your favorite constellation? orions belt
