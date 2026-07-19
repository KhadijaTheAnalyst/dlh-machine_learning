# 0x0C. APIs

This project is part of the DLH / Holberton ML engineering curriculum,
under the `pipeline/apis` directory of the `dlh-machine_learning`
repository. It covers consuming public REST APIs with Python's
`requests` library: handling pagination, following relational links
between resources, reading HTTP status codes and headers, and writing
standalone CLI scripts.

## Requirements

* Python 3.9
* `requests` module (`pip install requests`)
* All files start with `#!/usr/bin/env python3`
* All files are executable (`chmod +x`)
* Code follows `pycodestyle` (version 2.x) style
* Every module, class, and function has a docstring

## Tasks

### 0. Can I join? — `0-passengers.py`

`availableShips(passengerCount)` queries the
[SWAPI](https://swapi-api.hbtn.io/api/starships/) starships endpoint
and returns the names of every ship that can hold at least
`passengerCount` passengers.

* Follows pagination via the `next` field until it's exhausted.
* Strips commas from large passenger counts (e.g. `"1,000,000"`)
  before converting to `int`.
* Skips ships with non-numeric passenger values (`"n/a"`,
  `"unknown"`) instead of crashing.
* Returns an empty list if no ship qualifies.

```
ships = availableShips(4)
for ship in ships:
    print(ship)
```

### 1. Where I am? — `1-sentience.py`

`sentientPlanets()` queries the
[SWAPI](https://swapi-api.hbtn.io/api/species/) species endpoint and
returns the names of the home planets of every `sentient` species.

* A species counts as sentient if either its `classification` or its
  `designation` field equals `"sentient"`.
* `homeworld` on a species is a URL, not a name — a second request
  is made to that URL to fetch the actual planet name.
* Species with no homeworld (`None`) are skipped.
* Follows pagination the same way as task 0.

```
planets = sentientPlanets()
for planet in planets:
    print(planet)
```

### 2. Rate me if you can! — `2-user_location.py`

Standalone script that prints the `location` of a GitHub user, given
the full API URL as the first command-line argument.

```
./2-user_location.py https://api.github.com/users/<username>
```

* `404` → prints `Not found`
* `403` (rate limited) → prints `Reset in X min`, computed from the
  `X-Ratelimit-Reset` header (a Unix timestamp) minus the current
  time
* Otherwise → prints the user's `location` field
* Guarded with `if __name__ == '__main__':` so importing the file
  does not execute it

### 3. First launch — `3-first_launch.py`

Standalone script that displays the soonest upcoming SpaceX launch,
using the [SpaceX API](https://api.spacexdata.com/v4/launches/upcoming).

```
./3-first_launch.py
```

Output format:

```
<launch name> (<local date>) <rocket name> - <launchpad name> (<launchpad locality>)
```

* Launches are sorted by `date_unix`; the earliest one is selected.
* Python's `sort()` is stable, so if two launches share the same
  `date_unix`, the one listed first by the API stays first.
* `rocket` and `launchpad` on a launch are IDs, not data — separate
  requests fetch the rocket's name and the launchpad's name and
  locality.
* Guarded with `if __name__ == '__main__':`

## Author

Khadija Mustafa