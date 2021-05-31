#!/usr/bin/python
# -*- coding: utf-8 -*-


class Node(object):
    """二叉树节点"""
    def __init__(self, data=-1, left_child=None, right_child=None):
        """
        二叉树的节点定义
        """
        self.data = data     # 数据域
        self.left_child = left_child  # 左子树
        self.right_child = right_child  # 右子树

    def perorder(self):
        """
        前序遍历：根左右
        """
        print self.data
        if self.left_child is not None:
            return self.left_child.preorder()
        if self.right_child is not None:
            return self.right_child.preorder()


class BinaryTree(object):
    """二叉树"""
    def __init__(self):
        self.root = None
        self.tree_queue = list()

    def add(self, data):
        """
        添加节点到二叉树中
        :param data: 节点的值
        """
        node = Node(data)
        if not self.root:
            self.root = node  # 如果是空树，对其根节点赋值
            self.tree_queue.append(node)  # 将节点加入到树队列中
            return
        else:
            for i in range(0, len(self.tree_queue)):  # 如果非空，遍历树队列
                if not self.tree_queue[i].left_child:  # 如果这个节点的左子树为空，则赋到左子树上
                    self.tree_queue[i].left_child = node
                    self.tree_queue.append(node)
                    # print self.tree_queue[i].left_child
                    return
                elif not self.tree_queue[i].right_child:
                    self.tree_queue[i].right_child = node
                    self.tree_queue.append(node)
                    # print self.tree_queue[i].right_child
                    return

    def preorder(self, node):
        """
        前序：中左右
        :return:
        """
        if node.data != -1:
            print node.data
        if node.left_child is not None:
            self.preorder(node.left_child)
        if node.right_child is not None:
            self.preorder(node.right_child)

    def midorder(self, node):
        """
        中序：左中右
        """
        if node.left_child is not None:
            self.midorder(node.left_child)
        if node.data != -1:
            print node.data
        if node.right_child is not None:
            self.midorder(node.right_child)

    def postorder(self, node):
        """
        后序：左右中
        """
        if node.left_child is not None:
            self.postorder(node.left_child)
        if node.right_child is not None:
            self.postorder(node.right_child)
        if node.data != -1:
            print node.data

    def levelorder(self, root):
        """
        层次遍历
        """
        if not root:
            return
        treelist = list()
        node = root
        treelist.append(node)
        while treelist:
            node = treelist.pop(0)
            print node.data
            if node.left_child is not None:
                treelist.append(node.left_child)
            if node.right_child is not None:
                treelist.append(node.right_child)

    def preorder_in_stack(self, root):
        """堆栈实现先序遍历"""
        if not root:
            return
        treestack = list()
        node = root
        treestack.append(node)
        while len(treestack) > 0:
            print node.data
            if node.right_child is not None:  # 如果右不为空，入栈
                treestack.append(node.right_child)
            if node.left_child is not None:
                treestack.append(node.left_child)  # 如果左不为空，入栈
            node = treestack.pop()  # 弹出根节点

    def midorder_in_stack(self, root):
        """堆栈实现中序遍历"""
        if not root:
            return
        treestack = list()
        node = root
        while node or len(treestack) > 0:
            if node:
                treestack.append(node)  # 从根节点开始，左子树持续入栈
                node = node.left_child
            else:
                node = treestack.pop()  # 左子树遍历完成，弹出根
                print node.data
                node = node.right_child  # 右子树持续入栈
        """
        while node or treestack:
            while node:  # 从根节点开始，左子树持续入栈
                treestack.append(node)
                node = node.left_child
            node = treestack.pop()  # 左子树遍历完成，弹出根
            print node.data
            node = node.right_child   # 开始查看它的右子树
        """

    def postorder_in_stack(self, root):
        """
        堆栈实现后序遍历
        单栈写法：
        1. 类似于前序遍历，先最左，直到左没有左右孩子
        第一个栈——出栈：中右左（后续的逆序）
        第二个栈——出栈：左右中
        """
        if not root:
            return []
        treestack = list()
        treelist = list()
        node = root
        pre = None
        while node is not None or len(treestack) > 0:
            while node is not None:
                treestack.append(node)
                node = node.left_child
            if len(treestack) > 0:
                node = treestack.pop()
                if not node.right_child or node.right_child == pre:
                    treelist.append(node.val)
                    pre = node
                    node = None
                else:
                    treestack.append(node)
                    node = node.right_child
        print treelist


    def postorder_in_2stack(self, root):
        """
        堆栈实现后序遍历
        双栈写法：
        第一个栈——出栈：中右左（后续的逆序）
        第二个栈——出栈：左右中
        """
        if not root:
            return
        treestack1 = list()
        treestack2 = list()
        node = root
        treestack1.append(node)
        while len(treestack1) > 0:
            node = treestack1.pop()
            if node.left_child is not None:  # 先序遍历反序入栈：先左后右
                treestack1.append(node.left_child)
            if node.right_child is not None:
                treestack1.append(node.right_child)
            treestack2.append(node)
        while treestack2:
            print treestack2.pop().data






if __name__ == '__main__':
    mytree = BinaryTree()
    mytree.add(0)
    mytree.add(1)
    mytree.add(2)
    mytree.add(3)
    mytree.add(4)
    mytree.add(5)
    mytree.preorder_in_stack(mytree.root)
    mytree.preorder(mytree.root)
    # print len(mytree.tree_queue)
    """
    for i in range(0, len(mytree.tree_queue)):
        # print mytree.tree_queue
        print mytree.tree_queue[i].data
        print mytree.tree_queue[i].left_child
        print mytree.tree_queue[i].right_child
"""



