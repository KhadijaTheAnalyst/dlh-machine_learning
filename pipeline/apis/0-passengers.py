#!/usr/bin/env python3
"""
Method that returns the list of ships that can hold
a given number of passengers, using the SWAPI API.
"""
import requests


def availableShips(passengerCount):
    """
    Returns the list of ship names that can hold at least
    passengerCount passengers.

    If no ship is available, returns an empty list.
    """
    ships = []
    url = "https://swapi-api.hbtn.io/api/starships/"

    while url:
        response = requests.get(url)
        data = response.json()

        for ship in data.get("results", []):
            passengers = ship.get("passengers", "0").replace(",", "")
            try:
                if int(passengers) >= passengerCount:
                    ships.append(ship.get("name"))
            except ValueError:
                # passengers value is "n/a" or "unknown" - skip it
                continue

        url = data.get("next")

    return ships
