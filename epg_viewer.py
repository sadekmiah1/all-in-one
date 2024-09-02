import requests
import json
from datetime import datetime

# Replace this URL with the actual URL of your EPG JSON file
epg_url = 'https://raw.githubusercontent.com/example/epg-data/main/epg.json'

def fetch_epg_data(url):
    """Fetches EPG data from the given URL and returns it as a Python dictionary."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching EPG data: {e}")
        return None

def display_epg_data(epg_data):
    """Displays the program titles and their start times."""
    if not epg_data:
        print("No EPG data available.")
        return

    # Display channel information
    print("Channels:")
    for channel in epg_data.get('channels', []):
        print(f"ID: {channel['id']}, Name: {channel['name']}")

    # Display program information
    print("\nPrograms:")
    for programme in epg_data.get('programmes', []):
        start_time = datetime.fromisoformat(programme['start'].replace('Z', '+00:00')).strftime('%Y-%m-%d %H:%M:%S')
        end_time = datetime.fromisoformat(programme['end'].replace('Z', '+00:00')).strftime('%Y-%m-%d %H:%M:%S')
        print(f"Title: {programme['title']}")
        print(f"Start Time: {start_time}")
        print(f"End Time: {end_time}")
        print(f"Description: {programme['description']}")
        print('-' * 40)

def main():
    """Main function to fetch and display EPG data."""
    epg_data = fetch_epg_data(epg_url)
    display_epg_data(epg_data)

if __name__ == "__main__":
    main()
