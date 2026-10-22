import requests
import json
from pathlib import Path

url = "https://api.gbif.org/v1/occurrence/search?taxonKey=4410657&country=DE&hasCoordinate=true&hasGeospatialIssue=false&limit=1"


try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    regenwurm_data = response.json()

    base_dir = Path(__file__).parent
    data_path = base_dir / "data" / "regenwurm_rohdaten.json"

    with data_path.open("w", encoding="utf-8") as json_file:
        json.dump(regenwurm_data, json_file, indent=4, ensure_ascii=False)

    print(response.status_code)
    print(regenwurm_data["results"][0]["scientificName"])

except requests.exceptions.HTTPError as error:
    print(f"HTTP-Fehler: {error}")

except requests.exceptions.Timeout:
    print("API-Fehler: API-Abfrage wegen Zeitüberschreitung fehlgeschlagen.")
    
except requests.exceptions.ConnectionError as error:
    print(f"Verbindungsfehler: {error}")

