class Products:
    def __init__(self, products, bonuses=0):
        self.bonuses = bonuses
        self.products = products

    def get_products_price(self):
        return sum(self.products.values()) - self.bonuses

    def __add__(self, other):
        if isinstance(other, int):
            return Products(self.products, self.bonuses + other)
        elif isinstance(other, Products):
            new_products = self.products.copy()
            for product, price in other.products.items():
                if product not in new_products:
                    new_products[product] = price
            return Products(new_products, self.bonuses + other.bonuses)

    def __radd__(self, other):
        if isinstance(other, int):
            return Products(self.products, self.bonuses + other)

    def __sub__(self, other):
        if isinstance(other, int):
            return Products(self.products, self.bonuses - other)
        elif isinstance(other, Products):
            new_products = {
                product: price for product, price in self.products.items()
                if product not in other.products
            }
            new_bonuses = self.bonuses - other.bonuses
            return Products(new_products, new_bonuses)
        else:
            raise TypeError(f"Unsupported operand type(s) for -: 'Products' and '{type(other).__name__}'")

    def __rsub__(self, other):
        if isinstance(other, int):
            return Products(self.products, other - self.bonuses)
        else:
            raise TypeError(f"Unsupported operand type(s) for -: '{type(other).__name__}' and 'Products'")

    def __repr__(self):
        return f"Products(products={self.products}, bonuses={self.bonuses})"


products1 = Products({'Молоко': 3, 'Сыр': 5})
print(f'Цена: {products1.get_products_price()}, {products1.products}')
products2 = Products({'Кефир': 2})
products3 = products1 + products2
print(f'Цена: {products3.get_products_price()}, {products3.products}')
products4 = products3 + 2
print(f'Цена: {products4.get_products_price()}, {products4.products}')
products5 = 1 + products3
print(f'Цена: {products5.get_products_price()}, {products5.products}')
products6 = Products({'Молоко': 3, 'Сыр': 5}, bonuses=2)
products7 = Products({'Сыр': 5}, bonuses=1)
result1 = products6 - products7
print(f'Результат вычитания: {result1}')  # Products(products={'Молоко': 3}, bonuses=1)
result2 = products6 - 1
print(f'Результат вычитания: {result2}')  # Products(products={'Молоко': 3, 'Сыр': 5}, bonuses=1)
result3 = 5 - products6
print(f'Результат вычитания: {result3}')  # Products(products={'Молоко': 3, 'Сыр': 5}, bonuses=3)