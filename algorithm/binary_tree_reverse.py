# coding:utf-8


'''
Give a binary tree
Reverse it.
'''


class TreeNode(object):
    def __init__(self, x, leftNode=None, rightNode=None):
        self.val = x
        self.left = leftNode
        self.right = rightNode

    def __str__(self):
        return str(self.val)


def invert_tree(node):
    if node:
        node.left, node.right = node.right, node.left
        if node.left:
            node.left = invert_tree(node.left)
        if node.right:
            node.right = invert_tree(node.right)
    return node


def print_tree(node):
    if not node:
        return

    print "<{}>-> {}(L) {}(R)".format(node, node.left, node.right)
    if node.left:
        print_tree(node.left)
    if node.right:
        print_tree(node.right)


def main():
    root = TreeNode(
        4,
        TreeNode(2, TreeNode(1), TreeNode(3)),
        TreeNode(7, TreeNode(6), TreeNode(9))
    )
    invert_tree(root)
    print_tree(root)


if __name__ == '__main__':
    main()
