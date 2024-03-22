dict_menu = {
    1001 : {
        "Product" : "Espresso",
        "Stock" : "Available",
        "Cogs" : 5000,
        "Price" : 10000,
        "Ingredients": {
            "coffee" : 1,
            "water" : 1
        }
    },
    1002 : {
        "Product" : "Long Black",
        "Stock" : "Available",
        "Cogs" : 7500,
        "Price" : 15000,
        "Ingredients": {
            "coffee" : 2,
            "water" : 1
        }
    },
    1003 : {
        "Product" : "Flat White",
        "Stock" : "Available",
        "Cogs" : 10000,
        "Price" : 20000,
        "Ingredients": {
            "coffee" : 2,
            "water" : 1
        }
    },
    1004: {
        "Product" : "Pour Over",
        "Stock" : "Available",
        "Cogs" : 15000,
        "Price" : 25000,
        "Ingredients": {
            "coffee" : 2,
            "water" : 2
        }
    }
}

stock_ingredients = {
    "coffee" : 10,
    "water" : 10
}

dict_cart = {}

def stock_availability(dict_menu):
    for i in dict_menu:
        for j in dict_menu[i]["Ingredients"]:
            if dict_menu[i]["Ingredients"][j] <= stock_ingredients[j]:
                dict_menu[i]["Stock"] = "Available"
            else:
                dict_menu[i]["Stock"] = "Not Available"
                break

def menu():
    print(f'\n{"LixSooyaaa Coffee Shop Menu":^80}')
    print(f'\n{"Code":^10} | {"Product":^20} | {"Stock":^20} | {"Cogs":^15} | {"Price":^14}')
    for i in dict_menu: 
        menu_cogs = (f'{dict_menu[i]["Cogs"]:,}')
        menu_price = (f'{dict_menu[i]["Price"]:,}')
        print(f'{i:^10} | {dict_menu[i]["Product"]:^20} | {dict_menu[i]["Stock"]:^20} | {menu_cogs:^15} | {menu_price:^15}')

def ingredients():
    print(f'\n{"Ingredients":^20} | {"Stock":^10}')
    for i in stock_ingredients:
        print(f'{i.title():^20} | {stock_ingredients[i]:^9}')

def main_menu(): 
    print("\nWelcome to LixSooyaaa Coffee Shop")
    print("""
        List:
        1. Display Data
        2. Add Data  
        3. Update Data
        4. Delete Data
        5. Transaction
        6. Exit Program
        """)

def user_input():
    user_input = int(input("\nPlease input a number from list above\t: "))
    return user_input

def user_input_2():
    user_input_2 = int(input("\nPlease input a number\t: "))
    return user_input_2

def option_1():
     print("""\n
    1. Display All Products
    2. Find a Product
    3. Display Inventory
    4. Back to Main Menu
    """)

def option_2():
     print("""\n
    1. Add New Product
    2. Add Stock
    3. Back to Main Menu
    """)
     
def option_3():
     print("""\n
    1. Update Product
    2. Update Recipe
    3. Back to Main Menu
    """)

def option_4():
    print("""\n
    1. Delete Product
    2. Remove Ingredients
    3. Back to Main Menu
    """)

def option_5():
    print("""\n
    1. Transaction
    2. Back to Main Menu
    """)

def recipe():
    for i in dict_menu: 
        if i == code:
            print(f'\n{"Code":^10} | {"Product":^20} | {"Coffee":^15} | {"Water":^15}')
            print(f'{code:^10} | {dict_menu[code]["Product"]:^20} | {dict_menu[code]["Ingredients"]["coffee"]:^15} | {dict_menu[code]["Ingredients"]["water"]:^15}')
            

should_continue = True
while should_continue:

    stock_availability(dict_menu)
    main_menu()

    answer = user_input()


    if answer == 1:

        should_continue_1 = True

        while should_continue_1:  
            option_1()

            try:  
                answer_2 = user_input_2() 

                try:
                    if answer_2 == 1:
                        menu()

                    elif answer_2 == 2:

                        code_wrong = True
                        while code_wrong: 

                            try:
                                code = int(input("Input a code\t: "))
                                for i in dict_menu: 
                                    if i == code:
                                        code_cogs = (f'{dict_menu[i]["Cogs"]:,}')
                                        code_price = (f'{dict_menu[i]["Price"]:,}')
                                        print(f'\n{"Code":^10} | {"Product":^20} | {"Stock":^20} | {"Cogs":^15} \t| {"Price":^14}')
                                        print(f'{i:^10} | {dict_menu[i]["Product"]:^20} | {dict_menu[i]["Stock"]:^20} | {code_cogs:^15} \t| {code_price:^15} ')
                                        code_wrong = False
                                        break
                            
                                if i != code:
                                    print("\nThe data you are looking for does not exist. Please try again!")
                                    continue
                                
                            except:
                                print("\nValue Error. Please try again!")
                                break
                    
                    elif answer_2 == 3:
                        ingredients()

                    elif answer_2 == 4:
                        break

                    else: 
                        print("\nYou entered invalid input. Please try again!")

                except:
                    print("\nValue Error. Please try again!")
                    should_continue_1 = True
                    break
            
            except:
                print("\nValue Error. Please try again!")


        elif answer == 2:
            
            should_continue_2 = True
            while should_continue_2:

                menu()
                option_2()

                try:  
                    answer_2 = user_input_2() 

                    try:
                        if answer_2 == 1:
                        
                            choice_2_continue = True
                            while choice_2_continue:

                                input_code = True
                                while input_code:
                                    code = int(input("Input Product's Code\t\t: "))
                                    should_input_2 = 0
                                    for i in dict_menu:
                                        if i == code:
                                            print("\nThe code already exists. Please input another code!")
                                            should_input_2 += 1
                                        else:
                                            pass

                                    if should_input_2 == 0:
                                        break
                                    elif should_input_2 != 0:
                                        continue

                                checking_alpha = True
                                while checking_alpha:
                                    product = input("\nInput Product's Name\t\t: ").title()
                                
                                    input_product = True
                                    while input_product:
                                        should_input_2 = 0
                                        for i in dict_menu:
                                            if dict_menu[i]["Product"] == product:
                                                print("\nThe product name already exists. Please input another name!")
                                                should_input_2 += 1
                                                product = input("Input Product's Name\t\t: ").title()
                                                continue
                                            else:
                                                pass

                                        if should_input_2 == 0:
                                            break
                                        elif should_input_2 != 0:
                                            continue
                                    
                                    product_alpha = (product.replace(" ","i",3))
                                    if product_alpha.isalpha():
                                        break
                                    else:
                                        print("\nYou entered invalid input. Please try again!")
                                        continue
                                
                                cogs = int(input("\nInput Cost of Goods Sold\t: "))
                                price = int(input("\nInput Product Price\t\t: "))
                                ingredients_coffee = int(input("\nInput how much coffee is needed\t: "))
                                ingredients_water = int(input("\nInput how much water is needed\t: "))

                                saving = True
                                while saving:
                                    save_data = input("\nDo you want to save the data? yes or no? ").lower()
                                    if save_data == "yes":
                                        dict_menu[code] = {"Product" : product.title(), "Stock" : "Available", "Cogs" : cogs, "Price" : price, "Ingredients" : {"coffee" : ingredients_coffee, "water" : ingredients_water}}
                                        print("\nData successfully saved!")
                                        stock_availability(dict_menu)
                                        menu()
                                        break
                                    elif save_data == "no":
                                        break
                                    else:
                                        print("\nYou entered invalid input. Please try again!")
                                        continue
                                
                                want_continue = input("\nDo you want to continue adding a new Product? yes or no? ").lower()
                                if want_continue == "yes":
                                    continue
                                elif want_continue == "no":
                                    break
                        
                        elif answer_2 == 2: 

                            want_add_more = True
                            while want_add_more:

                                add_stock = input("\nWhat ingredients do you want to add? coffee or water? ").lower()

                                if add_stock == "coffee":
                                    amount_coffee = int(input("Input amount of coffee\t: "))
                                    save_data = input("\nDo you want to save the data? yes or no? ").lower()
                                    if save_data == "yes":
                                        stock_ingredients["coffee"] += amount_coffee
                                        print("\nData successfully saved!")
                                        ingredients()
                                        want_add_more  = False
                                    elif save_data == "no":
                                        want_add_more = True
                                    else: 
                                        print("\nYou entered invalid input. Please try again!")
                                        break

                                    add_more = input("\nDo you want to add more ingredients? yes or no? ").lower()
                                    if add_more == "yes":
                                        want_add_more  = True
                                    elif add_more == "no": 
                                        want_add_more  = False
                                    else: 
                                        print("\nYou entered invalid input. Please try again!")
                                        break

                                elif add_stock == "water":
                                    amount_water = int(input("Input amount of water\t: "))
                                    save_data = input("\nDo you want to save the data? yes or no? ").lower()
                                    if save_data == "yes":
                                        stock_ingredients["water"] += amount_water
                                        print("\nData successfully saved!")
                                        ingredients()
                                        want_add_more  = False
                                    elif save_data == "no":
                                        want_add_more = True
                                    else:
                                        print("\nYou entered invalid input. Please try again!")
                                        break
                            
                                    add_more = input("\nDo you want to add more ingredients? yes or no? " ).lower()
                                    if add_more == "yes":
                                        want_add_more  = True
                                    elif add_more == "no": 
                                        want_add_more  = False
                                    else: 
                                        print("\nYou entered invalid input. Please try again!")
                                        break

                                else:
                                    print("\nYou entered invalid input. Please try again!")
                                    break
                                
                            stock_availability(dict_menu)

                            ingredients()

                        elif answer_2 == 3:
                            break
                        
                        else: 
                            print("\nYou entered invalid input. Please try again!")
                        
                    except:
                        print("\nValue Error. Please try again!")

                except:
                    print("\nValue Error. Please try again!")

                        elif answer_2 == 3:
                            break
                        
                        else: 
                            print("\nYou entered invalid input. Please try again!")
                        
                    except:
                        print("\nValue Error. Please try again!")

                except:
                    print("\nValue Error. Please try again!")


    elif answer == 3:
            
            should_continue_3 = True
            while should_continue_3:

                menu()
                option_3()
            
                try:  
                    answer_3 = user_input_2()   

                    try:
                        if answer_3 == 1:

                            code_wrong = True
                            while code_wrong: 
                                code = int(input("Input a code\t: "))
                                for i in dict_menu: 
                                    if i == code:
                                        code_cogs = (f'{dict_menu[i]["Cogs"]:,}')
                                        code_price = (f'{dict_menu[i]["Price"]:,}')
                                        print(f'\n{"Code":^10} | {"Product":^20} | {"Stock":^20} | {"Cogs":^15} \t| {"Price":^14}')
                                        print(f'{i:^10} | {dict_menu[i]["Product"]:^20} | {dict_menu[i]["Stock"]:^20} | {code_cogs:^15} \t| {code_price:^15} ')
                                        code_wrong = False
                                        break
                                
                                if i != code:
                                    print("The data does not exist. Please try again!")
                                    continue

                    
                            updating = True
                            while updating:
                                continue_update = input("\nDo you want continue update the data? yes or no? ").lower()
                                
                                if continue_update == "yes":
                                    updating_colomn = True
                                    
                                elif continue_update == "no":
                                    break
                                
                                else:
                                    print("\nYou entered invalid input. Please try again!")
                                    break
                                
                                update_column = input("\nName of the column you want to change (except Code & Stock)\t: ").title()

                                if update_column == "Product":
                                        
                                    update_product = True
                                    while update_product:
                                        should_input_3 = 0
                                        update_data_str = input("\nData is changed to\t: ").title()
                                        
                                        for i in dict_menu:
                                            if update_data_str == dict_menu[i]["Product"]:
                                                print("The product name already exists. Please input another name!")
                                                should_input_3 += 1
                                                continue
                                            
                                            else:
                                                pass

                                        if should_input_3 == 0:
                                            break
                                        elif should_input_3 != 0:
                                            continue   
                                                    

                                    saving_update = True
                                    while saving_update:
                        
                                        save_data = input("\nDo you want to save the data? yes or no? ").lower()
                                        if save_data == "yes":
                                            dict_menu[code][update_column] = update_data_str
                                            print("\nData successfully updated!")

                                            updating_colomn = False
                                            updating = False
                                            break
                                        
                                        elif save_data == "no":
                                            updating_colomn = False
                                            updating = False
                                            break

                                        else:
                                            print("\nYou entered invalid input. Please try again!")
                                            updating_colomn = False
                                            updating = False
                                            break


                                elif update_column == "Cogs" or update_column == "Price":

                                    for i in dict_menu[code]:
                                        if update_column == i:
                                                update_data_int = int(input("\nData is changed to\t: "))
                                                save_data = input("\nDo you want to save the data? yes or no? ").lower()
                                                
                                                if save_data == "yes":
                                                    dict_menu[code][update_column] = update_data_int
                                                    print("\nData successfully updated!")

                                                    updating_colomn = False
                                                    updating = False
                                                    break
                                                
                                                elif save_data == "no":
                                                    updating_colomn = False
                                                    updating = False
                                                    break

                                                else:
                                                    print("\nYou entered invalid input. Please try again!")
                                                    updating_colomn = False
                                                    updating = False
                                                    break

                                        
                                else:
                                    print("Colomn you are looking for does not exist. Please try again!")

                        
                        elif answer_3 == 2:

                            code_wrong = True
                            while code_wrong: 
                                
                                code = int(input("Input a code\t: "))
                                for i in dict_menu: 
                                    if i == code:
                                        recipe()
                                        code_wrong = False
                                        break
                                
                                if i != code:
                                    print("The data does not exist. Please try again!")
                                    code_wrong = True

                            updating = True
                            while updating:

                                continue_update = input("\nDo you want continue update the data? yes or no? ").lower()
                                if continue_update == "yes":
                                    updating_ingredients = True
                                elif continue_update == "no":
                                    break
                                else:
                                    print("\nYou entered invalid input. Please try again!")
                                    break
        
                    
                                updating_ingredients = True
                                while updating_ingredients:

                                    update_column_ingredients = input("\nName of the column you want to change (coffee or water)\t: ").lower()
    
                                    if update_column_ingredients == "coffee" or update_column_ingredients == "water":

                                            for i in dict_menu[code]["Ingredients"]:
                                                if i == "coffee" or "water":
                                                        update_data_int = int(input("\nData is changed to\t: "))

                                                        save_data = input("\nDo you want to save the data? yes or no? ").lower()
                                                        
                                                        if save_data == "yes":
                                                            dict_menu[code]["Ingredients"][update_column_ingredients] = update_data_int
                                                            print("\nData successfully updated!")
                                                            print("\nUpdated Recipe")
                                                            recipe()
                                                        
                                                            stock_availability(dict_menu)
                                                            updating_ingredients = False
                                                            break
                                                        
                                                        elif save_data == "no":
                                                            recipe()

                                                            updating_ingredients= False
                                                            break

                                                        else: 
                                                            print("\nYou entered invalid input. Please try again!")
                                                            updating_ingredients = False
                                                            updating = False
                                                            break                                                       

                                    else:
                                        print("Colomn you are looking for does not exist. Please try again!")
                                        break

                        elif answer_3 == 3:
                            break
                    
                        else: 
                            print("\nYou entered invalid input. Please try again!")
                    
                    except:
                        print("\nValue Error. Please try again!")

                except:
                    print("\nValue Error. Please try again!")       


    elif answer == 4:
            
            should_continue_4 = True
            while should_continue_4:

                stock_availability(dict_menu)
                menu()
                option_4()

                try:
                    answer_4 = user_input_2() 

                    if answer_4 == 1:

                        code_wrong = True
                        while code_wrong: 

                            code = int(input("Input a code\t: "))
                            for i in dict_menu: 
                                if i == code:
                                    code_cogs = (f'{dict_menu[i]["Cogs"]:,}')
                                    code_price = (f'{dict_menu[i]["Price"]:,}')

                                    print(f'\n{"Code":^10} | {"Product":^20} | {"Stock":^20} | {"Cogs":^15} \t| {"Price":^14}')
                                    print(f'{i:^10} | {dict_menu[i]["Product"]:^20} | {dict_menu[i]["Stock"]:^20} | {code_cogs:^15} \t| {code_price:^15} ')

                                    code_wrong = False
                                    break
                                
                            if i != code:
                                print("The data does not exist. Please try again!")
                                continue
                            
                        deleting = True
                        while deleting:

                            continue_delete = input("\nDo you want to delete the data? yes or no? ").lower()
                            
                            if continue_delete == "yes":
                                dict_menu.pop(code)
                                print("\nData successfully deleted")
                                break

                            elif continue_delete == "no":
                                break
                            
                            else:
                                print("\nYou entered invalid input. Please try again!")
                                break


                    elif answer_4 == 2:

                        code_wrong = True
                        while code_wrong: 
                            
                            code = int(input("Input a code\t: "))
                            for i in dict_menu: 
                                if i == code:
                                    recipe()
                                    code_wrong = False
                                    break
                            
                            if i != code:
                                print("The data does not exist. Please try again!")
                                code_wrong = True
                            

                        deleting_ingredients = True
                        while  deleting_ingredients:

                            ingredients_deleted = input("\nWhat ingredient do you want to delete? coffee or water? ").lower()

                            if ingredients_deleted == "coffee" or ingredients_deleted == "water":

                                deleting = True
                                while deleting:
                                    continue_delete = input("\nDo you want to delete the data? yes or no? ").lower()

                                    if continue_delete == "yes":
                                            dict_menu[code]["Ingredients"][ingredients_deleted] = 0
                                            print("\nData successfully deleted!")
                                            recipe()
                                            deleting_ingredients = False
                                            break

                                    elif continue_delete == "no":
                                        deleting_ingredients = False
                                        break

                                    else:
                                        print("\nYou entered invalid input. Please try again!")
                                        deleting_ingredients = False
                                        break

                            else:
                                print("\nYou entered invalid input. Please try again!")
                                break

                    elif answer_4 == 3:
                        break

                    else: 
                        print("\nYou entered invalid input. Please try again!")
            
                except:
                    print("\nValue Error. Please try again!")  


        elif answer == 5: 
        should_continue_5 = True
        while should_continue_5:
            
            option_5()
            try:
                answer_5 = user_input_2() 

                choice_5_continue = True
                while choice_5_continue:  

                    if answer_5 == 1:
                        stock_availability(dict_menu)
                        menu()

                        code_wrong = True
                        while code_wrong: 

                            code = int(input("\nPlease input a code of product you want to buy\t: "))

                            for i in dict_menu: 
                                if i == code:
                                    code_cogs = (f'{dict_menu[i]["Cogs"]:,}')
                                    code_price = (f'{dict_menu[i]["Price"]:,}')
                                    print(f'\n{"Code":^10} | {"Product":^20} | {"Stock":^20} | {"Cogs":^15} \t| {"Price":^14}')
                                    print(f'{i:^10} | {dict_menu[i]["Product"]:^20} | {dict_menu[i]["Stock"]:^20} | {code_cogs:^15} \t| {code_price:^15} ')
                                    code_wrong = False
                                    break
                                
                            if i != code:
                                print("\nThe data does not exist. Please try again!")
                                continue
                        
                        adding_cart = True
                        while adding_cart: 

                            stock_availability(dict_menu)

                            product_availability = dict_menu[code]["Stock"]

                            product_name = dict_menu[code]["Product"]

                            if product_availability == "Available":
                                buying_quantity = int(input(f"\nHow many {product_name} do you want to buy? "))

                                total_cogs = dict_menu[code]["Cogs"] * buying_quantity
                                total_price = dict_menu[code]["Price"] * buying_quantity
                                total_coffee_needed = dict_menu[code]["Ingredients"]["coffee"] * buying_quantity
                                total_water_needed = dict_menu[code]["Ingredients"]["water"] * buying_quantity

                                if total_coffee_needed <= stock_ingredients["coffee"] and total_water_needed <= stock_ingredients["water"]:

                                    product_cart = {code : 
                                    {"Product" : product_name, "Stock" : product_availability, "Cogs" : total_cogs, "Price" : total_price, "Quantity" : buying_quantity,
                                    "Ingredients" : {"coffee" : total_coffee_needed, "water" : total_water_needed}}}
                                                                    
                                    dict_cart.update(product_cart)

                                    stock_ingredients["coffee"] -= total_coffee_needed
                                    stock_ingredients["water"] -= total_water_needed

                                    break

                                else:
                                    print("\nSorry, the product is out of stock right now.")
                                    break

                            elif product_availability == "Not Available":
                                print("\nSorry, the product is out of stock right now.")
                                break


                        shopping = True
                        while shopping:
                            continue_shopping = input("\nDo you want to continue shopping? yes or no? ").lower()

                            if continue_shopping == "yes":
                                break
                            
                            elif continue_shopping == "no":
                                pass
                            
                            else:
                                print("\nYou entered invalid input. Please try again!")


                            payment = True 
                            while payment:

                                if dict_cart == {}:
                                    print("\nThank You!")
                                    shopping = False
                                    choice_5_continue = False
                                    should_continue_5 = False
                                    break
                        
                                else:
                                    print(f'\n{"Shopping Cart":^62}')
                                    print(f'{"Product":^20} | {"Quantity":^15} | {"Total Price":^14}')
                                    for i in dict_cart:
                                        price_cart = (f'{dict_cart[i]["Price"]:,}')
                                        print(f'{dict_cart[i]["Product"]:^20} | {dict_cart[i]["Quantity"]:^15} | {price_cart:^15}')

                                    total_payment = 0
                                    total_cogs = 0

                                    for i in dict_cart:
                                        total_payment += dict_cart[i]["Price"]
                                        total_cogs += dict_cart[i]["Cogs"]

                                    should_pay = True
                                    while should_pay:
                                        
                                        print(f"\nThe total payment is {total_payment:,}") 
                                        user_money = int(input("Please input your money = "))

                                        if user_money < total_payment:
                                            print("\nSorry, the amount of money you input is not enough!")

                                        elif user_money == total_payment:
                                            print("\nThank you!")
                                            dict_cart = {}
                                            break
                                        
                                        elif user_money > total_payment:
                                            print("\nThank you!")
                                            print(f"Here's your change = {user_money - total_payment}")
                                            dict_cart = {}
                                            break
                                        
                                        
                                    print(f"\nTotal profit = {total_payment - total_cogs}")

                                    payment = False
                                    shopping = False
                                    adding_cart = False
                                    code_wrong = False
                                    choice_5_continue = False
                                    should_continue_5 = False
                            
                    elif answer_5 == 2:
                        should_continue_5 = False
                        break  

                    else: 
                        print("\nYou entered invalid input. Please try again!")
                        break
            except:
                print("\nValue Error. Please try again!") 

    elif answer == 6:
        want_exit = input("\nDo you want to leave the program? yes or no? ").lower()

        if want_exit == "yes":
            exit()

        elif want_exit == "no":
            should_continue = True

        else:
            print("\nYou entered invalid input. Please try again!")
            should_continue = True
            

    else:
        print("\nThe program menu you are looking for does not exist. Please try again!")





