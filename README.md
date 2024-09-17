# Horizon

**Horizon** is an advanced phone number tracking and location visualization tool developed by Amit Kasbe. This project seamlessly integrates multiple APIs to deliver comprehensive insights into phone numbers, including their social media profiles, associated numbers, network towers, and profile photos. Horizon also features continuous tracking and live location simulation, making it a versatile tool for modern needs.

## 🚀 Features

- **Phone Number Analysis**: Retrieve detailed information such as location, time zone, and service provider.
- **Social Media Profiles**: Access social media profiles linked to the phone number.
- **Associated Numbers**: Discover related phone numbers.
- **Network Tower Data**: Obtain information about the last network tower used.
- **Profile Photo Retrieval**: Get the profile photo associated with the phone number.
- **Interactive Location Mapping**: Visualize locations on an interactive map using Folium.
- **Live Location Simulation**: Simulate and track live location data.
- **Continuous Tracking**: Monitor and update the phone number’s location in real-time.

## ⚙️ Installation

To get started with Horizon, follow these simple steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Lucifer-0217/Horizon.git
   cd Horizon
   ```

2. **Set Up the Environment**:
   Create a virtual environment (recommended) and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Configure API Keys**:
   Replace placeholders in the script with your actual API keys:
   - `SOCIAL_MEDIA_API_KEY`
   - `ASSOCIATED_NUMBERS_API_KEY`
   - `PROFILE_PHOTO_API_KEY`
   - `NETWORK_TOWER_API_KEY`
   - `YOUR_GOOGLE_MAPS_API_KEY`

## 🎯 Usage

Launch the Horizon CLI interface with:
```bash
python horizon.py
```

### CLI Options

1. **Track a Phone Number**: Enter a phone number with the country code to retrieve detailed information and location.
2. **Display the Map**: View the location map of the tracked phone number.
3. **Start Live Tracking**: Track and display live location data for a specified duration.
4. **Exit**: Close the application.

## 📜 Example

```plaintext
Horizon CLI Menu
1. Track a phone number
2. Display the map
3. Start live tracking
4. Exit
Enter your choice (1/2/3/4):
```

## 🤝 Contributing

We welcome contributions to Horizon! To get involved:

1. **Fork the Repository**: Click "Fork" on GitHub to create your own copy of the repository.
2. **Create a Branch**: 
   ```bash
   git checkout -b feature/your-feature
   ```
3. **Implement Changes**: Add your feature or fix bugs.
4. **Commit Your Changes**:
   ```bash
   git add .
   git commit -m "Add feature or fix bug"
   ```
5. **Push to Your Fork**:
   ```bash
   git push origin feature/your-feature
   ```
6. **Open a Pull Request**: Submit a pull request on GitHub with details about your changes.

## 📝 License

This project is licensed under the [MIT License](LICENSE).

## 📬 Contact

For questions or feedback, please reach out to [Amit Kasbe](amitkasbe2020@gmail.com).
