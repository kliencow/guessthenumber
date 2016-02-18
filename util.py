import random, sys

def create_random_name():
    name_list = random.choice([girl_names, boy_names])
    return random.choice(name_list) + " " + random.choice(last_names)


def load_list(name_type):
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


relpath = "res/"

files = {
    "boy": "boy-names.list",
    "girl": "girl-names.list",
    "last": "last-names.list"
}

boy_names  = load_list("boy")
girl_names = load_list("girl")
last_names = load_list("last")