import requests
import re
from PIL import Image

RANDOM_URL = "https://www.random.org/{type}/"


def get_random_integers(num, value_min, value_max, col, base=10, return_format="plain", rnd="new"):
    """
	Returns a list of random numbers

	Arguments
	num: Number of random numbers
	value_min: Min value
	value_max: Max value
	col: Number of columns
	base: Base of number returned
	return_format: Return type of document
	rnd: Randomization used

    return List
    """

    params = {
        "num": num,
        "min": value_min,
        "max": value_max,
        "col": col,
        "base": base,
        "format": return_format,
        "rnd": rnd
    }

    r = requests.get(RANDOM_URL.format(type="integers"), params=params)

    if r.status_code == requests.codes.ok:
        return map(int, r.text.strip().split('\n')[:num])
    else:
        r.raise_for_status()
        return []


def create_rgb_bitmap(pixel_red, pixel_green, pixel_blue, file_name="result.bmp", resolution=[128, 128]):
	"""
	Saves a RGB bitmap image

	Arguments
	pixel_red: list of red pixels
	pixel_green: list of red pixels
	pixel_blue: list of red pixels
	file_name: Name of image
	resolution: resolution of image

	"""

    img = Image.new('RGB', tuple(resolution))
    img_pixels = img.load()

    for i in range(resolution[0]):
        for j in range(resolution[1]):
            img_pixels[i, j] = tuple([pixel_red[i + j],pixel_green[i+j],pixel_blue[i+j]])

    img.show()
    img.save(file_name)

    return


def main():
    total_pixels = 16384 # 128 * 128
    pixel_red = get_random_integers(10000,0,255,1) + get_random_integers(total_pixels - 10000,0,255,1)
    pixel_green = get_random_integers(10000,0,255,1) + get_random_integers(total_pixels - 10000,0,255,1)
    pixel_blue = get_random_integers(10000,0,255,1) + get_random_integers(total_pixels - 10000,0,255,1)
    return create_rgb_bitmap(pixel_red,pixel_green,pixel_blue)


main()
