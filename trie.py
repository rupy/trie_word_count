
class Trie:

    class Node:
        def __init__(self, data, sibling = None, child = None):
            self.data = data
            self.count = 0
            self.sibling = sibling
            self.child = child

        def set_child(self, data):
            # child moves to sibling
            child = Trie.Node(data, self.child)
            # replace child
            self.child = child
            return child

        def get_child(self, data):
            child = self.child
            # loop until finding node that has exact data
            while child:
                if child.data == data: break
                child = child.sibling
            return child

        def del_child(self, x):
            child = self.child
            if child.data == x:
                self.child = child.sibling # skip
                return True
            else:
                # loop until finding node that has exact data
                while child.bros:
                    if child.bros.data == x:
                        child.bros = child.bros.bros # skip
                        return True
                    child = child.bros
            return False

        def traverse(self, leaf):
            if self.data == leaf:
                yield []
            else:
                # go to child
                child = self.child
                while child:
                    for x in child.traverse(leaf):
                        yield [self.data] + x
                    # go to sibling
                    child = child.sibling


    def __init__(self, x = None):
        self.root = Trie.Node("")    # header
        self.leaf = x

    def search(self, seq):
        node = self.root
        for x in seq:
            node = node.get_child(x)
            if node is None: return False
        # check leaf
        return node.get_child(self.leaf) is not None

    def get_hist(self, seq):
        node = self.root
        for x in seq:
            node = node.get_child(x)
            if node is None: return False
        # check leaf
        if node.get_child(self.leaf) is not None:
            return node.child.count
        else:
            return 0


    def insert(self, seq):
        node = self.root
        for x in seq:
            child = node.get_child(x)
            if not child:
                child = node.set_child(x)
            node = child # go to child
        # check if child is leaf
        if not node.get_child(self.leaf):
            node.set_child(self.leaf).count
        node.get_child(self.leaf).count += 1
        return node.get_child(self.leaf)

    def delete(self, seq):
        node = self.root
        for x in seq:
            node = node.get_child(x)
            if not node: return False
        # delete leaf
        return node.del_child(self.leaf)

    def traverse(self):
        node = self.root.child
        while node:
            for x in node.traverse(self.leaf):
                yield x
            node = node.sibling

    def get_all(self):
        for x in self.traverse():
            yield "".join(x)

    def common_prefix(self, seq):
        node = self.root
        buff = []
        for x in seq:
            buff.append(x)
            node = node.get_child(x)
            if not node: return
        node = node.child
        while node:
            for x in node.traverse(self.leaf):
                yield buff + x
            node = node.sibling

    def display(self):
        self.root.display(self.leaf, "")



if __name__ == '__main__':
    # suffix trie
    def make_suffix_trie(seq):
        a = Trie()
        for x in xrange(len(seq)):
            a.insert(seq[x:])
        a.insert("ca")
        return a

    s = make_suffix_trie('abcabbca')
    for x in s.traverse():
        print "".join(x)

    print "***********"

    print s.get_hist("a")

    # for x in ['a', 'bc']:
    #     print x
    #     for y in s.common_prefix(x):
    #         print y