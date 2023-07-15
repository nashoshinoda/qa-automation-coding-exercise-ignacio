import json
import random

name_list = json.load(open("./resources/names.json"))


class CustomLibs:
    """
    `Description:`
        Select one of the fake username from a list.

    `Return:`
        `String:` Name of a username.
    """
    def get_random_name(self):
        return name_list[random.randint(0, 2)]
