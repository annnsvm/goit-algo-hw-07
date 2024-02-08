from task1 import sum_values, Node, insert


if __name__ == "__main__":
    root = Node(5)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 4)
    root = insert(root, 7)
    root = insert(root, 6)
    root = insert(root, 8)
    root = insert(root, 99)

    # root = delete(root, 7)
    # print(root)
    
    
    
# Шукаємо суму в дереві:
    print(sum_values(root))