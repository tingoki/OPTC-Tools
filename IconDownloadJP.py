import requests
import os

# start and end number pretty obvious, remember it starts with 0001 not 1 
start_number_str = ''
end_number_str = ''

# Use the path you wish to save icons to
destination_folder = 'path'

# Convert string numbers to integers for iteration
start_number = int(start_number_str)
end_number = int(end_number_str)

# Determine the length for zero-padding based on the start_number_str
padding_length = len(start_number_str)

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for number in range(start_number, end_number + 1):
   
    number_str = str(number).zfill(padding_length)

    url = f'https://cdn.gb.onepiece-tc.jp/images/characters/character_{number_str}_t.png'

    filename = f'character_{number_str}_t.png'
    destination_file = os.path.join(destination_folder, filename)

    if os.path.exists(destination_file):
        print(f"Skipped file {destination_file} (already downloaded)")
        continue

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)

        with open(destination_file, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Image saved: {destination_file}")
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 403:
            print(f"Skipped file {destination_file} (Not A Unit?)")
        else:
            print(f"Failed to download image: {e.response.status_code} - {e.response.reason}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request for {destination_file}: {e}")
    except IOError as e:
        print(f"Failed to save image: {e}")
