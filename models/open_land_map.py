import requests
import json


def get_collections() -> json:
    """
    Gets the collections that are available from OpenLandMap.
    :return: Returns a list of the available collections.
    """
    response = requests.get("https://api.openlandmap.org/query/collections")
    return response.json()


def get_layers(collection):
    """
    Gets the layers that are available for a given 'collection'.
    Returns a json file containing the information for the provided layer
    Returns a json containing all layers if 'collection' is empty or not a string
    """
    if isinstance(collection, str) and collection:
        response = requests.get('https://api.openlandmap.org/query/layers?coll={}'.format(collection))

    else:
        response = requests.get('https://api.openlandmap.org/query/layers?coll=all')

    return response.json()


def get_populate() -> json:
    """
    Gets the layers for front-end to populate the menu.
    :return: Returns a json file containing layer information.
    """
    response = requests.get("https://api.openlandmap.org/query/populate")
    return response.json()
