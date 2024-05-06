#Hughes Izah , PSID 2310365


class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_description(self):
        print(f'{self.item_name}: {self.item_description}')


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2016"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_name, new_quantity):
        for item in self.cart_items:
            if item.item_name == item_name:
                item.item_quantity = new_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_quantity * item.item_price
        return total_cost

    def print_total(self):
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
            return
        total_cost = self.get_cost_of_cart()
        print(f"Total: ${total_cost:.2f}")

    def print_descriptions(self):
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
            return
        print("Item Descriptions:")
        for item in self.cart_items:
            print(item.item_description)


if __name__ == "__main__":
    cart = ShoppingCart()

    print("ADD ITEM TO CART")
    while True:
        print("Enter the item name:")
        item_name = input()
        if item_name == "q":
            break
        print("Enter the item description:")
        item_description = input()
        print("Enter the item price:")
        item_price = int(input())
        print("Enter the item quantity:")
        item_quantity = int(input())

        item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
        cart.add_item(item)

    print("\nMENU")
    while True:
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit\n")

        print("Choose an option:")
        option = input()

        if option == "a":
            print("ADD ITEM TO CART")
            print("Enter the item name:")
            item_name = input()
            if item_name == "q":
                break
            print("Enter the item description:")
            item_description = input()
            print("Enter the item price:")
            item_price = int(input())
            print("Enter the item quantity:")
            item_quantity = int(input())

            item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            cart.add_item(item)

        elif option == "r":
            print("REMOVE ITEM FROM CART")
            print("Enter name of item to remove:")
            item_name = input()
            cart.remove_item(item_name)

        elif option == "c":
            print("CHANGE ITEM QUANTITY")
            print("Enter the item name:")
            item_name = input()
            print("Enter the new quantity:")
            new_quantity = int(input())
            cart.modify_item(item_name, new_quantity)

        elif option == "i":
            cart.print_descriptions()

        elif option == "o":
            print("OUTPUT SHOPPING CART")
            print(f"{cart.customer_name}'s Shopping Cart - {cart.current_date}")
            print(f"Number of Items: {cart.get_num_items_in_cart()}\n")
            total_cost = cart.get_cost_of_cart()
            if total_cost == 0:
                print("SHOPPING CART IS EMPTY")
            else:
                for item in cart.cart_items:
                    print(
                        f"{item.item_name} {item.item_quantity} @ ${item.item_price} = ${item.item_quantity * item.item_price}")
                print(f"\nTotal: ${total_cost:.2f}")

        elif option == "q":
            break
