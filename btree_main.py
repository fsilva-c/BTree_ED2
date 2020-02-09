from key_insert import *
from btree_net1 import *

ORDER = 2

def btree_creator(type_key):
    t = BTree(ORDER)

    archive = open("cardapy.csv")
    items = csv.DictReader(archive)

    iArchive = 1
    for lines in items:
        output = []
        output.append(iArchive)
        output.append(lines[type_key])
        
        t.insert(output)
        iArchive += 1

    archive.close()

    return t
