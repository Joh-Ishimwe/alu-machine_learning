#!/usr/bin/env python3
<<<<<<< HEAD
"""
Defines methods to ping the Star Wars API and return the list of ships
that can hold a given number of passengers
"""
=======
""" Return list of ships"""
>>>>>>> d01a612edafbcb20b156d4f8e219d7deae1f7d56


import requests


def availableShips(passengerCount):
<<<<<<< HEAD
    """
    Uses the Star Wars API to return the list of ships that can hold
        passengerCount number of passengers

    parameters:
        passengerCount [int]:
            the number of passenger the ship must be able to carry

    returns:
        [list]: all ships that can hold that many passengers
    """
    if type(passengerCount) is not int:
        raise TypeError(
            "passengerCount must be a positive number of passengers")
    if passengerCount < 0:
        raise ValueError(
            "passengerCount must be a positive number of passengers")
    url = "https://swapi-api.hbtn.io/api/starships/?format=json"
    ships = []
    while url:
        results = requests.get(url).json()
        ships += results.get('results')
        url = results.get('next')
    shipsList = []
    for ship in ships:
        passengers = ship.get('passengers').replace(",", "")
        if passengers != "n/a" and passengers != "unknown":
            if int(passengers) >= passengerCount:
                shipsList.append(ship.get('name'))
    return shipsList
=======
    """ Return list of ships

    Args:
        passengerCount (int): number of ships
    """

    res = requests.get('https://swapi-api.alx-tools.com/api/starships')

    output = []
    while res.status_code == 200:
        res = res.json()
        for ship in res['results']:
            passengers = ship['passengers'].replace(',', '')
            try:
                if int(passengers) >= passengerCount:
                    output.append(ship['name'])
            except ValueError:
                pass
        try:
            res = requests.get(res['next'])
        except Exception:
            break
    return output
>>>>>>> d01a612edafbcb20b156d4f8e219d7deae1f7d56
