class Carrinho:
    def __init__(self) -> dict:
        self.shopping_cart = {}

    def adiciona(self, product: str, price: int):
        self.shopping_cart.setdefault(product, []).append(price)

    def total_produto(self, product):
        return sum(self.shopping_cart[product])
