from collections import deque


class BinarySearchTree:
    class Node:
        def __init__(self, key):
            self.key = key
            # self.parent = None
            self.left = None
            self.right = None

    def __init__(self) -> None:
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        # base case, the position for new value is found
        if root is None:
            return self.Node(key)

        if key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)

        return root

    def insert_iterative(self, key):
        new_node = self.Node(key)

        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while current:
            if key < current.key:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None:
            return False
        if root.key == key:
            return True

        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            # deleted node has one child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # deleted node has two children
            root.key = self._get_min(root.right)
            root.right = self._delete(root.right, root.key)

    def _get_min(self, node):
        while node.left is not None:
            node = node.left

        return node.key

    def preorder_traversal(self):
        self._preorder_traversal(self.root)

    def _preorder_traversal(self, node):
        if node is not None:
            print(node.key)
            self._preorder_traversal(node.left)
            self._preorder_traversal(node.right)

    def inorder_traversal(self):
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node is not None:
            self._inorder_traversal(node.left)
            print(node.key)
            self._inorder_traversal(node.right)

    def postorder_traversal(self):
        self._postorder_traversal(self.root)

    def _postorder_traversal(self, node):
        if node is not None:
            self._postorder_traversal(node.left)
            self._postorder_traversal(node.right)
            print(node.key)

    def breadth_first_traversal(self):
        queue = deque()
        queue.append(self.root)

        while len(queue) != 0:
            node = queue.popleft()
            print(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


bst = BinarySearchTree()
bst.insert(2)
bst.insert(1)
bst.insert(4)
bst.insert(3)
bst.insert(7)
bst.insert(6)
bst.insert(8)
print('preorder')
bst.preorder_traversal()
print('inorder')
bst.inorder_traversal()
print('postorder')
bst.postorder_traversal()

# homework: using breadth-first search
