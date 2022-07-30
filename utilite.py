import json

import requests

candidates = 'https://jsonkeeper.com/b/YFEO'


def load_candidates(candidates):
    candidates = requests.get(candidates)
    return candidates.json()
