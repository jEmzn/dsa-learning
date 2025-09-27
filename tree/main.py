from binary_tree import BinaryTree


r = BinaryTree('1')

r.insertLeft('2')
r.getLeftChild().insertLeft('4')
r.getLeftChild().insertRight('5')
r.insertRight('3')
r.getRightChild().insertRight('6')

print(r.inorder(r))



