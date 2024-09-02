import requests
import json

# List of M3U playlist URLs
m3u_urls = [
    'https://raw.githubusercontent.com/sadekmiah1/all-in-one/main/Allchannel1.m3u',
    'https://raw.githubusercontent.com/sadekmiah1/all-in-one/main/Allchannel2.m3u'
]

def download_m3u(m3u_url):
    """Download the M3U file from the provided URL."""
    response = requests.get(m3u_url)
    response.raise_for_status()  # Check if the request was successful
    return response.text.splitlines()

def parse_m3u(lines):
    """Parse the M3U lines to extract channel information."""
    channels = []
    programs = []
    
    for line in lines:
        if line.startswith('#EXTINF:'):
            parts = line.split(' ', 1)
            channel_info = parts[1].split(',')
            channel_name = channel_info[1] if len(channel_info) > 1 else "Unknown Channel"
            
            # Extract logo URL if present
            logo_url = None
            if 'tvg-logo=' in parts[1]:
                logo_start = parts[1].find('tvg-logo="') + len('tvg-logo="')
                logo_end = parts[1].find('"', logo_start)
                logo_url = parts[1][logo_start:logo_end]

            channels.append({
                "id": None,  # ID not present in the M3U file
                "name": channel_name,
                "logo": logo_url
            })

            # Add a dummy program entry for each channel (no specific timing here)
            programs.append({
                "channel_id": None,  # ID not present in the M3U file
                "title": channel_name,
                "description": "Sample program description."
            })
    
    return channels, programs

def save_json(epg_data, filename='epg.json'):
    """Save the EPG data to a JSON file."""
    with open(filename, 'w') as json_file:
        json.dump(epg_data, json_file, indent=4)

def main():
    """Main function to execute the script."""
    all_channels = []
    all_programs = []

    for m3u_url in m3u_urls:
        print(f"Processing {m3u_url}...")
        m3u_lines = download_m3u(m3u_url)
        channels, programs = parse_m3u(m3u_lines)
        
        # Add channels and programs to the combined lists
        all_channels.extend(channels)
        all_programs.extend(programs)
    
    # Create the EPG JSON structure
    epg_data = {
        "channels": all_channels,
        "programs": all_programs
    }
    
    save_json(epg_data)
    print("EPG data has been written to epg.json")

if __name__ == "__main__":
    main()
