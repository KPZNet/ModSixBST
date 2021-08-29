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
bst.BuildTreeFromArray(keys)
bst.print_tree("Initial Tree")
bst.rebalance()
PL()
bst.print_tree("Balanced Tree")

PL()
print("Deleting Node value 9...")
bst.delete(9)
bst.print_tree("Updated Tree without 9")

PL()
print("Deleting Node value 67...")
bst.delete(67)
bst.print_tree("Updated Tree without 67")

PL()
print("Adding 9 and 67 back in Tree...")
bst.insert(9)
bst.insert(67)

bst.print_tree("Updated Tree with 9 and 67 added back")

PL()
print("Bonus !!  Compare Node Data...")
nf = bst.compare_data("Payload 5")
nodeFound = None
if nf:
    nodeFound = nf[0]
print("Compared Data to Payload and Found :" + nodeFound.payload)