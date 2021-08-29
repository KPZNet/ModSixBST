# CSC506 Module 6, Option 1
# Kenneth Ceglia

#Node Class for Binary Search Tree
class BSTNode:

    #Init method for Nodes to set key and payload
    def __init__(self, key, payload=None):
        self.key = key
        self.payload = payload
        #Set default payload is none given
        if payload == None:
            self.payload = "Payload " + str(key)
        #Initialize left and right pointers to None
        self.left = None
        self.right = None

    #Convenience method to print out Node
    def __str__(self):
        return "Node Key:" + str (self.key) + " : " + str(self.payload)

#Binary Search Tree Class
#Wraps up Root Node class into Tree with all methods
class BSTree:
    #root node for tree
    root = None

    #convenience print function to pretty print tree structure
    def __str__(self):
        return self.print_tree()

    #Constructor
    def __init__(self, _root=None):
        if _root != None:
            self.root = _root

    #Build tree from input List array
    #returns root node after building tree
    def BuildTree(self, keys):
        for key in keys:
            self.insert(key)
        return self.root

    #insert a new key
    #duplicates are not added
    def insert(self, key, payload=None):
        def __insert(node, key):
            if node is None:
                return BSTNode (key, payload)
            
            # remove duplicates
            if key == node.key:
                return node
            
            if key < node.key:
                node.left = __insert (node.left, key)
            else:
                node.right = __insert (node.right, key)

            return node

        self.root = __insert (self.root, key)
        return self.root

    #Returns minimum tree key
    def get_min_value_node(self, node):
        current = node
        # loop down to find the leftmost leaf
        while (current.left is not None):
            current = current.left

        return current

    #deletes node with input key
    def delete(self, key):
        def __deleteNode(node, key):
            if node is None:
                return node
            if key < node.key:
                node.left = __deleteNode (node.left, key)
            elif (key > node.key):
                node.right = __deleteNode (node.right, key)
            else:
                if node.left is None:
                    temp = node.right
                    node = None
                    return temp
                elif node.right is None:
                    temp = node.left
                    node = None
                    return temp
                temp = self.get_min_value_node (node.right)
                node.key = temp.key
                node.right = __deleteNode (node.right, temp.key)
            return node

        self.root = __deleteNode (self.root, key)
        return self.root

    #Convenient pretty print support method
    COUNT = [10]
    def __print2DUtil(self, root, space):
        # Base case
        if (root == None):
            return

        space += self.COUNT[0]

        self._BSTree__print2DUtil (root.right, space)

        print ()
        for i in range (self.COUNT[0], space):
            print (end=" ")
        print (root.key)

        self._BSTree__print2DUtil (root.left, space)

    #print entire tree in graphical format
    def print_tree(self, title="BST", val="key", left="left", right="right"):
        def display(root, val=val, left=left, right=right):
            if getattr (root, right) is None and getattr (root, left) is None:
                line = '%s' % getattr (root, val)
                width = len (line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            if getattr (root, right) is None:
                lines, n, p, x = display (getattr (root, left))
                s = '%s' % getattr (root, val)
                u = len (s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            if getattr (root, left) is None:
                lines, n, p, x = display (getattr (root, right))
                s = '%s' % getattr (root, val)
                u = len (s)
                first_line = s + x * '_' + (n - x) * ' '
                second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            left, n, p, x = display (getattr (root, left))
            right, m, q, y = display (getattr (root, right))
            s = '%s' % getattr (root, val)
            u = len (s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip (left, right)
            lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max (p, q) + 2, n + u // 2

        if self.root is None:
            return
        lines, *_ = display (self.root, val, left, right)
        print(title)
        for line in lines:
            print (line)

    #balance the tree
    def rebalance(self):
        def storeBSTNodes(root, nodes):
            if not root:
                return
            storeBSTNodes (root.left, nodes)
            nodes.append (root)
            storeBSTNodes (root.right, nodes)
            
        def buildTreeUtil(nodes, start, end):
            if start > end:
                return None

            mid = (start + end) // 2
            node = nodes[mid]

            node.left = buildTreeUtil (nodes, start, mid - 1)
            node.right = buildTreeUtil (nodes, mid + 1, end)
            return node
        #gets nodes in order
        #re-add in middle out fashion to build new balanced tree
        nodes = []
        storeBSTNodes (self.root, nodes)
        n = len (nodes)
        self.root = buildTreeUtil (nodes, 0, n - 1)

    #print out nodes in key order ascending
    def inorder(self):

        def __inorder(node, d):
            if node is not None:
                __inorder (node.left, d)
                d.append (node)
                __inorder (node.right, d)

        d = []
        __inorder (self.root, d)
        return [i.payload for i in d]

    #Bonus method to search and return data value
    def compare_data(self, dataValue):

        def __inorder(node, d, data):
            if node is not None:
                __inorder (node.left, d, data)
                if node.payload == data:
                    d.append (node)
                __inorder (node.right, d, data)

        d = []
        __inorder (self.root, d, dataValue)
        return d


