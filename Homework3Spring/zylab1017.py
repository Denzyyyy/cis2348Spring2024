#Hughes Izah , PSID 2310365


class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}')


if __name__ == "__main__":
    # Prompt user for two items
    print("Item 1")
    item1_name = input("Enter the item name:\n")
    item1_price = int(input("Enter the item price:\n"))
    item1_quantity = int(input("Enter the item quantity:\n"))
    item1 = ItemToPurchase(item1_name, item1_price, item1_quantity)

    print("\nItem 2")
    item2_name = input("Enter the item name:\n")
    item2_price = int(input("Enter the item price:\n"))
    item2_quantity = int(input("Enter the item quantity:\n"))
    item2 = ItemToPurchase(item2_name, item2_price, item2_quantity)

    # Output individual item costs
    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()

    # Calculate and output total cost
    total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
    print("\nTotal: $" + str(total_cost))
