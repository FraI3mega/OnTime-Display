import json
import time
from datetime import datetime

import requests
from prettytable import SINGLE_BORDER, PrettyTable

while True:
    przystanek = json.loads(
        requests.get(
            "https://dip.mzkopole.pl/getRealtime.json?stopPointSymbol=263"
        ).text
    )
    tablica = PrettyTable()
    tablica.set_style(SINGLE_BORDER)
    tablica.field_names = ["Nr", "Kierunek", "Odjazd"]
    # print(przystanek)
    for autobus in przystanek["departures"]:
        departure_in = (
            str(
                (
                    datetime.fromtimestamp(autobus["realDeparture"] // 1000)
                    - datetime.fromtimestamp(time.time())
                ).seconds
                // 60
            )
            + " min"
        )
        # print(autobus["lineName"], autobus["directionName"], departure_in)
        tablica.add_row([autobus["lineName"], autobus["directionName"], departure_in])
    print(tablica)
    time.sleep(60)
