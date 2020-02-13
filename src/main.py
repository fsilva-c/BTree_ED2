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
        
    if option is 1:
        system("clear")
        itemRegister()
        tree_carne, tree_peixe, tree_vegano = btree_typeProtein()

    #remoção do item
    elif option is 2:
        system("clear")
        btree = int(input("1-> ÁRVORE NUMÉRICA\n2-> ÁRVORE ALFABÉTICA\n\nInforme uma opção: "))
        
        if btree is 1:
            system("clear")
            key = input("Informe a chave que será removida: ")
            key = key.upper()
            index = tree_keyPrice.search_bt(tree_keyPrice.root, key)

            remove_item(index)
            #recriando a árvore
            tree_keyPrice = btree_creator("price")

        elif btree is 2:
            system("clear")
            key = input("Informe a chave que será removida: ")
            key = key.upper()
            index = tree_keyName.search_bt(tree_keyName.root, key)

            remove_item(index)
            #recriando a árvore
            tree_keyName = btree_creator("name")
        system("pause")

    #alterar registro
    elif option is 3:
        alter_register()
        print("chevrolet")

    #operações da btree
    elif option is 4:
        system("clear")
        option_bt = int(input("1-> ÁRVORE NUMÉRICA\n2-> ÁRVORE ALFABÉTICA\n3-> ÁRVORES TIPO DE PROTEÍNA\n\nInforme uma opção: "))

        #chave numérica
        if option_bt is 1:
            system("clear")
            option_btKey = int(input("1-> DETRALHAR REGISTRO\n2-> BUSCA POR INTERVALO\n3-> BUSCA MAIOR OU MENOR\n4-> IMPRESSÃO ORDENADA\n\nInforme uma opcao: "))
            
            #detalhar registro
            if option_btKey is 1:
                system("clear")
                item_name = input("Informe o valor da chave: ")
                index = tree_keyPrice.search_bt(tree_keyPrice.root, item_name)
                return_dataIndex(index)

                system("pause")

            #busca por intervalo
            elif option_btKey is 2:
                value_0 = input("Informe o valor inicial: ")
                value_1 = input("Informe o valor final: ")
                tree_keyPrice.seach_by_interval(tree_keyPrice.root, value_0, value_1)

                system("pause")
            
            #maior ou menor
            elif option_btKey is 3:
                value = input("Informe o valor referencia: ")
                ty = input("Maior ou menor: ")
                tree_keyPrice.seach_by_value(tree_keyPrice.root, value, ty)

                system("pause")

            
            #impressao ordenada
            elif option_btKey is 4:
                tree_keyPrice.seq_press(tree_keyPrice.root)

                system("pause")

        #chave alfabética
        elif option_bt is 2:
            system("clear")
            option_btKey = int(input("1-> DETALHAR REGISTRO\n2-> IMPRESSÃO ORDENADA\n\nInforme uma opcao: "))
            
            if option_btKey is 1:
                system("clear")
                item_name = input("Informe o nome da chave: ")
                item_name = item_name.upper()
                index = tree_keyName.search_bt(tree_keyName.root, item_name)
                return_dataIndex(index)

                system("pause")
                
            elif option_btKey is 2:
                tree_keyName.seq_press(tree_keyName.root)

                system("pause")

        #chave tipo de proteína
        elif option_bt is 3:
            system("clear")
            option_btKey = int(input("1-> DETALHAR REGISTRO\n2-> IMPRESSÃO ORDENADA\n\nInforme uma opcao: "))
            system("clear")
            option_btProtein = int(input("1-> TIPO CARNE\n2-> TIPO PEIXE\n3-> TIPO VEGANO\n\nInforme uma opcao: "))

            if option_btKey is 1:
                system("clear")
                item_name = input("Informe o nome da chave: ")
                item_name = item_name.upper()

                if option_btProtein is 1:
                    index = tree_carne.search_bt(tree_carne.root, item_name)
                    return_dataIndex(index)

                elif option_btProtein is 2:
                    index = tree_peixe.search_bt(tree_peixe.root, item_name)
                    return_dataIndex(index)

                elif option_btProtein is 3:
                    index = tree_vegano.search_bt(tree_vegano.root, item_name)
                    return_dataIndex(index)

                system("pause")
                
            elif option_btKey is 2:
                if option_btProtein is 1:
                    tree_carne.seq_press(tree_carne.root)

                elif option_btProtein is 2:
                    tree_peixe.seq_press(tree_peixe.root)

                elif option_btProtein is 3:
                    tree_vegano.seq_press(tree_vegano.root)

                system("pause")
