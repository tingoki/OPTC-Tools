import requests
import os

# start and end number pretty obvious, remember it starts with 0001 not 1 
start_number = ''
end_number = ''

# Use the path you wish to save icons to
destination_folder = 'path'

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for number in range(int(start_number), end_number + 1):
   
    number_str = str(number).zfill(len(start_number))

    url = f'https://cdn.onepiece-tc.jp/images/characters/character_{number_str}_t.png'

    filename = f'character_{number_str}_t.png'
    destination_file = os.path.join(destination_folder, filename)

    if os.path.exists(destination_file):
        print(f"Skipped file {destination_file} (already downloaded)")
        continue

    response = requests.get(url)

    if response.status_code == 200:
        try:
            with open(destination_file, 'wb') as file:
                file.write(response.content)
            print(f"Image saved: {destination_file}")
        except IOError as e:
            print(f"Failed to save image: {e}")
    elif response.status_code == 403:
        print(f"Skipped file {destination_file} (Not A Unit?)")
    else:
        print(f"Failed to download image: {response.status_code} - {response.reason}")
