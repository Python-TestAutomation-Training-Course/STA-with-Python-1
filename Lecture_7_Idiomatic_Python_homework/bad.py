"""
Ready implementation of bad.py
See the task in good.py
"""
import logging
from typing import Dict, List

import requests

logging.basicConfig(level=logging.INFO)


def create_country_make_dict(url: str) -> Dict[str, List[str]]:
    country_manufacturers: Dict[str, List[str]] = {}
    page = 1
    while True:
        response = requests.get(f"{url}&page={page}")
        make_dict = response.json()
        if not make_dict["Count"]:
            break
        for manufacturer in make_dict["Results"]:
            country = manufacturer["Country"]
            if country:
                if country in country_manufacturers:
                    country_manufacturers[country].append(manufacturer["Mfr_Name"])
                else:
                    country_manufacturers[country] = [manufacturer["Mfr_Name"]]
        logging.info(f"Done with page {page}")
        page += 1
    return country_manufacturers
