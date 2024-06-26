from binarytree import BinaryTree
if __name__ == '__main__':
    t=BinaryTree()
    n1=t.Node(100)
    n2=t.Node(200)
    n3=t.Node(300)
    n4=t.Node(400)
    n5=t.Node(500)
    n6=t.Node(600)
    n7=t.Node(700)
    n8=t.Node(800)

    n1.left=n2
    n1.right=n3
    n2.left=n4
    n2.right=n5
    n3.left=n6
    n3.right=n7
    n4.left=n8
    t.root=n1

    print('트리 높이 =',t.height(t.root))
    print('전위 순회:\t',end='')
    t.preorder(t.root)
    print('\n중위 순회:\t', end='')
    t.inorder(t.root)
    print('\n후위 순회:\t', end='')
    t.postorder(t.root)
    print('\n레벨 순회:\t', end='')
    t.levelorder(t.root)
    print()
    print('checking about is_equal method : ',end='')
    print(t.is_equal(t.root,t.root))