def inOrder(root):
    #Write your code here
    if root:
        inOrder(root.left)
        # print(root.info) #new line print
        print(root.info, end=" ") #same line print
        inOrder(root.right)