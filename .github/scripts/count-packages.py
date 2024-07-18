import json
import requests
import os

def count_packages_in_files(files):
    total_packages = 0
    for url in files:
        response = requests.get(url)
        data = response.json()
        total_packages += len(data.get("Packages", []))
    return total_packages

if __name__ == "__main__":
    files = [
        'https://raw.githubusercontent.com/ohhsodead/arisen-studio-database/main/PS3/packages/avatars.json',
        'https://raw.githubusercontent.com/ohhsodead/arisen-studio-database/main/PS3/packages/demos.json',
        'https://raw.githubusercontent.com/ohhsodead/arisen-studio-database/main/PS3/packages/dlcs.json',
        'https://raw.githubusercontent.com/ohhsodead/arisen-studio-database/main/PS3/packages/games.json',
        'https://raw.githubusercontent.com/ohhsodead/arisen-studio-database/main/PS3/packages/themes.json'
    ]
    total_packages = count_packages_in_files(files)
    
    badge_data = {
        "schemaVersion": 1,
        "label": "packages",
        "message": str(total_packages),
        "color": "brightgreen"
    }
    
    os.makedirs('.github/badges', exist_ok=True)
    with open('github/badges/package-count-badge.json', 'w') as f:
        json.dump(badge_data, f)
