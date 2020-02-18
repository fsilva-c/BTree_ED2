from structs_prog import *
from key_insert import *
from btree_creator import *
from color import *
 
option = -9
option_bt = -9
option_btKey = -9
option_btProtein = -9

tree_keyName = btree_creator("name")
tree_keyPrice = btree_creator("price")
tree_carne, tree_peixe, tree_vegano = btree_typeProtein()

def print_logo():
    print(color.BOLD + color.DARKCYAN + "=" * 60 + color.END)
    print(color.BOLD + color.RED + "=         RESTAURANTE ESPETINHO COM DOBRADINHA II          =" + color.END)
    print(color.BOLD + color.DARKCYAN + "=" * 60 + color.END)
    print("\n")

while option != 0:
    system("clear")
    print_logo()
    option = int(input(color.BOLD + "1-> INSERIR NOVO ITEM\n2-> ELIMINAR ITEM\n3-> MODIFICAR ITEM\n4-> OPERAÇÕES DA BTREE\n0-> Sair\n\n" + color.DARKCYAN + "Informe uma opcao: " + color.END))
        
    #1) inserir registro
    if option == 1:
        system("clear")
        #validando input
        name_item = input(color.DARKCYAN + "Informe o nome do produto: " + color.END)
        name_item = name_item.upper()
        check_name = tree_keyName.search_bt(tree_keyName.root, name_item)

        price_item = float(input(color.DARKCYAN + "Informe o preco do produto: " + color.END))

        check_price = tree_keyPrice.search_bt(tree_keyPrice.root, price_item)

        itemRegister(name_item, price_item, check_name, check_price)
        system("pause")

    #2) remoção do item
    elif option == 2:
        system("clear")
        btree = int(input(color.BOLD + "1-> ÁRVORE NUMÉRICA\n2-> ÁRVORE ALFABÉTICA\n\n" + color.DARKCYAN + "Informe uma opção: " + color.END))
        
        #arvore numérica
        if btree == 1:
            system("clear")
            key = input(color.DARKCYAN + "Informe a chave que será removida: " + color.END)
            key = float(key)
            index = tree_keyPrice.search_bt(tree_keyPrice.root, key)

            remove_item(index)

        #arvore alfabética
        elif btree == 2:
            system("clear")
            key = input(color.DARKCYAN + "Informe a chave que será removida: " + color.END)
            key = key.upper()
            index = tree_keyName.search_bt(tree_keyName.root, key)

            remove_item(index)
            
        system("pause")

    #3) alterar registro
    elif option == 3:
        system("clear")
        btree = int(input(color.BOLD + "1-> ÁRVORE NUMÉRICA\n2-> ÁRVORE ALFABÉTICA\n\n" + color.DARKCYAN + "Informe uma opção: " + color.END))

        #arvore numérica
        if btree == 1:
            system("clear")
            key = input(color.DARKCYAN + "Informe a chave que será alterada: " + color.END)
            key = float(key)
            index = tree_keyPrice.search_bt(tree_keyPrice.root, key)

            alter_register(index)
        
        #arvore alfabética
        elif btree == 2:
            system("clear")
            key = input(color.DARKCYAN + "Informe a chave que será alterada: " + color.END)
            key = key.upper()
            index = tree_keyName.search_bt(tree_keyName.root, key)
            alter_register(index)

        system("pause")

    #4) operações da btree
    elif option == 4:
        system("clear")
        option_bt = int(input(color.BOLD + "1-> ÁRVORE NUMÉRICA\n2-> ÁRVORE ALFABÉTICA\n3-> ÁRVORES TIPO DE PROTEÍNA\n\n" + color.DARKCYAN + "Informe uma opção: " + color.END))

        #4.1) chave numérica
        if option_bt == 1:
            system("clear")
            option_btKey = int(input(color.BOLD + "1-> DETALHAR REGISTRO\n2-> BUSCA POR INTERVALO\n3-> BUSCA MAIOR OU MENOR\n4-> IMPRESSÃO ORDENADA\n\n" + color.DARKCYAN + "Informe uma opcao: " + color.END))
            
            #detalhar registro
            if option_btKey == 1:
                system("clear")
                item_name = float(input(color.DARKCYAN + "Informe o valor da chave: " + color.END))
                index = tree_keyPrice.search_bt(tree_keyPrice.root, item_name)
                return_dataIndex(index)

                system("pause")

            #busca por intervalo
            elif option_btKey == 2:
                value_0 = float(input(color.DARKCYAN + "Informe o valor inicial: " + color.END))
                value_1 = float(input(color.DARKCYAN + "Informe o valor final: " + color.END))
                tree_keyPrice.seach_by_interval(tree_keyPrice.root, value_0, value_1)

                system("pause")
            
            #maior ou menor
            elif option_btKey == 3:
                value = float(input(color.DARKCYAN + "Informe o valor referencia: " + color.END))
                ty = input(color.DARKCYAN + "Maior ou Menor: " + color.END)
                tree_keyPrice.seach_by_value(tree_keyPrice.root, value, ty)

                system("pause")

            
            #impressao ordenada
            elif option_btKey == 4:
                tree_keyPrice.seq_press(tree_keyPrice.root)

                system("pause")

        #4.2) chave alfabética
        elif option_bt == 2:
            system("clear")
            option_btKey = int(input(color.BOLD + "1-> DETALHAR REGISTRO\n2-> IMPRESSÃO ORDENADA\n\n" + color.DARKCYAN + "Informe uma opcao: " + color.END))
            
            #detalhar registro
            if option_btKey == 1:
                system("clear")
                item_name = input(color.DARKCYAN + "Informe o nome da chave: " + color.END)
                item_name = item_name.upper()
                index = tree_keyName.search_bt(tree_keyName.root, item_name)
                return_dataIndex(index)

                system("pause")
            
            #impressao ordenada
            elif option_btKey == 2:
                tree_keyName.seq_press(tree_keyName.root)

                system("pause")

        #4.3) chave tipo de proteína
        elif option_bt == 3:
            system("clear")
            option_btKey = int(input(color.BOLD + "1-> DETALHAR REGISTRO\n2-> IMPRESSÃO ORDENADA\n\n" + color.DARKCYAN + "Informe uma opcao: " + color.END))
            system("clear")
            option_btProtein = int(input(color.BOLD + "1-> TIPO CARNE\n2-> TIPO PEIXE\n3-> TIPO VEGANO\n\n" + color.DARKCYAN + "Informe uma opcao: " + color.END))

            #detalhar registro
            if option_btKey == 1:
                system("clear")
                item_name = input(color.DARKCYAN + "Informe o nome da chave: " + color.END)
                item_name = item_name.upper()

                if option_btProtein == 1:
                    index = tree_carne.search_bt(tree_carne.root, item_name)
                    return_dataIndex(index)

                elif option_btProtein == 2:
                    index = tree_peixe.search_bt(tree_peixe.root, item_name)
                    return_dataIndex(index)

                elif option_btProtein == 3:
                    index = tree_vegano.search_bt(tree_vegano.root, item_name)
                    return_dataIndex(index)

                system("pause")

            #impressao ordenada
            elif option_btKey == 2:
                if option_btProtein == 1:
                    tree_carne.seq_press(tree_carne.root)

                elif option_btProtein == 2:
                    tree_peixe.seq_press(tree_peixe.root)

                elif option_btProtein == 3:
                    tree_vegano.seq_press(tree_vegano.root)

                system("pause")

    tree_keyName = btree_creator("name")
    tree_keyPrice = btree_creator("price")
    tree_carne, tree_peixe, tree_vegano = btree_typeProtein()
    #end while