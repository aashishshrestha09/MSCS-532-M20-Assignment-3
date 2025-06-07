from typing import Any, Optional, List, Tuple
from universal_hash import UniversalHash


class HashTable:
    """
    Hash Table with chaining for collision resolution using universal hashing.
    Supports insert, search, and delete operations with dynamic resizing.
    """

    def __init__(self, initial_capacity: int = 11):
        self.capacity = initial_capacity
        self.size = 0
        self.buckets: List[List[Tuple[Any, Any]]] = [[] for _ in range(self.capacity)]
        self.hasher = UniversalHash(self.capacity)

    def _hash(self, key: Any) -> int:
        """
        Compute hash index for the given key.
        Supports integer keys with universal hashing,
        falls back to built-in hash for other types.
        """
        if isinstance(key, int):
            return self.hasher.hash(key)
        else:
            # Built-in hash for other key types, mod capacity
            return hash(key) % self.capacity

    def insert(self, key: Any, value: Any) -> None:
        """
        Insert or update key-value pair in the hash table.
        Resize if load factor exceeds 0.75.
        """
        index = self._hash(key)
        chain = self.buckets[index]

        for i, (k, _) in enumerate(chain):
            if k == key:
                chain[i] = (key, value)  # Update existing
                return

        chain.append((key, value))
        self.size += 1

        if self.load_factor() > 0.75:
            self._resize()

    def search(self, key: Any) -> Optional[Any]:
        """
        Search for a key and return its value, or None if not found.
        """
        index = self._hash(key)
        for k, v in self.buckets[index]:
            if k == key:
                return v
        return None

    def delete(self, key: Any) -> bool:
        """
        Delete the key-value pair for the given key.
        Returns True if deleted, False if key not found.
        """
        index = self._hash(key)
        chain = self.buckets[index]

        for i, (k, _) in enumerate(chain):
            if k == key:
                del chain[i]
                self.size -= 1
                return True
        return False

    def load_factor(self) -> float:
        """
        Returns current load factor (size / capacity).
        """
        return self.size / self.capacity

    def _resize(self) -> None:
        """
        Resize the hash table to larger capacity and rehash all entries.
        """
        old_capacity = self.capacity
        old_buckets = self.buckets
        self.capacity = self.capacity * 2 + 1  # keep capacity odd
        self.buckets = [[] for _ in range(self.capacity)]
        self.hasher = UniversalHash(self.capacity)
        self.size = 0
        print(f"Resizing table from {old_capacity} to {self.capacity}")

        for chain in old_buckets:
            for key, value in chain:
                self.insert(key, value)

    def __str__(self) -> str:
        """
        String representation showing non-empty buckets.
        """
        return "\n".join(
            f"Bucket {i}: {chain}" for i, chain in enumerate(self.buckets) if chain
        )
