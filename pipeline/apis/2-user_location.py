#!/usr/bin/env python3
"""
Script that prints the location of a specific GitHub user,
given the full API URL as the first command line argument.
"""
import sys
import time
import requests


if __name__ == '__main__':
    # This whole block only runs when the file is executed directly
    # (./2-user_location.py ...), NOT when it's imported elsewhere -
    # that's exactly what the task requires.
    if len(sys.argv) < 2:
        print("Usage: ./2-user_location.py <GitHub API user URL>")
        sys.exit(1)

    # sys.argv[1] is the URL passed on the command line, e.g.
    # https://api.github.com/users/holbertonschool
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code == 404:
        # User doesn't exist on GitHub.
        print("Not found")

    elif response.status_code == 403:
        # We've hit GitHub's rate limit. X-Ratelimit-Reset is a Unix
        # timestamp (seconds since epoch) telling us exactly when
        # our quota resets.
        reset_timestamp = int(response.headers.get("X-Ratelimit-Reset", 0))
        current_timestamp = time.time()
        # Difference in seconds, converted down to whole minutes.
        minutes = int((reset_timestamp - current_timestamp) / 60)
        print("Reset in {} min".format(minutes))

    else:
        # 200 OK - parse the JSON body and pull out "location".
        data = response.json()
        print(data.get("location"))
