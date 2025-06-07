import random


class UniversalHash:
    """
    Implements a universal hash function family for integers.
    """

    def __init__(self, capacity: int, prime: int = 109345121):
        self.capacity = capacity
        self.p = prime
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)

    def hash(self, key: int) -> int:
        """
        Hash integer key using universal hashing.
        """
        return ((self.a * key + self.b) % self.p) % self.capacity
