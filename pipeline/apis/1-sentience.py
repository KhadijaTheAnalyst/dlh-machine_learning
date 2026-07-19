#!/usr/bin/env python3
"""
Method that returns the list of names of the home planets
of all sentient species, using the SWAPI API.
"""
import requests


def sentientPlanets():
    """
    Returns the list of home planet names for every species
    whose classification or designation is 'sentient'.
    """
    planets = []
    url = "https://swapi-api.hbtn.io/api/species/"

    while url:
        response = requests.get(url)
        data = response.json()

        for species in data.get("results", []):
            classification = species.get("classification", "")
            designation = species.get("designation", "")

            if classification == "sentient" or designation == "sentient":
                homeworld_url = species.get("homeworld")
                if homeworld_url is None:
                    continue

                planet_response = requests.get(homeworld_url)
                planet_data = planet_response.json()
                planets.append(planet_data.get("name"))

        url = data.get("next")

    return planets
