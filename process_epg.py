import json

def read_epg_file(file_path): 'https://raw.githubusercontent.com/sadekmiah1/all-in-one/main/epg.json'
    """Reads and processes an EPG JSON file."""
    try:
        # Open and read the JSON file
        with open(file_path, 'r') as file:
            epg_data = json.load(file)
        
        # Extract the list of channels
        channels = epg_data.get('channels', [])
        
        # Check the total number of channels
        total_channels = len(channels)
        print(f"Total number of channels: {total_channels}")

        # Process channels (e.g., print first 10 for brevity)
        # Adjust the slicing as needed
        for i, channel in enumerate(channels[:10]):  # Modify slice as needed for large datasets
            print(f"Channel {i + 1}:")
            print(f"  ID: {channel.get('id', 'N/A')}")
            print(f"  Name: {channel.get('name', 'N/A')}")
            print(f"  Logo: {channel.get('logo', 'N/A')}")
            print()

    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except json.JSONDecodeError:
        print("Error: The file is not a valid JSON file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Specify the path to your JSON file
    file_path = 'epg.json'
    
    # Read and process the EPG file
    read_epg_file(file_path)
