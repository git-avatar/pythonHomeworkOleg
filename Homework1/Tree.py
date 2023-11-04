layers = int(input("Enter the number of layers"))
tree_trunk_size = int(input("Size of the tree trunk"))
for i in range(1, layers + 1):
    spaces = " " * (layers - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)


for i in range(tree_trunk_size):
    print("  " * (layers//2) + "|")


