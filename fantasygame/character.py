from dataclasses import dataclass
from typing import Final, List

import requests


DND_API_ENDPOINT: Final[str] = "https://www.dnd5eapi.co/api/2014"


@dataclass(frozen=True)
class Character():
    name: str
    job: str

    @classmethod
    def get_available_jobs(cls) -> List[str]:
        resp = requests.get(f"{DND_API_ENDPOINT}/classes/")
        if resp.status_code != 200:
            return []

        klasses = resp.json().get("results", [])
        return [klass["name"] for klass in klasses]
