import requests

def download_file(url, filename):
    response = requests.get(url)
    response.raise_for_status()  # Ensure the request was successful
    with open(filename, 'wb') as file:
        file.write(response.content)
    print(f"File saved as {filename}")

def parse_m3u_file(filename):
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

def main():
    # URL to the M3U file
    m3u_url = 'https://raw.githubusercontent.com/sadekmiah1/all-in-one/main/Allchannel1.m3u'
    
    # Download the M3U file
    local_filename = 'Allchannel1.m3u'
    download_file(m3u_url, local_filename)
    
    # Parse the M3U file
    channels = parse_m3u_file(local_filename)
    
    # Print channel information
    for channel in channels:
        print(f"Name: {channel['name']}, URL: {channel['url']}")

if __name__ == '__main__':
    main()
