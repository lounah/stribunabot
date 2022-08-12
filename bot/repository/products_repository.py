class ProductsRepository:
    def __init__(self):
        self._products = {}

    def add(self, id: str, desc: str):
        self._products[id] = desc

    def get(self, id: str) -> str:
        return self._products[id]
