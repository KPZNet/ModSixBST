from BSTree import BSTree
def PL(l = 1):
    for i in range(l):
        print("\n")


keys = [1, 7, 4, 23, 8, 9, 4, 3, 5, 7, 9, 67, 6345, 324]
x = set(keys)
keys = list(set(keys))
print("Input List")
print(keys)
PL()
bst = BSTree()
bst.BuildTree(keys)
bst.print_tree("Initial Tree")
PL()
bst.rebalance()
bst.print_tree("Balanced Tree")


