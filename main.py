import json
import time
from datetime import datetime

import requests

przystanek = json.loads(
    requests.get("https://dip.mzkopole.pl/getRealtime.json?stopPointSymbol=352").text
)
# print(przystanek)
for autobus in przystanek["departures"]:
    departure_in = datetime.fromtimestamp(
        autobus["realDeparture"] // 1000
    ) - datetime.fromtimestamp(time.time())
    print(
        autobus["lineName"], autobus["directionName"], departure_in.seconds // 60, "min"
    )
