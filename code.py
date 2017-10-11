import requests
import re
RANDOM_URL = "https://www.random.org/{type}/"


def get_random_integers(num, value_min, value_max, value_number, base=10, return_format="plain", rnd="new"):
    """
    return List
    """

    params = {
        "num": num,
        "min": value_min,
        "max": value_max,
        "col": value_number,
        "base": base,
        "format": return_format,
        "rnd": rnd
    }

    r = requests.get(RANDOM_URL.format(type="integers"), params=params)

    if r.status_code == requests.codes.ok:
    	return re.split('\D+',c)
    else:
    	r.raise_for_status()
    	return []