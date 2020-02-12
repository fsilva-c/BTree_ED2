from menu_prog import *
from key_insert import *
from btree_main import *
 
option = -9
option_bt = -9
option_btKey = -9

tree_keyName = btree_creator("name")
tree_keyPrice = btree_creator("price")

while option != 0:
    system("clear")
    option = int(input("1-> Inserir novo item\n2-> Buscar item\n3-> Eliminar item\n4-> Modificar item\n5-> Operações da BTree\n0-> Sair\nInforme uma opcao: "))
        
    if option == 1:
        system("clear")
        itemRegister()
    elif option == 2:
        print("fiat")

    elif option == 3:
        system("clear")
        remove_item()

    elif option == 5:
        system("clear")
        option_bt = int(input("1-> Chave Numérica\n2-> Chave Alfabética\nInforme uma opção: "))

        #chave numérica
        if option_bt == 1:
            system("clear")
            option_btKey = int(input("1-> Detalhar registro\n2-> Busca por intervalo\n3-> Busca maior ou menor\n4-> Impressão ordenada\nInforme uma opcao: "))
            
            #detalhar registro
            if option_btKey == 1:
                system("clear")
                item_name = input("Informe o valor da chave: ")
                index = tree_keyPrice.search_bt(tree_keyPrice.root, item_name)
                return_dataIndex(index)

                system("pause")

            #busca por intervalo
            elif option_btKey == 2:
                value_0 = input("Informe o valor inicial: ")
                value_1 = input("Informe o valor final: ")
                tree_keyPrice.seach_by_interval(tree_keyPrice.root, value_0, value_1)

                system("pause")
            
            #maior ou menor
            elif option_btKey == 3:
                value = input("Informe o valor referencia: ")
                ty = input("Maior ou menor: ")
                tree_keyPrice.seach_by_value(tree_keyPrice.root, value, ty)

                system("pause")

            
            #impressao ordenada
            elif option_btKey == 4:
                tree_keyPrice.seq_press(tree_keyPrice.root)

        #chave alfabética
        elif option_bt == 2:
            system("clear")
            option_btKey = int(input("1-> DETALHAR REGISTRO\n2-> IMPRESSÃO ORDENADA\nInforme uma opcao: "))
            
            if option_btKey == 1:
                system("clear")
                item_name = input("Informe o nome da chave: ")
                item_name = item_name.upper()
                index = tree_keyName.search_bt(tree_keyName.root, item_name)
                return_dataIndex(index)

                system("pause")
                
            elif option_btKey == 2:
                tree_keyName.seq_press(tree_keyName.root)

                system("pause")
