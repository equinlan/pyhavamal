import pickle
import random as r

stanzas = pickle.load(open(r"pyhavamal\data\stanzas", "rb"))

def all():
    return stanzas

def random():
    return r.choice(all())