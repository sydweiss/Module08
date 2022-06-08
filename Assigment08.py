# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# SWeiss,06.07.22 ,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name

        product_price: (float) with the product's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        SWeiss,06.07.22,Modified code to complete assignment 8
    """

    # TODO: Add Code to the Product class
    @staticmethod
    def intialize(file_name = strFileName):
        file = open(file_name, "w")
        for row in lstOfProductObjects:
            file.write(row["Product"] + "," + row["Price"] + "\n")
        file.close()




# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        SWeiss,06.07.22,Modified code to complete assignment 8
    """
    # TODO: Add Code to process data from a file
    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        file = open(file_name, "r")
        for line in file:
            product, price = line.split(",")
            row = {"Product": product.strip(), "Price": price.strip()}
            list_of_rows.append(row)
            file.close()
            return list_of_rows

    @staticmethod
    def add_data_to_list(product, price, list_of_rows) :
        row = {"Product": str(product).strip(), "Price": str(price).strip()}
        list_of_rows.append(row)
        return list_of_rows

    # TODO: Add Code to process data to a file
    @staticmethod
    def remove_data_from_list(product, list_of_rows):
        for row in lstOfProductObjects:
            if row["Product"] == product:
                list_of_rows.remove(row)
                print(" Product has been removed from the list.")
        return list_of_rows

    @staticmethod
    def write_data_to_list(file_name, list_of_rows):
        for row in lstOfProductObjects:
            file = open(file_name, "a")
            file.write(row["Product"] + "," + row["Price"] + "/n")
            file.close()
        return list_of_rows

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    """Perform Input and Output tasks"""
    @staticmethod
    def output_menu_tasks():
            print('''
            Menu of Options
            1) Add a new Product
            2) Remove an exisiting product
            3) Save new products to file
            4) Exit
            ''')
            print()

        # TODO: Add code to get user's choice
    @staticmethod
    def input_menu_choice():
            pick = str(input("Which option you you pick [ 1 to 4] - ")).strip()
            print()
            return pick

        # TODO: Add code to show the current data from the file to user
    @staticmethod
    def output_current_products_in_list(list_of_rows):
        print("**********Current Products************")
        for row in list_of_rows:
            print(row["Product"] + " (" + row["Price"] + ")")
            print("**********")
            print()

        # TODO: Add code to get product data from user
    @staticmethod
    def input_new_products_and_price():
        product = input("Enter Product: ")
        price = input("Enter Price: ")
        return product, price

    @staticmethod
    def input_products_to_be_removed():
        product = input("Which product should be removed? ")
        return product


# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body

# Load data from file into a list of product objects when script starts

# Show user a menu of options

# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program
Product.intialize(file_name=strFileName)
FileProcessor.read_data_from_file(file_name=strFileName, list_of_rows=lstOfProductObjects)
while(True):
    IO.output_current_products_in_list(list_of_rows=lstOfProductObjects)
    IO.output_menu_tasks()
    pick_str = IO.input_menu_choice()

    if pick_str.strip()  ==  '1':
        product, price = IO.input_new_products_and_price()
        lstOfProductObjects = FileProcessor.add_data_to_list(product=product, price=price, list_of_rows=lstOfProductObjects)
        continue

    elif pick_str == '2':
        product = IO.input_products_to_be_removed()
        lstOfProductObjects = FileProcessor.remove_data_from_list(product=product, list_of_rows= lstOfProductObjects)
        continue

    elif pick_str == '3':
        lstOfProductObjects = FileProcessor.write_data_to_list(strFileName, list_of_rows=lstOfProductObjects)
        print("Data Saved")
        continue

    elif pick_str == '4':
        print("Bye")
        break


# Main Body of Script  ---------------------------------------------------- #

