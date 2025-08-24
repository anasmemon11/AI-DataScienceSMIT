import csv
from datetime import datetime

class Order:
    prodcutfile = "Product.csv"
    logfile = "Log.txt"
    setdiscount = 0.0

    def __init__(self):
        self.items = []

    @staticmethod
    def log(message: str):
        with open(Order.logfile, 'a') as log:
            date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            log.write(f"[{date}] {message}\n")

    @classmethod
    def logaction(cls, func):
        def wrapper(self,*args, **kwargs):
            result = func(self,*args, **kwargs)
            cls.log(f"Executed {func.__name__}")
            return result
        return wrapper

    @staticmethod
    def isValidProductId(productid):
        productid = str(productid)
        with open(Order.prodcutfile, 'r') as csvfile:
            for line in csvfile.readlines():
                data = line.strip().split(',')
                if data[0] == productid:
                    return True
        Order.log(f"Invalid product ID attempt: {productid}")
        return False

    def addItemByProductId(self, productid, quantity):
        productid = str(productid)
        if self.isValidProductId(productid):
            with open(Order.prodcutfile, 'r') as csvfile:
                products = [line.strip().split(',') for line in csvfile.readlines()]
                for data in products:
                    if data[0] == productid:
                        price = float(data[2])   # convert price to float
                        self.items.append({
                            'productid': productid,
                            'name': data[1],
                            'quantity': quantity,
                            'price': price
                        })
                        break
        return self.items

    def calculateTotal(self):
        total = sum(item['quantity'] * item['price'] for item in self.items)
        if Order.setdiscount > 0:
            total = total * (1 - Order.setdiscount / 100)
        Order.log(f"Calculated total after discount {total}")
        return total


obj = Order()
obj.addItemByProductId(1, 2)
print("Total:", obj.calculateTotal())
