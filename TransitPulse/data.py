import random
from datetime import datetime, timedelta

# 1. Locations (Same as before)
LOCATIONS = [
    "Borivali", "Andheri", "Dadar", "Churchgate", 
    "Ghatkopar", "Versova", "BKC", "Thane", "Kurla"
]

STATION_COORDS = {
    "Borivali": [19.2307, 72.8567],
    "Andheri": [19.1136, 72.8697],
    "Dadar": [19.0178, 72.8478],
    "Churchgate": [18.9322, 72.8264],
    "Ghatkopar": [19.0860, 72.9090],
    "Thane": [19.2183, 72.9781]
}

# --- 2. THE SMART SCHEDULE GENERATOR ---
def get_schedule(line_choice):
    current_time = datetime.now()
    trains = []
    
    # Configuration for each line
    if line_choice == "Central Line":
        base_route = "Thane -> CSMT"
        prefixes = ["T", "K", "TL", "A"] # Thane, Kalyan, Titwala, Ambernath
        types = ["Slow", "Fast"]
    elif line_choice == "Western Line":
        base_route = "Borivali -> Churchgate"
        prefixes = ["BO", "VR", "BY", "AC"] # Borivali, Virar, Bhayandar
        types = ["Fast", "Slow", "AC Fast"]
    else: # Metro
        base_route = "Versova -> Ghatkopar"
        prefixes = ["M"]
        types = ["Metro"]

    # Logic: Generate next 5 trains starting from NOW
    for i in range(5):
        # 1. Calculate Time: Har train 3-8 minute ke gap pe
        delta = (i * 5) + random.randint(2, 6) 
        train_time = current_time + timedelta(minutes=delta)
        time_str = train_time.strftime("%I:%M %p") # e.g., "02:30 PM"
        
        # 2. Randomize Details
        train_id = f"{random.choice(prefixes)}-{random.randint(10, 99)}"
        train_type = random.choice(types)
        
        # Thoda 'Reality' daalne ke liye
        status_options = ["On Time", "On Time", "On Time", "Delayed (3 min)"]
        status = random.choice(status_options)
        
        # 3. Build Data Object
        train_obj = {
            "Train": f"{train_id}: {base_route}",
            "Type": train_type,
            "Time": time_str, # Ye asli "Upcoming Time" hai!
            "Status": status,
            "PF": f"PF-{random.randint(1, 6)}",
            "Crowd": random.randint(40, 100)
        }
        trains.append(train_obj)
        
    return trains

# Traffic (Same as before)
def get_traffic_status():
    traffic_levels = ["Clear", "Moderate", "Heavy", "Jam"]
    return random.choice(traffic_levels)

# Network Data for Route Planner (Same as before - Isse delete mat karna!)
# --- NETWORK DATABASE (Updated for Connectivity) ---
TRANSPORT_NETWORK = {
    "Borivali": {
        "Andheri": {"mode": "Train (Fast)", "time": 25, "cost": 10},
        "Dadar": {"mode": "Train (Fast)", "time": 40, "cost": 15},
        "Churchgate": {"mode": "Train (Fast)", "time": 55, "cost": 20},
        "Thane": {"mode": "Bus 461 (TMT)", "time": 90, "cost": 45} # Direct Bus
    },
    "Andheri": {
        "Borivali": {"mode": "Train (Fast)", "time": 25, "cost": 10},
        "Dadar": {"mode": "Train (Fast)", "time": 20, "cost": 10},
        "Versova": {"mode": "Metro", "time": 15, "cost": 20},
        "Ghatkopar": {"mode": "Metro", "time": 25, "cost": 30},
        "Churchgate": {"mode": "Train (Slow)", "time": 45, "cost": 15}
    },
    "Dadar": { # THE HUB (Sab yahan aate hain)
        "Borivali": {"mode": "Train (Fast)", "time": 40, "cost": 15},
        "Andheri": {"mode": "Train (Fast)", "time": 20, "cost": 10},
        "Churchgate": {"mode": "Train (Slow)", "time": 20, "cost": 10},
        "Kurla": {"mode": "Train (Slow)", "time": 15, "cost": 10},
        "Thane": {"mode": "Train (Fast)", "time": 40, "cost": 15},
        "Ghatkopar": {"mode": "Train (Slow)", "time": 25, "cost": 10}
    },
    "Ghatkopar": {
        "Andheri": {"mode": "Metro", "time": 25, "cost": 30},
        "Dadar": {"mode": "Train (Slow)", "time": 25, "cost": 10},
        "Thane": {"mode": "Train (Slow)", "time": 20, "cost": 10},
        "Versova": {"mode": "Metro", "time": 40, "cost": 40}
    },
    "Thane": {
        "Dadar": {"mode": "Train (Fast)", "time": 40, "cost": 15},
        "Kurla": {"mode": "Train (Slow)", "time": 30, "cost": 15},
        "Borivali": {"mode": "Bus 461 (BEST)", "time": 90, "cost": 45}, # Tera Favorite Route
        "Ghatkopar": {"mode": "Train (Slow)", "time": 20, "cost": 10}
    },
    "Churchgate": {
        "Dadar": {"mode": "Train (Fast)", "time": 20, "cost": 10},
        "Borivali": {"mode": "Train (Fast)", "time": 55, "cost": 20},
        "Andheri": {"mode": "Train (Fast)", "time": 45, "cost": 15}
    },
    "Kurla": {
        "Dadar": {"mode": "Train (Slow)", "time": 15, "cost": 10},
        "Thane": {"mode": "Train (Slow)", "time": 30, "cost": 15},
        "BKC": {"mode": "Auto/Bus", "time": 15, "cost": 20}
    },
    "Versova": {
        "Andheri": {"mode": "Metro", "time": 15, "cost": 20},
        "Ghatkopar": {"mode": "Metro", "time": 40, "cost": 40}
    },
    "BKC": {
        "Kurla": {"mode": "Bus", "time": 20, "cost": 15},
        "Andheri": {"mode": "Bus", "time": 45, "cost": 25}
    }
}
# (Note: Upar wala Transport Network pura copy kar lena purane code se)