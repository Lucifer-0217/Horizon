import argparse
import os
import sys
import requests
import folium
import phonenumbers
from colorama import Fore, init
from phonenumbers import carrier, geocoder, timezone
from googlemaps import Client as GoogleMapsClient
from googlemaps.exceptions import ApiError
import time

init()


#gmaps = GoogleMapsClient(key='YOUR_GOOGLE_MAPS_API_KEY')


#SOCIAL_MEDIA_API_KEY = 'YOUR_SOCIAL_MEDIA_API_KEY'
#ASSOCIATED_NUMBERS_API_KEY = 'YOUR_ASSOCIATED_NUMBERS_API_KEY'
#PROFILE_PHOTO_API_KEY = 'YOUR_PROFILE_PHOTO_API_KEY'
#NETWORK_TOWER_API_KEY = 'YOUR_NETWORK_TOWER_API_KEY'


def display_banner():
    banner = f"""
    {Fore.CYAN}
    ##############################################
    #                                            #
    #              H O R I Z O N                 #
    #                                            #
    #         Created by: GHOST                  #
    #                                            #
    ##############################################
    {Fore.RESET}
    """
    print(banner)


def process_number(phone_number):
    global location

    try:
        parsed_number = phonenumbers.parse(phone_number)
        print(f"{Fore.GREEN}[+] Attempting to track the location of "
              f"{phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}..")

        print(f"{Fore.GREEN}[+] Time Zone ID: {timezone.time_zones_for_number(parsed_number)}")

        location = geocoder.description_for_number(parsed_number, "en")
        if location:
            print(f"{Fore.GREEN}[+] Region: {location}")
        else:
            print(f"{Fore.RED}[-] Region: Unknown")

        service_provider = carrier.name_for_number(parsed_number, 'en')
        if service_provider:
            print(f"{Fore.GREEN}[+] Service Provider: {service_provider}")
        else:
            print(f"{Fore.RED}[-] Service Provider: Unknown")


        fetch_social_media_profiles(phone_number)
        fetch_associated_numbers(phone_number)
        fetch_last_network_tower(phone_number)
        fetch_profile_photo(phone_number)

    except phonenumbers.NumberParseException as e:
        print(f"{Fore.RED}[-] NumberParseException: {e}")
        sys.exit()
    except Exception as e:
        print(f"{Fore.RED}[-] An unexpected error occurred: {e}")
        sys.exit()


def fetch_social_media_profiles(phone_number):
    print(f"{Fore.YELLOW}[+] Fetching social media profiles for {phone_number}...")
    try:
        response = requests.get(
            f'https://api.socialmedia.com/v1/profiles?phone={phone_number}',
            headers={'Authorization': f'Bearer {SOCIAL_MEDIA_API_KEY}'}
        )
        response.raise_for_status()
        profiles = response.json()
        for profile in profiles:
            print(f"{Fore.GREEN}[+] Profile: {profile.get('url', 'No URL available')}")
    except requests.RequestException as e:
        print(f"{Fore.RED}[-] Error fetching social media profiles: {e}")


def fetch_associated_numbers(phone_number):
    print(f"{Fore.YELLOW}[+] Fetching associated numbers for {phone_number}...")
    try:
        response = requests.get(
            f'https://api.associatednumbers.com/v1/lookup?phone={phone_number}',
            headers={'Authorization': f'Bearer {ASSOCIATED_NUMBERS_API_KEY}'}
        )
        response.raise_for_status()
        data = response.json()
        associated_numbers = data.get('associated_numbers', [])
        for number in associated_numbers:
            print(f"{Fore.GREEN}[+] Associated Number: {number}")
    except requests.RequestException as e:
        print(f"{Fore.RED}[-] Error fetching associated numbers: {e}")


def fetch_last_network_tower(phone_number):
    print(f"{Fore.YELLOW}[+] Fetching last network tower information for {phone_number}...")
    try:
        response = requests.get(
            f'https://api.networktower.com/v1/lookup?phone={phone_number}',
            headers={'Authorization': f'Bearer {NETWORK_TOWER_API_KEY}'}
        )
        response.raise_for_status()
        data = response.json()
        last_tower = data.get('last_tower', 'Unknown')
        print(f"{Fore.GREEN}[+] Last Network Tower: {last_tower}")
    except requests.RequestException as e:
        print(f"{Fore.RED}[-] Error fetching network tower information: {e}")


def fetch_profile_photo(phone_number):
    print(f"{Fore.YELLOW}[+] Fetching profile photo for {phone_number}...")
    try:
        response = requests.get(
            f'https://api.profilephoto.com/v1/photo?phone={phone_number}',
            headers={'Authorization': f'Bearer {PROFILE_PHOTO_API_KEY}'}
        )
        response.raise_for_status()
        data = response.json()
        photo_url = data.get('photo_url', 'https://example.com/photo.jpg')
        print(f"{Fore.GREEN}[+] Profile Photo URL: {photo_url}")
    except requests.RequestException as e:
        print(f"{Fore.RED}[-] Error fetching profile photo: {e}")


def get_approx_coordinates():
    global latitude, longitude
    try:
        if location:
            geocode_result = gmaps.geocode(location)
            if geocode_result:
                location_obj = geocode_result[0]['geometry']['location']
                latitude, longitude = location_obj['lat'], location_obj['lng']
                print(f"{Fore.GREEN}[+] Latitude: {latitude}, Longitude: {longitude}")
                print(f"{Fore.LIGHTRED_EX}[+] Approximate Location: {location}")
            else:
                print(f"{Fore.RED}[-] Could not get coordinates for location: {location}")
                latitude, longitude = 0.0, 0.0
        else:
            print(f"{Fore.RED}[-] Location not available to fetch coordinates.")
            latitude, longitude = 0.0, 0.0
    except ApiError as e:
        print(f"{Fore.RED}[-] Google Maps API error: {e}")
        latitude, longitude = 0.0, 0.0
    except Exception as e:
        print(f"{Fore.RED}[-] Could not determine coordinates: {e}")
        latitude, longitude = 0.0, 0.0


def draw_map(phone_number):
    try:
        if latitude == 0.0 and longitude == 0.0:
            print(f"{Fore.RED}[-] Coordinates are not available. Cannot create map.")
            return

        my_map = folium.Map(location=[latitude, longitude], zoom_start=9)
        folium.Marker([latitude, longitude], popup=location).add_to(my_map)
        file_name = f"{phone_number.replace('+', '').replace(' ', '')}.html"
        my_map.save(file_name)
        print(f"{Fore.GREEN}[+] See the map at: {os.path.abspath(file_name)}")
    except Exception as e:
        print(f"{Fore.RED}[-] Error in map creation: {e}")
        sys.exit()


def get_live_location(phone_number):
    print(f"{Fore.YELLOW}[+] Fetching live location for {phone_number}...")

    try:

        simulated_latitude = 17.385044
        simulated_longitude = 78.486671
        print(f"{Fore.GREEN}[+] Live Latitude: {simulated_latitude}, Longitude: {simulated_longitude}")
        return simulated_latitude, simulated_longitude
    except Exception as e:
        print(f"{Fore.RED}[-] Error fetching live location: {e}")
        return None, None


def continuous_tracking(phone_number, duration=60):
    print(f"{Fore.YELLOW}[+] Starting continuous tracking for {phone_number}...")
    start_time = time.time()
    while time.time() - start_time < duration:
        latitude, longitude = get_live_location(phone_number)
        if latitude and longitude:
            draw_map(phone_number)
        time.sleep(10)


def simple_cli():
    phone_number = None
    while True:
        print("\n" + Fore.CYAN + "Horizon CLI Menu" + Fore.RESET)
        print("1. Track a phone number")
        print("2. Display the map")
        print("3. Start live tracking")
        print("4. Exit")

        choice = input(Fore.YELLOW + "Enter your choice (1/2/3/4): " + Fore.RESET)

        if choice == "1":
            phone_number = input(Fore.YELLOW + "Enter phone number with country code: " + Fore.RESET)
            process_number(phone_number)
            get_approx_coordinates()
        elif choice == "2":
            if phone_number:
                draw_map(phone_number)
            else:
                print(Fore.RED + "[-] No phone number tracked yet. Please track a phone number first." + Fore.RESET)
        elif choice == "3":
            if phone_number:
                duration = int(input(Fore.YELLOW + "Enter tracking duration in seconds: " + Fore.RESET))
                continuous_tracking(phone_number, duration)
            else:
                print(Fore.RED + "[-] No phone number tracked yet. Please track a phone number first." + Fore.RESET)
        elif choice == "4":
            print(Fore.GREEN + "Exiting... Goodbye!" + Fore.RESET)
            sys.exit()
        else:
            print(Fore.RED + "Invalid choice, please select 1, 2, 3, or 4." + Fore.RESET)


if __name__ == "__main__":
    display_banner()
    simple_cli()
