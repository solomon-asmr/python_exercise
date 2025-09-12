class Car:
    def __init__(self, model, price, for_sale):
        self.model=model
        self.price=price
        self.for_sale=for_sale

    def drive(self):
        print(f"you are driving {self.model} car")
    def stop(self):
        print(f"you stopped the {self.model} car")
