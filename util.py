import random, sys

"""

This is a classless module. Sometimes this sort of thing is handy. As it turns out, this is an effective way of creating
a pattern called "Singleton" in Python.

"""

"""
Create a random name from the list of names. This also randomly pics a gender using an odd choice. I will have to check
to see what the side effects of this could be. Is python pass by reference in this case?
"""
def create_random_name() -> str:
    name_list = random.choice([girl_names, boy_names])
    return random.choice(name_list) + " " + random.choice(last_names)


"""
Take a list and load it with names.
"""
def load_list(name_type: str) -> [str]:
    filepath = relpath + files[name_type]
    namelist = []
    try:
        f = open(filepath, 'r')
        for name in f:
            namelist.append(name.strip().capitalize())
        return namelist
    except IOError:
        print("unable to read file " +filepath)
        sys.exit()
        return []


# the root path for our game's resources
relpath = "res/"

# a dict to map names to gender
files = {
    "boy": "boy-names.list",
    "girl": "girl-names.list",
    "last": "last-names.list"
}


# do work the first time this module is invoked.
boy_names  = load_list("boy")
girl_names = load_list("girl")
last_names = load_list("last")