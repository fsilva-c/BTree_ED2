def struct_item():
    item = {
        "name" : "NaN",
        "price" : "NaN",
        "igredients" : "NaN",
        "kcal" : "NaN",
        "type_item" : "NaN",
        "type_drink" : "NaN",
        "flavor_drink" : "NaN",
        "type_protein" : "NaN",
        "protein_portion" : "NaN"
    }

    return item

def struct_menu():
    menu_prog = {
        "type_item" : {
            1 : "bebida",
            2 : "comida"
        },

        "type_drink" : {
            1 : "suco",
            2 : "refrigerante",
            3 : "água"
        },

        "type_protein" : {
            1 : "carne",
            2 : "peixe",
            3 : "vegano"
        }
    }

    return menu_prog