#!/usr/bin/env python3
"""
Script that displays the first (soonest) upcoming SpaceX launch:
name, local date, rocket name, and launchpad name + locality.
"""
import requests


if __name__ == '__main__':
    # /upcoming gives us every launch that hasn't happened yet.
    url = "https://api.spacexdata.com/v4/launches/upcoming"
    launches = requests.get(url).json()

    # Sort by date_unix (the raw timestamp, safe to compare as a
    # number) so the soonest launch ends up first. Python's sort
    # is stable, so if two launches share the exact same date_unix,
    # whichever came first in the API response stays first here -
    # exactly what the task asks for.
    launches.sort(key=lambda launch: launch["date_unix"])
    first_launch = launches[0]

    launch_name = first_launch["name"]
    date_local = first_launch["date_local"]

    # rocket/launchpad on the launch object are just ID strings,
    # not the actual data - need a follow-up request for each,
    # same pattern as fetching a species' homeworld in task 1.
    rocket_id = first_launch["rocket"]
    rocket_url = "https://api.spacexdata.com/v4/rockets/{}".format(
        rocket_id)
    rocket_name = requests.get(rocket_url).json()["name"]

    launchpad_id = first_launch["launchpad"]
    launchpad_url = "https://api.spacexdata.com/v4/launchpads/{}".format(
        launchpad_id)
    launchpad_data = requests.get(launchpad_url).json()
    launchpad_name = launchpad_data["name"]
    launchpad_locality = launchpad_data["locality"]

    print("{} ({}) {} - {} ({})".format(
        launch_name,
        date_local,
        rocket_name,
        launchpad_name,
        launchpad_locality
    ))
