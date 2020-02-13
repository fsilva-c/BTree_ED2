from key_insert import *
from btree import *

ORDER = 2

def btree_creator(type_key):
    t = BTree(ORDER)

    archive = open("cardapy.csv")
    items = csv.DictReader(archive)

    iArchive = 1
    for lines in items:
        output = []
        output.append(lines[type_key])
        output.append(iArchive)
        
        t.insert(output)
        iArchive += 1

    archive.close()

    return t

def btree_typeProtein():
    """ Este método cria três árvores com a chave alfabética porém com o campo type_protein a mais.
    
    Returns:
        [tree_carne] -- [Árvore que tem o type_protein carne]
        [tree_peixe] -- [Árvore que tem o type_protein peixe]
        [tree_vegano] -- [Árvore que tem o type_protein vegano]
    """    
    tree_carne = BTree(ORDER)
    tree_peixe = BTree(ORDER)
    tree_vegano = BTree(ORDER)

    with open("cardapy.csv") as archive:
        items = csv.DictReader(archive)

        iArchive = 1
        for lines in items:
            output = []
            
            output.append(lines["name"])
            output.append(iArchive)
            output.append(lines["type_protein"])
            if lines["type_protein"] == "carne":
                tree_carne.insert(output)

            elif lines["type_protein"] == "peixe":
                tree_peixe.insert(output)
                
            elif lines["type_protein"] == "vegano":
                tree_vegano.insert(output)

            iArchive += 1
            
        archive.close()

        return tree_carne, tree_peixe, tree_vegano
