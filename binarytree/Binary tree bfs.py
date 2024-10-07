class Node:
    def _init_(self,data):
        self.data = data 
        self.right = None 
        self.left = None 
class BinaryTree_BFS:
    def _init_(self):
        self.root = None 
        self.queue = []
    
    def insert(self,data):
        newnode = Node(data)
        if self.root is None:
            self.root = newnode 
        else:
            self.queue = [self.root]
            while True:
                node = self.queue.pop(0)
                if node.left is None:
                    node.left = newnode 
                    return 
                else:
                    self.queue.append(node.left)
                
                if node.right is None:
                    node.right = newnode 
                    return 
                else:
                    self.queue.append(node.right)
    # def inorder(node):
    #     if  node is None:
    #         return 
    # inorder(node.left)
    #     print(node.data,end=' ')
    # inorder(node.right)

    def display(self):
        if self.root is None:
            print("The tree is empty.")
            return
        
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.data, end=" ")
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()  # For a new line after displaying all nodes



b = BinaryTree_BFS()
b.insert(1)
b.insert(2)
b.insert(3)
b.insert(4)
b.display()


