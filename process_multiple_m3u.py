import requests

def download_file(url, filename):
    """Download a file from a URL and save it locally."""
    response = requests.get(url)
    response.raise_for_status()  # Ensure the request was successful
    with open(filename, 'wb') as file:
        file.write(response.content)
    print(f"File saved as {filename}")

def parse_m3u_file(filename):
    """Parse the M3U file to extract channel information."""
    channels = []
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    for i, line in enumerate(lines):
        line = line.strip()
        if line.startswith('#EXTINF'):
            # Extract channel information from #EXTINF tag
            parts = line.split(',', 1)
            if len(parts) > 1:
                name = parts[1]
                # The next line should be the URL
                url = lines[i + 1].strip()
                channels.append({
                    'name': name,
                    'url': url
                })
    return channels

def process_m3u_files(urls):
    """Process multiple M3U files from the given URLs."""
    all_channels = []
    for url in urls:
        local_filename = url.split('/')[-1]  # Extract the file name from URL
        download_file(url, local_filename)
        channels = parse_m3u_file(local_filename)
        all_channels.extend(channels)
    return all_channels

def main():
    # List of M3U file URLs
    m3u_urls = [
        'https://raw.githubusercontent.com/sadekmiah1/all-in-one/main/Allchannel1.m3u',
    'https://raw.githubusercontent.com/sadekmiah1/all-in-one/main/Allchannel2.m3u',
    'https://raw.githubusercontent.com/sadekmiah1/all-in-one/main/Bangla.m3u',
    'https://raw.githubusercontent.com/sadekmiah1/all-in-one/main/IndianBangla.m3u',
    'https://raw.githubusercontent.com/sadekmiah1/all-in-one/main/Indian.m3u',
    'https://raw.githubusercontent.com/sadekmiah1/all-in-one/main/Sports.m3u',
    'https://raw.githubusercontent.com/sadekmiah1/all-in-one/main/Cartoon.m3u',
    'https://raw.githubusercontent.com/sadekmiah1/all-in-one/main/Documentary.m3u',
    'https://raw.githubusercontent.com/sadekmiah1/all-in-one/main/English.m3u',
    'https://raw.githubusercontent.com/sadekmiah1/all-in-one/main/Music.m3u',
    'https://raw.githubusercontent.com/sadekmiah1/all-in-one/main/Islamic.m3u',
        # Add more URLs here
    ]
    
    # Process all M3U files
    all_channels = process_m3u_files(m3u_urls)
    
    # Print channel information
    for channel in all_channels:
        print(f"Name: {channel['name']}, URL: {channel['url']}")

if __name__ == '__main__':
    main()
