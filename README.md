# 🚆 TransitPulse - Mumbai's Smartest Commute Companion

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31-FF4B4B)
![Status](https://img.shields.io/badge/Status-Beta-orange)

**TransitPulse** is a unified urban mobility dashboard designed to solve the fragmented public transport problem in Mumbai. It integrates Local Trains, Metro, and Buses into a single intelligent interface.

---

## 💡 The Story Behind The Code

> *"Necessity is the mother of invention."*

On the day of my **Final Semester Exam**, I took the usual **Bus 461** from Thane to Borivali. Halfway through, I got stuck in massive traffic at Ghodbunder Road. I panicked. I needed to switch to Metro or Train immediately, but switching between multiple apps (Google Maps, m-Indicator, Chalo App) took valuable time. I barely made it to the exam hall.

That day, I realized Mumbai needs a **Unified Dashboard**—one app that tells you:
* *"Bus stuck? Take the Metro."*
* *"Train delayed? Take a shared Auto."*

**TransitPulse is that solution.**

---

## 🚀 Key Features

### 🗺️ 1. Multi-Modal Route Planner
- **Smart Pathfinding:** Uses Graph Algorithms (Adjacency Matrix) to find the best route.
- **Cost Comparison:** Compares Public Transport cost vs. Private Cabs (Uber/Ola).
- **"Via Dadar" Logic:** Automatically suggests hub-based routing if direct trains aren't available.

### 📡 2. Live Status Simulation
- **Dynamic Scheduling:** A simulation engine that generates realistic train schedules relative to your current time.
- **Real-time Volatility:** Mimics real-world delays and cancellations using randomized logic.

### 📊 3. Network Analytics
- **Geospatial Visualization:** Uses `Pandas` and Streamlit's Map component to visualize station density.
- **Crowd Heatmaps:** Data-driven insights into high-traffic zones.

### 🔗 4. Deep Linking
- **Google Maps Bridge:** One-click integration to open the calculated route directly in Google Maps for live navigation.

---

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/) (Python Framework)
* **Backend Logic:** Python (Graph Theory, Datetime Simulation)
* **Data Processing:** Pandas (DataFrames)
* **Visualization:** Streamlit Map & Metric Components

---

## 📂 Project Structure

```bash
TransitPulse/
├── main.py           # The Application Interface (View & Controller)
├── data.py           # The Database & Logic Store (Model)
├── requirements.txt  # Dependencies list
├── README.md         # Project Documentation
└── images/           # Static Assets
    ├── p1.png        # Home Page Hero Image
    └── p2.jpg        # Developer Profile Picture
