import requests


def multiselect_to_string(list_options, other_options):
    retlist = ', '.join(list_options)
    if other_options != "":
        retlist = retlist + ", " + other_options
    return retlist

def save_image(image_url, name):
    img_data = requests.get(image_url)

    # Save the image to a file
    with open("../img/" + name + ".png", "wb") as f:
        f.write(img_data.content)