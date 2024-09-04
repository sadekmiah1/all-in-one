import requests

def fetch_json_from_github(raw_url):
    try:
        # Fetch the JSON data
        response = requests.get(raw_url)
        response.raise_for_status()  # Check if the request was successful
        # Parse JSON data
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error fetching the JSON file: {e}")
        return None
    except ValueError as e:
        print(f"Error parsing JSON data: {e}")
        return None

def print_channel_info(data):
    if not data or 'channels' not in data:
        print("No channels data found.")
        return

    # Extract and print channel information
    for channel in data.get('channels', []):
        channel_id = channel.get('id')
        name = channel.get('name')
        logo = channel.get('logo')
        print(f'ID: {channel_id}, Name: {name}, Logo: {logo}')

# Replace this URL with the actual raw URL of your JSON file on GitHub
raw_github_url = 'https://raw.githubusercontent.com/username/repository/main/epg.json'

# Fetch JSON data from GitHub
json_data = fetch_json_from_github(raw_github_url)

# Print channel information
print_channel_info(json_data)
