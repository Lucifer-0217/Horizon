# 🌌 **Horizon — Advanced Phone Intelligence & Tracking System**

### *Developed by [Amit Kasbe](mailto:amitkasbe2020@gmail.com)*

> “Because every number tells a story — Horizon helps you see it.”

---

## 🛰️ Overview

**Horizon** is an **API-powered phone number intelligence and live tracking framework** designed to provide **real-time insights**, **data visualization**, and **geographical mapping** of phone numbers with exceptional precision.

It integrates **multiple data APIs** to fetch, correlate, and display detailed phone intelligence such as:

* Geographic location
* Service provider
* Linked social media profiles
* Network tower information
* Associated numbers
* Profile photos
* Live movement simulations

Horizon bridges the gap between **data aggregation**, **analysis**, and **visual presentation**, giving users a clear view of a phone number’s digital footprint.

---

## ⚡ Core Functionalities

### 1. 📞 **Phone Number Intelligence**

* Retrieve key details like:

  * Country and region
  * Time zone
  * Network carrier/service provider
* Uses reliable number validation and lookup APIs.
* Ideal for telecom research, fraud analysis, and OSINT workflows.

---

### 2. 🌐 **Social Media Profile Integration**

* Uses social lookup APIs to extract **linked profiles** associated with the target number.
* Returns platform name, username, profile URLs, and more.
* Supports multi-platform cross-referencing.

---

### 3. 🔗 **Associated Numbers Discovery**

* Finds **other numbers linked to the same identity** or registered data.
* Helps uncover relationships between entities or possible duplicates.
* Enables graph-style correlation analysis.

---

### 4. 🏗️ **Network Tower & Signal Insights**

* Retrieves the **most recent network tower** or last known cell ID used by the number.
* Displays tower coordinates and signal source area on the map.
* Can approximate coverage zone and triangulate general movement trends.

---

### 5. 🖼️ **Profile Photo Retrieval**

* Gathers **publicly available profile photos** via connected APIs.
* Supports image caching and preview through the dashboard or CLI output.
* Useful for identity matching and verification.

---

### 6. 🗺️ **Interactive Location Mapping**

* Built using **Folium** for interactive, draggable maps.
* Displays:

  * Number’s approximate location
  * Nearby towers or related numbers
  * Real-time simulation paths
* Generates `HTML` maps for direct visualization in browsers.

---

### 7. 📡 **Live Location Simulation**

* Simulates **continuous live movement** for demonstration and testing.
* Coordinates dynamically update on the map at fixed intervals.
* Can simulate speed, direction, and route variation for realism.

---

### 8. 🔁 **Continuous Tracking Mode**

* Runs in the background, periodically checking and updating coordinates.
* Logs each update with:

  * Timestamp
  * Latitude & Longitude
  * Distance moved
* Can export data to `.csv` for later analysis.

---

## ⚙️ Installation Guide

### 🧩 Step 1: Clone the Repository

```bash
git clone https://github.com/Lucifer-0217/Horizon.git
cd Horizon
```

---

### 🧱 Step 2: Set Up the Environment

Create and activate a virtual environment (recommended):

```bash
python -m venv venv
```

Activate it:

* **Windows:** `venv\Scripts\activate`
* **macOS/Linux:** `source venv/bin/activate`

Then install dependencies:

```bash
pip install -r requirements.txt
```

---

### 🔑 Step 3: Configure API Keys

Open `horizon.py` and replace placeholders with valid API keys:

```python
SOCIAL_MEDIA_API_KEY = "<Your Social Media API Key>"
ASSOCIATED_NUMBERS_API_KEY = "<Your Associated Numbers API Key>"
PROFILE_PHOTO_API_KEY = "<Your Profile Photo API Key>"
NETWORK_TOWER_API_KEY = "<Your Network Tower API Key>"
GOOGLE_MAPS_API_KEY = "<Your Google Maps API Key>"
```

Each key corresponds to a different lookup API:

| API                        | Purpose                    |
| -------------------------- | -------------------------- |
| **Social Media API**       | Fetches linked profiles    |
| **Associated Numbers API** | Finds related numbers      |
| **Profile Photo API**      | Retrieves user’s photo     |
| **Network Tower API**      | Gets tower and signal data |
| **Google Maps API**        | Provides map visualization |

---

## 🚀 Usage

Run Horizon from your terminal:

```bash
python horizon.py
```

### Horizon CLI Menu:

```plaintext
===================================
      HORIZON CLI INTERFACE
===================================
1. Track a phone number
2. Display the map
3. Start live tracking
4. Exit
Enter your choice (1/2/3/4):
```

### Menu Options

| Option                     | Description                                                   |
| -------------------------- | ------------------------------------------------------------- |
| **1. Track a Number**      | Input a number with country code to fetch intelligence.       |
| **2. Display the Map**     | Opens the generated interactive location map in your browser. |
| **3. Start Live Tracking** | Simulates or fetches real-time tracking updates.              |
| **4. Exit**                | Safely closes the CLI interface.                              |

---

## 🌍 Example Output

```plaintext
[+] Tracking Number: +1 202-555-0127
---------------------------------------
Carrier: Verizon Communications
Location: Washington D.C., United States
Time Zone: UTC-5
Tower ID: #3487 (Last Seen: 2 mins ago)
---------------------------------------
Linked Profiles:
  • Twitter: @john_doe
  • Instagram: johndoe_2025
---------------------------------------
Associated Numbers:
  • +1 202-555-0189
  • +1 202-555-0146
---------------------------------------
Map saved as: /maps/number_2025550127.html
```

---

## 🧠 Technical Stack

| Layer                  | Technology Used               |
| ---------------------- | ----------------------------- |
| **Core Language**      | Python                        |
| **Mapping Engine**     | Folium                        |
| **CLI Interface**      | Rich Text-based CLI           |
| **APIs**               | Custom OSINT & telecom APIs   |
| **Data Visualization** | HTML maps, CSV logs           |
| **Simulation Engine**  | Dynamic coordinate generation |

---

## 🧰 File Structure

```bash
Horizon/
├── horizon.py               # Main script / CLI interface
└── README.md                # Documentation
```

---

## 🧩 Troubleshooting

| Problem                  | Possible Cause                           | Solution                                                       |
| ------------------------ | ---------------------------------------- | -------------------------------------------------------------- |
| **Invalid API Response** | Incorrect API key or expired token       | Verify your credentials and renew key                          |
| **Map Not Loading**      | Missing Google Maps or Folium dependency | Reinstall dependencies using `pip install -r requirements.txt` |
| **No Location Data**     | Tower API timeout or missing data        | Retry or check your network connection                         |
| **Simulation Lag**       | Slow system or high update frequency     | Increase the interval between updates                          |

---

## 🤝 Contributing

We welcome contributions from the community!

**How to contribute:**

1. Fork the repository
2. Create a new branch:

   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit and push your changes
4. Open a Pull Request on GitHub 🚀

---

## 📜 License

This project is distributed under the **MIT License**.
You are free to use, modify, and share — with proper credit to the original author.

---

## 📬 Contact

For queries, collaborations, or reporting issues:
📧 **[amitkasbe2020@gmail.com](mailto:amitkasbe2020@gmail.com)**
🌐 GitHub: [Lucifer-0217](https://github.com/Lucifer-0217)

---

## 🌠 Vision

> *“Horizon is more than a tracker — it’s your digital window into location intelligence.”*
> — **Amit Kasbe**

Horizon is built to evolve into a **complete telecommunication intelligence framework**, combining multi-API precision, real-time visualization, and deep data relationships — empowering researchers, developers, and analysts to explore the unseen patterns of the connected world.


