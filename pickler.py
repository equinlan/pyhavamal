import pickle, re

f = open(r"pyhavamal\data\Poetic Edda_Hávamál.txt", "r")
lines = f.readlines()[15:1802]
populated_lines = filter(lambda line: re.match("\n", line) == None, lines)
stanzas = re.split(r"\[\d+\]\s", "".join(populated_lines))[1:]
stripped_stanzas = list(map(lambda stanza: stanza.rstrip(), stanzas))

pickle.dump(stripped_stanzas, open( r"pyhavamal\data\stanzas", "wb" ) )