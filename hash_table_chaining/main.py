from hash_table import HashTable


def main():
    ht = HashTable()

    # Insert 20 key-value pairs and track progress
    for i in range(20):
        ht.insert(i, i * i)
        print(
            f"Insert {i}: size={ht.size}, capacity={ht.capacity}, load factor={ht.load_factor():.3f}"
        )

    print("\nHashTable contents after inserts:")
    print(ht)
    print(f"Load factor: {ht.load_factor():.3f}")

    # Search and delete test
    key_to_test = 5
    print(f"\nSearch key {key_to_test}: {ht.search(key_to_test)}")
    print(f"Delete key {key_to_test}: {ht.delete(key_to_test)}")
    print(f"Search key {key_to_test} after deletion: {ht.search(key_to_test)}")
    print(f"Load factor after deletion: {ht.load_factor():.3f}")



if __name__ == "__main__":
    main()
