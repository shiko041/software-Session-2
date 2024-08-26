class ShoppingCart:
    def __init__(self):
        self.itemsName = []
        self.itemsPrice = []
        self.itemsQuantity = []
        self.count = 0

    def add_item(self, item_name, price, quantity):
        for i in range(self.count):
            if self.itemsName[i] == item_name:
                self.itemsQuantity[i] += quantity
                return
        self.itemsName.append(item_name)
        self.itemsPrice.append(price)
        self.itemsQuantity.append(quantity)
        self.count += 1
        
    def remove_item(self, item_name):
        for i in range(self.count):
            if self.itemsName[i] == item_name:
                self.itemsName.pop(i)
                self.itemsPrice.pop(i)
                self.itemsQuantity.pop(i)
                self.count -= 1
                return 
        print("Item not found in list")       

    def calculate_total(self):
        total = 0
        for i in range(self.count):
            total += self.itemsPrice[i] * self.itemsQuantity[i]
        return total

    def display_cart(self):
        if self.count == 0:
            print("The shopping cart is empty.")
        else:
            for i in range(self.count):
                print("Item ",i,": ",self.itemsName[i],", price: ",self.itemsPrice[i],", Quantity: ",self.itemsQuantity[i])
            print(f"Total Cost: ${self.calculate_total():.2f}")

cart = ShoppingCart()
cart.add_item("Apple", 0.99, 3)
cart.add_item("Banana", 0.50, 5)
cart.add_item("Orange", 1.25, 2)

cart.display_cart()

cart.remove_item("Banana")
cart.add_item("Apple", 0.99, 2)
cart.display_cart()

print(f"Total Cost: ${cart.calculate_total():.2f}")
