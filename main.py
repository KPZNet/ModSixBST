from BSTree import BSTree

keys = [1, 7, 4, 23, 8, 9, 4, 3, 5, 7, 9, 67, 6345, 324]
print("Input List")
print(keys)
bst = BSTree()
bst.BuildTree(keys)
bst.print_tree("Initial Tree")
bst.rebalance()
bst.print_tree("Balanced Tree")


