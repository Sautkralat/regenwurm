import requests
import json
from pathlib import Path

base_dir = Path(__file__).parent
data_path = base_dir / "data" / "regenwurm_rohdaten.json"

with data_path.open("r", encoding="utf-8") as json_file:
    regenwurm_data_eingelesen = json.load(json_file)

print(regenwurm_data_eingelesen["results"][0]["scientificName"])