import streamlit as st
import data
import os
import pandas as pd
import time
import random

# --- 1. APP CONFIGURATION ---
st.set_page_config(
    page_title="TransitPulse",
    page_icon="🚆",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. CUSTOM CSS (Dark Mode & Clean UI) ---
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp { background-color: #0E1117; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
st.sidebar.title("TransitPulse ⚡")
st.sidebar.markdown("### Integrated Urban Commute")
st.sidebar.write("---")

menu_choice = st.sidebar.radio(
    "Navigate",
    ["Home", "Route Planner", "Live Status", "Analytics", "About"]
)

st.sidebar.write("---")
st.sidebar.caption("v1.0.0 | Developer Build")

# --- 4. PAGE ROUTING LOGIC ---

# === HOME PAGE ===
if menu_choice == "Home":
    # Header Section
    col1, col2 = st.columns([1.2, 1], gap="medium")

    with col1:
        st.title("🚆 TransitPulse")
        st.subheader("Mumbai's Smartest Commute Companion")
        st.markdown("##### *Stop guessing. Start moving.*")
        
        st.write("""
        TransitPulse integrates Metro, Local Trains, and Buses into a single, 
        intelligent network using real-time data.
        
        **Why use this?**
        * ⚡ **Smart Switching:** Real-time rerouting when trains are delayed.
        * 💰 **Cost Optimization:** Find the cheapest way to travel.
        * 👥 **Crowd Analysis:** Live density updates for safe travel.
        """)
        
        st.write("") # Spacer
        if st.button("Start Your Journey 🚀", use_container_width=True):
            st.toast("Redirecting to Route Planner...")
            
    with col2:
        # Image Handling (Looks for p1.png in images folder)
        image_path = "TransitPulse/images/p1.png"
        if os.path.exists(image_path):
            st.image(image_path, caption="Seamless Connectivity", use_container_width=True)
        else:
            st.warning("⚠️ Image 'images/p1.png' not found. Please generate and add it.")

    # Statistics Section (Fake Data for Dashboard Feel)
    st.markdown("---")
    st.subheader("System Metrics")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric(label="Active Routes", value="12", delta="Western Line")
    m2.metric(label="Users Online", value="1,240", delta="+8%")
    m3.metric(label="Server Status", value="Stable", delta_color="normal")
    m4.metric(label="Avg Commute Saved", value="15 min", delta="High Impact")

# === PLACEHOLDERS (We will build these later) ===
elif menu_choice == "Route Planner":
    st.title("🗺️ Route Planner")
    st.caption("AI-Powered Multi-Modal Transit Search")
    
    # 1. INPUT SECTION
    st.markdown("""
    <style>
    .stSelectbox { border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        start = st.selectbox("📍 Start Location", data.LOCATIONS)
    with col2:
        end = st.selectbox("🏁 Destination", data.LOCATIONS, index=1)

    st.write("") # Spacer
    
    # 2. SEARCH BUTTON LOGIC
    if st.button("Find Best Route 🔍", use_container_width=True):
        
        # Edge Case: Same Station
        if start == end:
            st.warning("⚠️ Start and Destination cannot be the same!")
        
        else:
            # Loading Effect (Fake AI Processing)
            with st.spinner(f"Analyzing routes between {start} and {end}..."):
                time.sleep(1.2) # 1.2 second ka drama
            
            # --- PATHFINDING ALGORITHM ---
            found_route = None
            route_type = None # "Direct" or "Via"

            # A. CHECK DIRECT ROUTE
            if start in data.TRANSPORT_NETWORK and end in data.TRANSPORT_NETWORK[start]:
                found_route = data.TRANSPORT_NETWORK[start][end]
                route_type = "Direct"

            # B. CHECK "VIA DADAR" (Smart Fallback)
            # Logic: Start -> Dadar -> End (Only if direct fails)
            elif "Dadar" in data.TRANSPORT_NETWORK.get(start, {}) and end in data.TRANSPORT_NETWORK.get("Dadar", {}):
                leg1 = data.TRANSPORT_NETWORK[start]["Dadar"]
                leg2 = data.TRANSPORT_NETWORK["Dadar"][end]
                
                found_route = {
                    "mode": f"{leg1['mode']} ➝ Switch ➝ {leg2['mode']}",
                    "time": leg1['time'] + leg2['time'] + 15, # 15 min buffer
                    "cost": leg1['cost'] + leg2['cost'],
                    "via": "Dadar"
                }
                route_type = "Via"
            
            # --- DISPLAY RESULTS ---
            
            if found_route:
                # 1. Comparison Logic (Uber/Ola vs Public Transport)
                cab_time = max(10, found_route['time'] - 15) # Cab is slightly faster
                cab_cost = found_route['cost'] * 15 # Cab is WAY more expensive
                savings = cab_cost - found_route['cost']

                # 2. Success Banner
                if route_type == "Direct":
                    st.success(f"✅ Best Route Found: {start} ➝ {end}")
                else:
                    st.warning(f"⚠️ No Direct Route. Going via {found_route['via']} is best.")

                # 3. Main Metric Cards
                c1, c2, c3 = st.columns(3)
                c1.metric("🚆 Mode", found_route['mode'])
                c2.metric("⏱️ Duration", f"{found_route['time']} mins", delta=f"{cab_time} min by Cab", delta_color="inverse")
                c3.metric("💰 Cost", f"₹{found_route['cost']}", delta=f"Save ₹{savings}", delta_color="normal")
                
                st.write("---")
                
                # 4. Detailed Breakdown (Expansion)
                with st.expander("📊 View Cost Analysis (vs Private Taxi)"):
                    st.write(f"**Why take Public Transport?**")
                    st.write(f"- 🚆 **TransitPulse Route:** ₹{found_route['cost']} (Time: {found_route['time']} min)")
                    st.write(f"- 🚖 **Uber/Ola Estimate:** ₹{cab_cost} (Time: {cab_time} min)")
                    st.progress(found_route['cost']/cab_cost, text="Cost Efficiency Score: 95%")

                # 5. GOOGLE MAPS DEEP LINK (The Real Utility)
                st.write("")
                # URL Encode logic manually for simple cities
                gmaps_url = f"https://www.google.com/maps/dir/?api=1&origin={start}+Station,Mumbai&destination={end}+Station,Mumbai&travelmode=transit"
                
                st.markdown(f"""
                <a href="{gmaps_url}" target="_blank">
                    <button style='width: 100%; background-color: #4CAF50; color: white; padding: 10px 24px; border: none; border-radius: 4px; cursor: pointer; font-size: 16px;'>
                        Open Live Navigation in Google Maps 🗺️
                    </button>
                </a>
                """, unsafe_allow_html=True)
                
            else:
                # Agar koi rasta na mile
                st.error(f"❌ Route not found in database.")
                st.info("Try connecting via major hubs like Dadar, Andheri or Kurla.")
                
                # Still show Google Maps button just in case
                gmaps_url = f"https://www.google.com/maps/dir/?api=1&origin={start}+Station,Mumbai&destination={end}+Station,Mumbai&travelmode=transit"
                st.link_button("Check Google Maps directly ↗️", gmaps_url)

elif menu_choice == "Live Status":
    st.title("📡 Live Network Status")
    
    # 1. Top Filters (Just like mIndicator)
    col1, col2, col3 = st.columns(3)
    with col1:
        line_filter = st.selectbox("Select Line", ["Western Line", "Central Line", "Metro One"])
    with col2:
        st.write("") # Spacer
        st.write("") # Spacer
        if st.button("🔄 Refresh Feed"):
            st.toast("Syncing with Railway Server...")
            st.rerun()

    st.write("---")

    # 2. Get Data specific to the line
    train_data = data.get_schedule(line_filter)
    
    # 3. Display Header
    st.subheader(f"{line_filter} - Live Board")
    
    # 4. Loop through specific trains
    for t in train_data:
        # Visual Styling
        if "AC" in t["Type"]:
            badge_color = "blue"
            icon = "❄️"
        elif "Fast" in t["Type"]:
            badge_color = "red"
            icon = "⚡"
        elif "Metro" in t["Type"]:
            badge_color = "orange"
            icon = "🚇"
        else:
            badge_color = "green"
            icon = "🐢"

        # Status Color
        if "Cancelled" in t["Status"]:
            stat_color = "red"
        elif "Delayed" in t["Status"]:
            stat_color = "orange"
        else:
            stat_color = "green"

        # The Card UI
        with st.container():
            c1, c2, c3, c4 = st.columns([2.5, 1, 1.5, 1])
            c1.markdown(f"**{icon} {t['Train']}**")
            c2.write(f"🕒 {t['Time']}")
            c3.markdown(f":{stat_color}[{t['Status']}]")
            c4.write(f"📍 {t['PF']}")
            
            # Crowd Progress Bar
            st.progress(t['Crowd'], text=f"Crowd Density: {t['Crowd']}%")
            st.divider()
elif menu_choice == "Analytics":
    st.title("📊 Network Analytics")
    
    # 1. Map Visualization
    st.subheader("📍 Live Station Density")
    
    # Data ko DataFrame (Table) mein convert karna padta hai map ke liye
    map_data = pd.DataFrame.from_dict(data.STATION_COORDS, orient='index', columns=['lat', 'lon'])
    
    # Ye ek line ka code poora map bana dega!
    st.map(map_data, zoom=10)
    
    # 2. Charts
    st.write("---")
    st.subheader("📈 Peak Hours Traffic")
    
    # Fake data chart ke liye
    chart_data = pd.DataFrame({
        "Station": ["Borivali", "Andheri", "Dadar", "Churchgate"],
        "Footfall": [4500, 8000, 6200, 3100]
    })
    
    # Bar Chart dikhana
    st.bar_chart(chart_data.set_index("Station"))

elif menu_choice == "About":
    st.title("👨‍💻 About The Project")
    
    # 1. Profile Card (Photo + Socials)
    col1, col2 = st.columns([1, 2])
    with col1:
        # TERA PHOTO LOGIC (p2.jpg)
        image_path = "TransitPulse/images/p2.jpg"
        
        if os.path.exists(image_path):
            # Photo thoda bada aur center mein achha lagega
            st.image(image_path, width=180, caption="Sahil Tiwari")
        else:
            # Agar naam galat hua toh error na aaye, bas text dikhe
            st.error("⚠️ 'p2.jpg' not found in images folder.")
            st.write("Sahil Tiwari")
            
        st.markdown("### Sahil Tiwari")
        st.caption("Full Stack Developer | IT Student")
        
        # Social Links (Clean Buttons)
        st.markdown("""
        <div style="display: flex; gap: 10px;">
            <a href="https://www.linkedin.com/in/sahil-tiwari-33715433b/" target="_blank">
                <button style="padding:5px 10px; border-radius:5px; border:none; background:#0077B5; color:white;">LinkedIn</button>
            </a>
            <a href="https://github.com/lamesahil" target="_blank">
                <button style="padding:5px 10px; border-radius:5px; border:none; background:#333; color:white;">GitHub</button>
            </a>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.info("Built for **Smart City Innovation** using Python & Streamlit.")
        st.write("---")
        
        # 2. The "Why" Story (Exam Incident)
        st.subheader("💡 Why I Built TransitPulse?")
        st.markdown("""
        > *"Necessity is the mother of invention."*
        
        This project was born out of a personal struggle. On the day of my **Final Semester Exam**, 
        I took the usual **Bus 461** from Thane to Borivali. Halfway through, I got stuck in massive traffic at Jogeshwari Road.
        
        I panicked. I needed to switch to Metro or Train immediately, but switching apps (Google Maps -> mIndicator -> Chalo App) 
        took valuable time. I barely made it to the exam hall.
        
        That day, I realized Mumbai needs a **Unified Dashboard**—one app that tells you:
        * *"Bus stuck? Take the Metro."*
        * *"Train delayed? Take a shared Auto."*
        
        **TransitPulse is that solution.**
        """)

    # 3. Technical Architecture
    st.write("---")
    with st.expander("🛠️ How It Works (Architecture)"):
        st.write("""
        1.  **Graph Algorithms:** The app treats stations as 'Nodes' and routes as 'Edges'. It calculates the shortest path using a weighted graph system.
        2.  **Dynamic Simulation:** Since official APIs are restricted, I built a simulation engine that mimics real-time train schedules based on peak/non-peak hours.
        3.  **Data Visualization:** Used `Pandas` and `Streamlit Map` to render geospatial data for station density.
        """)

    # 4. Future Scope
    with st.expander("🚀 Future Scope & Roadmap"):
        st.write("""
        This is currently a **Beta Version (MVP)**. The future roadmap includes:
        * **Live GPS Integration:** Replace simulation with real-time GTFS data from Railways.
        * **Ticket Booking:** Integrated QR-code ticketing for Metro & Local trains.
        * **Crowd Prediction AI:** Using Machine Learning to predict rush hours based on historical data.
        """)

    # 5. Contact Footer

    st.success("📫 **Get in Touch:** iamsahilt20@gmail.com | Insta: @lamesahil")

