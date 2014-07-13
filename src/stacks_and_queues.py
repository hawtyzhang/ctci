#def allocate_three_stacks(array):
class MinStackNode(object):
    def __init__(self, val, min_val):
        self.val = val
        self.min = min([min_val, val])
        self.next = None

    def __str__(self):
        return str(self.val)

class MinStack(object):
    def __init__(self, vals=None):
        self.top = None
        if not vals is None:
            for val in vals:
                self.push(val)

    def push(self, val):
        if self.is_empty():
            node = MinStackNode(val, val)
        else:
            node = MinStackNode(val, self.top.min)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top == None:
            return None
        val = self.top.val
        self.top = self.top.next
        return val

    def min(self):
        return self.top.min

    def is_empty(self):
        return self.top is None

def hanoi(level):

    def move_top(level, src, dest):
        print "move %d from %s to %s" % (level, src, dest)
    
    def move(level, src, dest, buf):
        if level == 0:
            return
        move(level-1, src, buf, dest)
        move_top(level, src, dest)
        move(level-1, buf, dest, src)

    return move(level, "p0", "p1", "p2")

class TwoStackQueue():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, val):
        self.stack1.append(val)

    def dequeue(self):
        if len(self.stack2):
            return self.stack2.pop()
        while len(self.stack1):
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def size(self):
        return len(self.stack1) + len(self.stack2)

def sort_stack(stack):
    sorted_stack = []
    while len(stack):
        last = stack.pop()
        while len(sorted_stack) and last > sorted_stack[-1]:
            stack.append(sorted_stack.pop())
        sorted_stack.append(last)
    return sorted_stack

def test2():
    stack = MinStack([4, 4, 3, 2, 1, 3])
    print stack.min()
    stack.pop()
    print stack.min()
    stack.pop()
    print stack.min()

def test4():
    hanoi(3)

def test5():
    queue = TwoStackQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print queue.dequeue()
    print queue.dequeue()
    queue.enqueue(5)
    queue.enqueue(6)
    print queue.dequeue()
    print queue.dequeue()

def test6():
    print sort_stack([3,2,1,5,4,9,3,3,2,9,6])

#test2()
#test4()
#test5()
test6()

