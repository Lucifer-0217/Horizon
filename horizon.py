import os
import sys
import time
import random
import requests
import folium
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from colorama import Fore, init
from dotenv import load_dotenv
from googlemaps import Client as GoogleMapsClient
from googlemaps.exceptions import ApiError

# Initialize colorama
init(autoreset=True)

# Load environment variables
load_dotenv()

# Load API Keys securely
SOCIAL_MEDIA_API_KEY = os.getenv("SOCIAL_MEDIA_API_KEY")
ASSOCIATED_NUMBERS_API_KEY = os.getenv("ASSOCIATED_NUMBERS_API_KEY")
PROFILE_PHOTO_API_KEY = os.getenv("PROFILE_PHOTO_API_KEY")
NETWORK_TOWER_API_KEY = os.getenv("NETWORK_TOWER_API_KEY")
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

# Initialize Google Maps client safely
gmaps = None
if GOOGLE_MAPS_API_KEY:
    gmaps = GoogleMapsClient(key=GOOGLE_MAPS_API_KEY)
else:
    print(Fore.RED + "[-] Google Maps API key not found. Map features may not work properly.")

# Global variables
location = None
latitude = 0.0
longitude = 0.0


def display_banner():
    banner = f"""
    {Fore.CYAN}
    ##############################################
    #                                            #
    #              H O R I Z O N                 #
    #                                            #
    #           Created by: AMIT KASBE           #
    #                                            #
    ##############################################
    {Fore.RESET}
    """
    print(banner)


def process_number(phone_number):
    global location
    try:
        parsed_number = phonenumbers.parse(phone_number)
        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        print(f"{Fore.GREEN}[+] Tracking number: {formatted_number}")

        tz = timezone.time_zones_for_number(parsed_number)
        print(f"{Fore.GREEN}[+] Time Zone: {tz if tz else 'Unknown'}")

        location = geocoder.description_for_number(parsed_number, "en")
        print(f"{Fore.GREEN}[+] Region: {location if location else 'Unknown'}")

        service_provider = carrier.name_for_number(parsed_number, 'en')
        print(f"{Fore.GREEN}[+] Service Provider: {service_provider if service_provider else 'Unknown'}")

        fetch_social_media_profiles(phone_number)
        fetch_associated_numbers(phone_number)
        fetch_last_network_tower(phone_number)
        fetch_profile_photo(phone_number)

    except phonenumbers.NumberParseException as e:
        print(f"{Fore.RED}[-] Invalid phone number: {e}")
    except Exception as e:
        print(f"{Fore.RED}[-] Unexpected error: {e}")


def safe_api_get(url, headers):
    """Helper to safely make GET requests"""
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"{Fore.RED}[-] API request failed: {e}")
        return {}


def fetch_social_media_profiles(phone_number):
    print(f"{Fore.YELLOW}[+] Fetching social media profiles...")
    if not SOCIAL_MEDIA_API_KEY:
        print(f"{Fore.RED}[-] SOCIAL_MEDIA_API_KEY missing.")
        return
    url = f'https://api.socialmedia.com/v1/profiles?phone={phone_number}'
    headers = {'Authorization': f'Bearer {SOCIAL_MEDIA_API_KEY}'}
    data = safe_api_get(url, headers)
    profiles = data.get('profiles', [])
    if profiles:
        for p in profiles:
            print(f"{Fore.GREEN}[+] Profile: {p.get('url', 'N/A')}")
    else:
        print(f"{Fore.RED}[-] No profiles found or mock API used.")


def fetch_associated_numbers(phone_number):
    print(f"{Fore.YELLOW}[+] Fetching associated numbers...")
    if not ASSOCIATED_NUMBERS_API_KEY:
        print(f"{Fore.RED}[-] ASSOCIATED_NUMBERS_API_KEY missing.")
        return
    url = f'https://api.associatednumbers.com/v1/lookup?phone={phone_number}'
    headers = {'Authorization': f'Bearer {ASSOCIATED_NUMBERS_API_KEY}'}
    data = safe_api_get(url, headers)
    nums = data.get('associated_numbers', [])
    for n in nums:
        print(f"{Fore.GREEN}[+] Related Number: {n}")


def fetch_last_network_tower(phone_number):
    print(f"{Fore.YELLOW}[+] Fetching last network tower...")
    if not NETWORK_TOWER_API_KEY:
        print(f"{Fore.RED}[-] NETWORK_TOWER_API_KEY missing.")
        return
    url = f'https://api.networktower.com/v1/lookup?phone={phone_number}'
    headers = {'Authorization': f'Bearer {NETWORK_TOWER_API_KEY}'}
    data = safe_api_get(url, headers)
    tower = data.get('last_tower', 'Unknown')
    print(f"{Fore.GREEN}[+] Last Network Tower: {tower}")


def fetch_profile_photo(phone_number):
    print(f"{Fore.YELLOW}[+] Fetching profile photo...")
    if not PROFILE_PHOTO_API_KEY:
        print(f"{Fore.RED}[-] PROFILE_PHOTO_API_KEY missing.")
        return
    url = f'https://api.profilephoto.com/v1/photo?phone={phone_number}'
    headers = {'Authorization': f'Bearer {PROFILE_PHOTO_API_KEY}'}
    data = safe_api_get(url, headers)
    photo_url = data.get('photo_url', 'https://example.com/default.jpg')
    print(f"{Fore.GREEN}[+] Profile Photo URL: {photo_url}")


def get_approx_coordinates():
    global latitude, longitude
    if not gmaps or not location:
        print(f"{Fore.RED}[-] Google Maps API or location not available.")
        return
    try:
        geocode_result = gmaps.geocode(location)
        if geocode_result:
            loc_obj = geocode_result[0]['geometry']['location']
            latitude, longitude = loc_obj['lat'], loc_obj['lng']
            print(f"{Fore.GREEN}[+] Coordinates: {latitude}, {longitude}")
        else:
            print(f"{Fore.RED}[-] Could not resolve coordinates.")
    except ApiError as e:
        print(f"{Fore.RED}[-] Google Maps API error: {e}")
    except Exception as e:
        print(f"{Fore.RED}[-] Error getting coordinates: {e}")


def draw_map(phone_number):
    if latitude == 0.0 and longitude == 0.0:
        print(f"{Fore.RED}[-] Coordinates unavailable. Cannot create map.")
        return
    try:
        my_map = folium.Map(location=[latitude, longitude], zoom_start=9)
        folium.Marker([latitude, longitude], popup=location or "Unknown").add_to(my_map)
        timestamp = int(time.time())
        file_name = f"{phone_number.replace('+', '').replace(' ', '')}_{timestamp}.html"
        my_map.save(file_name)
        print(f"{Fore.GREEN}[+] Map saved at: {os.path.abspath(file_name)}")
    except Exception as e:
        print(f"{Fore.RED}[-] Map creation failed: {e}")


def get_live_location(phone_number):
    """Simulated live location"""
    base_lat = 17.3850
    base_lon = 78.4867
    simulated_latitude = base_lat + random.uniform(-0.05, 0.05)
    simulated_longitude = base_lon + random.uniform(-0.05, 0.05)
    print(f"{Fore.GREEN}[+] Live Coordinates: {simulated_latitude}, {simulated_longitude}")
    return simulated_latitude, simulated_longitude


def continuous_tracking(phone_number, duration=60):
    print(f"{Fore.YELLOW}[+] Starting live tracking for {duration}s...")
    start_time = time.time()
    while time.time() - start_time < duration:
        global latitude, longitude
        latitude, longitude = get_live_location(phone_number)
        draw_map(phone_number)
        time.sleep(10)
    print(f"{Fore.GREEN}[+] Tracking completed.")


def simple_cli():
    phone_number = None
    while True:
        print("\n" + Fore.CYAN + "Horizon CLI Menu" + Fore.RESET)
        print("1. Track a phone number")
        print("2. Display the map")
        print("3. Start live tracking")
        print("4. Exit")

        choice = input(Fore.YELLOW + "Enter choice (1/2/3/4): " + Fore.RESET)

        if choice == "1":
            phone_number = input(Fore.YELLOW + "Enter phone number with country code: " + Fore.RESET)
            process_number(phone_number)
            get_approx_coordinates()
        elif choice == "2":
            if phone_number:
                draw_map(phone_number)
            else:
                print(Fore.RED + "[-] No number tracked yet." + Fore.RESET)
        elif choice == "3":
            if phone_number:
                try:
                    duration = int(input(Fore.YELLOW + "Enter tracking duration (seconds): " + Fore.RESET))
                    continuous_tracking(phone_number, duration)
                except ValueError:
                    print(Fore.RED + "[-] Invalid duration." + Fore.RESET)
            else:
                print(Fore.RED + "[-] No number tracked yet." + Fore.RESET)
        elif choice == "4":
            print(Fore.GREEN + "Goodbye!" + Fore.RESET)
            sys.exit()
        else:
            print(Fore.RED + "Invalid option. Choose 1-4." + Fore.RESET)


if __name__ == "__main__":
    display_banner()
    simple_cli()
