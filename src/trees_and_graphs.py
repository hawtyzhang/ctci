class Tree(object):
    def __init__(self, tree=None):
        if tree is None:
            self.val = None
            self.left = None
            self.right = None
        elif isinstance(tree, list):
            self.val = tree[0]
            self.left = Tree(tree[1])
            self.right = Tree(tree[2])
        elif isinstance(tree, int):
            self.val = tree
            self.left = None
            self.right = None

class GraphNode(object):
    def __init__(self, val):
        self.val = val
        self.neighbors = []

def level_print(root):
    if root == None:
        return
    levels = [[root]]
    while True:
        current_level = []
        for i in levels[-1]:
            if i.left != None:
                current_level.append(i.left)
            if i.right != None:
                current_level.append(i.right)
        if len(current_level) == 0:
            break
        levels.append(current_level)
    for level in levels:
        for node in level:
            print node.val,
        print

def max_height(root):
    if root == None:
        return 0
    return 1 + max([max_height(root.left), max_height(root.right)])

def min_height(root):
    if root == None:
        return 0
    return 1 + min([min_height(root.left), min_height(root.right)])

def is_balance(root):
    return max_height(root) - min_height(root) < 2

def bfs_search(a, b):
    stack = [a]
    visited = {}
    while len(stack):
        node = stack.pop()
        visited[node] = True
        for neigh in node.neighbors:
            if neigh == b:
                return True
            if not neigh in visited:
                stack.append(neigh)
    return False

def create_tree_using_sorted_list(sorted_list):
    if len(sorted_list) == 0:
        return None
    mid = len(sorted_list) / 2
    tree = Tree(sorted_list[mid])
    tree.left = create_tree_using_sorted_list(sorted_list[0:mid])
    tree.right = create_tree_using_sorted_list(sorted_list[mid+1:])
    return tree

def level_list(root):
    if root == None:
        return None
    levels = {0:[root]}
    current = 0
    while len(levels[current]) != 0:
        next_level = []
        for node in levels[current]:
            if node.left != None:
                next_level.append(node.left)
            if node.right != None:
                next_level.append(node.right)
        current += 1
        levels[current] = next_level
    return levels

def find_next(node):
    def left_most(node):
        while node != None:
            node = node.left
        return node
    if node.right != None:
        return left_most(node.right)
    else:
        while node.parent != None:
            if node.parent.left == node:
                return node
            node = node.parent
    return None

def common_ancestor(root, p, q):
    def contain(root, p):
        if root == None:
            return False
        if root == p:
            return True
        return contain(root.left, p) or contain(root.right, p)
    if contain(root.left, p) and contain(root.left, q):
        return common_ancestor(root.left, p, q)
    if contain(root.right, p) and contain(root.right, q):
        return common_ancestor(root.right, p, q)
    return root

def contain_tree(tree1, tree2):
    def match(tree1, tree2):
        if tree2 == None:
            return True
        if tree1 == None:
            return False
        if tree1.val == tree2.val:
            return match(tree1.left, tree2.left) and match(tree1.left, tree2.left)
        return False

    if tree2 == None:
        return True
    if tree1 == None:
        return False
    if tree1.val == tree2.val:
        if match(tree1, tree2):
            return True
    return contain_tree(tree1.left, tree2.left) or contain_tree(tree2.left, tree2.left)

def find_sum(root, total_sum, buf):
    if root == None:
        return
    buf.append(root.val)
    if total_sum == root.val:
        print buf
    find_sum(root.left, total_sum - root.val, buf[:])
    find_sum(root.right, total_sum - root.val, buf[:])


def test1():
    t = Tree([1, [1, 2, 3], 3])
    level_print(t)
    print is_balance(t)

def test2():
    a = GraphNode(1)
    b = GraphNode(2)
    c = GraphNode(3)
    d = GraphNode(4)
    a.neighbors = [b, c]
    b.neighbors = [a]
    c.neighbors = [a]
    print bfs_search(a, c)
    print bfs_search(a, d)

def test3():
    level_print(create_tree_using_sorted_list([1,2,3,4,5,6,7]))

def test4():
    print level_list(create_tree_using_sorted_list([1,2,3,4,5,6,7]))

def test6():
    t = create_tree_using_sorted_list([1,2,3,4,5,6,7])
    print common_ancestor(t, t.left.left, t.right.right).val
    print common_ancestor(t, t.left.right, t.left.left).val

def test8():
    t = create_tree_using_sorted_list([1,2,3,4,5,6,7])
    find_sum(t, 6, [])   

#test1()
#test2()
#test3()
#test4()
#test5()
test8()