class Bill:
    def __init__(self, date, customer_name):
        self.date = date
        self.customer_name = customer_name
        self.items = []

    def add_item(self, item_name, rate, quantity):
        total_amount = rate * quantity
        item_details = {
            'item_name': item_name,
            'rate': rate,
            'quantity': quantity,
            'total_amount': total_amount
        }
        self.items.append(item_details)

    def display_bill(self):
        print("Customer Bill")
        print("Date:", self.date)
        print("Customer Name:", self.customer_name)
        print("-------------------------------------------------------")
        print("{:<20} {:<10} {:<10} {:<15}".format("Item Name", "Rate", "Quantity", "Total Amount"))
        print("-------------------------------------------------------")
        for item in self.items:
            print("{:<20} {:<10.2f} {:<10} {:<15.2f}".format(item['item_name'], item['rate'], item['quantity'], item['total_amount']))
        print("-------------------------------------------------------")
        total_bill_amount = sum(item['total_amount'] for item in self.items)
        print("Total Bill Amount:", total_bill_amount)
if __name__ == "__main__":
    bill = Bill(date="2023-07-20", customer_name="John Doe")
    bill.add_item("Item 1", rate=10, quantity=2)
    bill.add_item("Item 2", rate=20, quantity=3)
    bill.add_item("Item 3", rate=30, quantity=1)
    bill.display_bill()
