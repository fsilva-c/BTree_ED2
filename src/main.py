from structs_prog import *
from key_insert import *
from btree_creator import *
 
option = -9
option_bt = -9
option_btKey = -9
option_btProtein = -9

tree_keyName = btree_creator("name")
tree_keyPrice = btree_creator("price")
tree_carne, tree_peixe, tree_vegano = btree_typeProtein()

while option != 0:
    system("clear")
    option = int(input("1-> INSERIR NOVO ITEM\n2-> ELIMINAR ITEM\n3-> MODIFICAR ITEM\n4-> OPERAÇÕES DA BTREE\n0-> Sair\n\nInforme uma opcao: "))
        
    #1) inserir registro
    if option == 1:
        system("clear")
        #validando input
        name_item = input("Informe o nome do produto: ")
        name_item = name_item.upper()
        check_name = tree_keyName.search_bt(tree_keyName.root, name_item)

        price_item = input("Informe o preco do produto: ")
        check_price = tree_keyPrice.search_bt(tree_keyPrice.root, price_item)

        itemRegister(name_item, price_item, check_name, check_price)
        system("pause")

    #2) remoção do item
    elif option == 2:
        system("clear")
        btree = int(input("1-> ÁRVORE NUMÉRICA\n2-> ÁRVORE ALFABÉTICA\n\nInforme uma opção: "))
        
        #arvore numérica
        if btree == 1:
            system("clear")
            key = input("Informe a chave que será removida: ")
            key = float(key)
            index = tree_keyPrice.search_bt(tree_keyPrice.root, key)

            remove_item(index)

        #arvore alfabética
        elif btree == 2:
            system("clear")
            key = input("Informe a chave que será removida: ")
            key = key.upper()
            index = tree_keyName.search_bt(tree_keyName.root, key)

            remove_item(index)
            
        system("pause")

    #3) alterar registro
    elif option == 3:
        system("clear")
        btree = int(input("1-> ÁRVORE NUMÉRICA\n2-> ÁRVORE ALFABÉTICA\n\nInforme uma opção: "))

        #arvore numérica
        if btree == 1:
            system("clear")
            key = input("Informe a chave que será alterada: ")
            key = float(key)
            index = tree_keyPrice.search_bt(tree_keyPrice.root, key)
            alter_register(index)
        
        #arvore alfabética
        elif btree == 2:
            system("clear")
            key = input("Informe a chave que será alterada: ")
            key = key.upper()
            index = tree_keyName.search_bt(tree_keyName.root, key)
            alter_register(index)

        system("pause")

    #4) operações da btree
    elif option == 4:
        system("clear")
        option_bt = int(input("1-> ÁRVORE NUMÉRICA\n2-> ÁRVORE ALFABÉTICA\n3-> ÁRVORES TIPO DE PROTEÍNA\n\nInforme uma opção: "))

        #4.1) chave numérica
        if option_bt == 1:
            system("clear")
            option_btKey = int(input("1-> DETALHAR REGISTRO\n2-> BUSCA POR INTERVALO\n3-> BUSCA MAIOR OU MENOR\n4-> IMPRESSÃO ORDENADA\n\nInforme uma opcao: "))
            
            #detalhar registro
            if option_btKey == 1:
                system("clear")
                item_name = float(input("Informe o valor da chave: "))
                index = tree_keyPrice.search_bt(tree_keyPrice.root, item_name)
                return_dataIndex(index)

                system("pause")

            #busca por intervalo
            elif option_btKey == 2:
                value_0 = float(input("Informe o valor inicial: "))
                value_1 = float(input("Informe o valor final: "))
                tree_keyPrice.seach_by_interval(tree_keyPrice.root, value_0, value_1)

                system("pause")
            
            #maior ou menor
            elif option_btKey == 3:
                value = float(input("Informe o valor referencia: "))
                ty = input("Maior ou menor: ")
                tree_keyPrice.seach_by_value(tree_keyPrice.root, value, ty)

                system("pause")

            
            #impressao ordenada
            elif option_btKey == 4:
                tree_keyPrice.seq_press(tree_keyPrice.root)

                system("pause")

        #4.2) chave alfabética
        elif option_bt == 2:
            system("clear")
            option_btKey = int(input("1-> DETALHAR REGISTRO\n2-> IMPRESSÃO ORDENADA\n\nInforme uma opcao: "))
            
            #detalhar registro
            if option_btKey == 1:
                system("clear")
                item_name = input("Informe o nome da chave: ")
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
            option_btKey = int(input("1-> DETALHAR REGISTRO\n2-> IMPRESSÃO ORDENADA\n\nInforme uma opcao: "))
            system("clear")
            option_btProtein = int(input("1-> TIPO CARNE\n2-> TIPO PEIXE\n3-> TIPO VEGANO\n\nInforme uma opcao: "))

            #detalhar registro
            if option_btKey == 1:
                system("clear")
                item_name = input("Informe o nome da chave: ")
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
