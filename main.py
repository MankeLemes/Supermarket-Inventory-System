# Variables, lists and dictionaries
products = {}
history = []

# 1st Function - Register Product
def registerProduct(products, history):

    product_name = input("\nEnter the product name: ")

    if product_name in products:
        print("\nProduct already registered!")

    else:

        product_price = float(input("Enter the product price: $ "))

        if product_price <= 0:
            print("\nInvalid price!")
            return products

        stock_quantity = int(input("Enter stock quantity: "))

        if stock_quantity < 0:
            print("\nInvalid quantity!")
            return products

        category = input("Category: ")
        supplier = input("Supplier: ")

        products[product_name] = {
            "price": product_price,
            "stock": stock_quantity,
            "category": category,
            "supplier": supplier
        }

        history.append({
            "type": "Registration",
            "product": product_name,
            "price": product_price,
            "quantity": stock_quantity
        })

        print("\nProduct successfully registered!")

    return products


# 2nd Function - View Products
def viewProducts(products):

    if len(products) == 0:
        print("\nNo products registered!")

    else:
        for product, data in products.items():

            print(f"\nProduct: {product}")
            print(f"Price: ${data['price']:.2f}")
            print(f"Stock: {data['stock']}")
            print(f"Category: {data['category']}")
            print(f"Supplier: {data['supplier']}")


# 3rd Function - Search Product
def searchProduct(products):

    if len(products) == 0:
        print("\nNo products registered!")

    else:
        searched_product = input("\nWhich product would you like to search for? ")

        if searched_product in products:

            product = products[searched_product]

            print(f"\nProduct: {searched_product}")
            print(f"Price: ${product['price']:.2f}")
            print(f"Stock: {product['stock']}")
            print(f"Category: {product['category']}")
            print(f"Supplier: {product['supplier']}")

        else:
            print("\nProduct not found!")


# 4th Function - Update Product
def updateProduct(products, history):

    if len(products) == 0:
        print("\nNo products registered!")

    else:
        product_to_update = input("Which product would you like to update? ")

        if product_to_update in products:

            product = products[product_to_update]

            product['price'] = float(input("Enter the new price: $ "))
            product['stock'] = int(input("Enter the new stock quantity: "))
            product['category'] = input("Enter the new category: ")
            product['supplier'] = input("Enter the new supplier: ")

            print("\nProduct updated successfully!")

            history.append({
                "type": "Update",
                "product": product_to_update,
                "new_price": product['price']
            })

        else:
            print("\nProduct not found!")

    return products

# 5th Function - Delete Product
def deleteProduct(products, history):

    if len(products) == 0:
        print("\nNo products registered!")

    else:
        product_to_delete = input("Which product would you like to delete? ")

        if product_to_delete in products:

            del products[product_to_delete]

            print("\nProduct successfully deleted!")

            history.append({
                "type": "Deletion",
                "product": product_to_delete
            })

        else:
            print("\nProduct not found!")

    return products


# 6th Function - Add Stock
def addStock(products, history):

    if len(products) == 0:
        print("\nNo products registered!")

    else:
        product_to_add = input("Which product would you like to restock? ")

        if product_to_add in products:

            product = products[product_to_add]

            added_quantity = int(input("How many units would you like to add? "))

            if added_quantity <= 0:
                print("\nInvalid quantity!")

            else:

                product['stock'] += added_quantity

                print(f"\nProduct: {product_to_add}")
                print(f"Quantity Added: {added_quantity}")
                print(f"Current Stock: {product['stock']}")

                history.append({
                    "type": "Stock Entry",
                    "product": product_to_add,
                    "quantity": added_quantity
                })

        else:
            print("\nProduct not found!")

    return products


# 7th Function - Register Sale
def registerSale(products, history):

    if len(products) == 0:
        print("\nNo products registered!")

    else:
        sold_product = input("\nWhich product was sold? ")

        if sold_product in products:

            product = products[sold_product]

            sold_quantity = int(input(f"How many units of {sold_product} were sold? "))

            if sold_quantity <= 0:
                print("\nInvalid quantity!")

            else:

                if sold_quantity > product['stock']:
                    print("\nInsufficient stock!")

                else:

                    product['stock'] -= sold_quantity

                    print(f"\nProduct: {sold_product}")
                    print(f"Quantity Sold: {sold_quantity}")
                    print(f"Current Stock: {product['stock']}")
                    print("Sale successfully registered!")

                    history.append({
                        "type": "Sale",
                        "product": sold_product,
                        "quantity": sold_quantity
                    })

    return products


# 8th Function - View Transaction History
def viewHistory(history):

    if len(history) == 0:
        print("\nNo transactions recorded!")

    else:

        print("\n========== TRANSACTION HISTORY ==========")

        for transaction in history:

            print(f"\nType: {transaction['type']}")
            print(f"Product: {transaction['product']}")

            if 'quantity' in transaction:
                print(f"Quantity: {transaction['quantity']}")

            if 'price' in transaction:
                print(f"Price: ${transaction['price']:.2f}")

            if 'new_price' in transaction:
                print(f"New Price: ${transaction['new_price']:.2f}")


# 9th Function - Reports Menu
def reportsMenu():

# Reports Menu
    while True:

        print("\n========== REPORTS ==========")
        print("1 - Most Expensive Product")
        print("2 - Cheapest Product")
        print("3 - Product with Highest Stock")
        print("4 - Product with Lowest Stock")
        print("5 - Total Inventory Value")
        print("6 - Critical Stock Products")
        print("0 - Back")

        option = int(input("\nChoose an option: "))

        if option == 1:
            mostExpensiveProduct(products)

        elif option == 2:
            cheapestProduct(products)

        elif option == 3:
            highestStock(products)

        elif option == 4:
            lowestStock(products)

        elif option == 5:
            totalInventoryValue(products)

        elif option == 6:
            criticalStock(products)

        elif option == 0:
            print("Returning to main menu...")
            break

        else:
            print("Invalid option!")

# Report Option 1 - Most Expensive Product
def mostExpensiveProduct(products):

    highest_price = 0
    most_expensive_product = ""

    if len(products) == 0:
        print("\nNo products registered!")

    else:
        for name, product in products.items():

            if highest_price < product['price']:
                highest_price = product['price']
                most_expensive_product = name

        print(f"\nMost expensive product: {most_expensive_product}")
        print(f"Price: ${highest_price:.2f}")
        print(f"Stock: {products[most_expensive_product]['stock']}")
        print(f"Category: {products[most_expensive_product]['category']}")

# Report Option 2 - Cheapest Product
def cheapestProduct(products):

    lowest_price = float("inf")
    cheapest_product = ""

    if len(products) == 0:
        print("\nNo products registered!")

    else:
        for name, product in products.items():

            if lowest_price > product['price']:
                lowest_price = product['price']
                cheapest_product = name

        print(f"\nCheapest product: {cheapest_product}")
        print(f"Price: ${lowest_price:.2f}")
        print(f"Stock: {products[cheapest_product]['stock']}")
        print(f"Category: {products[cheapest_product]['category']}")

# Report Option 3 - Product with Highest Stock
def highestStock(products):

    highest_stock = 0
    product_highest_stock = ''

    if len(products) == 0:
        print("\nNo products registered!")

    else:
        for name, product in products.items():

            if highest_stock < product['stock']:
                highest_stock = product['stock']
                product_highest_stock = name

        print(f"\nProduct with highest stock: {product_highest_stock}")
        print(f"Price: ${products[product_highest_stock]['price']:.2f}")
        print(f"Stock: {products[product_highest_stock]['stock']}")
        print(f"Category: {products[product_highest_stock]['category']}")


# Report Option 4 - Product with Lowest Stock
def lowestStock(products):

    lowest_stock = float("inf")
    product_lowest_stock = ''

    if len(products) == 0:
        print("\nNo products registered!")

    else:
        for name, product in products.items():

            if lowest_stock > product['stock']:
                lowest_stock = product['stock']
                product_lowest_stock = name

        print(f"\nProduct with Lowest Stock: {product_lowest_stock}")
        print(f"Price: ${products[product_lowest_stock]['price']:.2f}")
        print(f"Stock: {products[product_lowest_stock]['stock']}")
        print(f"Category: {products[product_lowest_stock]['category']}")

# Report Option 5 - Total Inventory Value
def totalInventoryValue(products):

    total_value = 0

    if len(products) == 0:
        print("\nNo products registered!")

    else:
        for name, product in products.items():
            total_value += product['price'] * product['stock']

        print("\n========== TOTAL INVENTORY VALUE ==========")
        print(f"${total_value:.2f}")

# Report Option 6 - Critical Stock Products
def criticalStock(products):

    found = False

    if len(products) == 0:
        print("\nNo products registered!")

    else:

        print("\n========== CRITICAL STOCK PRODUCTS ==========")

        for name, product in products.items():

            if product['stock'] <= 5:

                found = True

                print(f"Product: {name}")
                print(f"Stock: {product['stock']}")
                print("-" * 30)

        if not found:
            print("No products with critical stock.")

# Main Menu
while True:

    print("\n========== INVENTORY MANAGEMENT SYSTEM ==========")
    print("1 - Register Product")
    print("2 - View All Products")
    print("3 - Search Product")
    print("4 - Update Product")
    print("5 - Delete Product")
    print("6 - Add Stock")
    print("7 - Register Sale")
    print("8 - View Movement History")
    print("9 - Reports")
    print("0 - Exit")

    option = input("\nChoose an option: ")

    if option == "1":
        products = registerProduct(products, history)

    elif option == "2":
        viewProducts(products)

    elif option == "3":
        searchProduct(products)

    elif option == "4":
        updateProduct(products, history)

    elif option == "5":
        deleteProduct(products, history)

    elif option == "6":
        addStock(products, history)

    elif option == "7":
        registerSale(products, history)

    elif option == "8":
        viewHistory(history)

    elif option == "9":
        reportsMenu()

    elif option == "0":
        print("\nClosing system...")
        break

    else:
        print("\nInvalid option!")
