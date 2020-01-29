from key_insert import *
from menu_prog import *
from btree_net1 import *

ORDER = 2


def itemRegister():

    item = struct_item()
    menu_prog = struct_menu()
    
    item["name"] = input("Informe o nome do produto: ")
    #caixa alta
    item["name"] = item["name"].upper()
    if key_validator(item["name"], "name") == False:
        return

    item["price"] = input("Informe o preco do produto: ")
    if key_validator(item["price"], "price") == False:
        return

    item["igredients"] = input("Informe os igredientes: ")
    item["igredients"] = item["igredients"].upper()
    
    item["kcal"]  = input("Informe a quantidade de kcal contida no item: ")
    
    while(True):
        item["type_item"] = int(input("1-> Bebida\n2-> Comida\nInforme o tipo do item: "))
        item["type_item"] = menu_prog["type_item"][item["type_item"]]

        if item["type_item"] == "bebida":
            item["type_drink"] = int(input("1-> Suco\n2-> Refrigerante\n3-> Agua\nInforme o tipo da bebida: "))
            item["type_drink"] = menu_prog["type_drink"][item["type_drink"]]

            item["flavor_drink"] = input("Informe o sabor da bebida: ")
            break

        elif item["type_item"] == "comida":
            item["type_protein"] = int(input("1-> Carne\n2-> Peixe\n3-> Vegano\nInforme o tipo da proteína: "))
            item["type_protein"] = menu_prog["type_protein"][item["type_protein"]]

            item["protein_portion"] = input("Informe a quantidade de porções que o prato rende: ")
            break

    input_archive(item)
    
def btree_creator(type_key):
    t = BTree(ORDER)

    archive = open("cardapy.csv")
    items = csv.DictReader(archive)

    iArchive = 1
    for lines in items:
        output = str(iArchive) + ", " + lines[type_key]
        
        t.insert(output)
        iArchive += 1

    archive.close()

    return t

#itemRegister()
t_name = BTree(ORDER)
t_price = BTree(ORDER)

t_name = btree_creator("name")
t_price = btree_creator("price")

#t_name.print_seq_ord()
t_price.print_seq_ord()

#bt.print_order()