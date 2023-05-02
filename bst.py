class BSTNode:
    def __init__(self, key, value, left= None, right= None, parent=None):
        self.key = key
        self.value=value
        self.left= left
        self.right=right
        self.parent=parent
        

class BinarySearchTree:
    def __init__(self):
        self._root = None
        self._size=0

    def size(self):
        return self._size

    def add(self, key, value):
        node = BSTNode(key, value)
        temp= self._root
        prev=None
        while temp!= None:
            prev=temp
            if key<= temp.key:
                temp= temp.left
            else:
                temp=temp.right
        if prev==None:
            self._root=node
        elif key<prev.key:
            prev.left=node
        else:
            prev.right=node
        node.parent=prev
        self._size += 1

    def search(self, key):
        temp=self._root
        while temp!=None:
            if key< temp.key:
                temp= temp.left
            elif key> temp.key:
                temp= temp.right
            else:
                break
        if temp== None:
            return False
        else:
            return temp.value
        
    def smallest(self):
        temp = self._root
        try: 
            while temp.left!=None:
                temp=temp.left
            return (temp.key, temp.value)
        except:
            return None
        
    def largest(self):
        temp = self._root
        try: 
            while temp.right!=None:
                temp=temp.right
            return (temp.key, temp.value)
        except:
            return None
    
    def noChild(self,temp):
        try:
            if temp.parent.left==temp:
                temp.parent.left=None 
            else: 
                temp.parent.right=None 
            temp=None
        except:
            temp=None
            self._root=None
    def leftChild(self,temp):
        try:
            temp.left.parent=temp.parent
            temp.parent.left=temp.left
            temp=None
        except:
            self._root=temp.left
            temp=None
    def rightChild(self,temp):
        try:
            temp.right.parent=temp.parent
            temp.parent.right=temp.right
            temp=None
        except:
            self._root=temp.right
            temp=None
    def bothChild(self,temp):
        swap=temp.left
        while swap.right!=None:
            swap=swap.right
        temp.key= swap.key
        temp.value= swap.value
        if swap.left==None:
            if swap.parent.left==swap:        
                swap.parent.left=None
            else:
                swap.parent.right=None
            swap = None
        else:
            if swap.parent.left==swap:
                swap.parent.left= swap.left
                swap.left.parent= swap.parent
            else:
                swap.parent.right= swap.right
                swap.left.right= swap.parent
            swap=None
    
    def remove(self, key):
        if self.search(key)== False:
            return False
        self._size = self._size - 1
        temp=self._root
        while temp.key != key:
            if key< temp.key:
                temp= temp.left
            else:  
                temp= temp.right
        if temp.left== None and temp.right==None:
            self.noChild(temp)
            
        elif temp.left!=None and temp.right==None:
            self.leftChild(temp)
            
        elif temp.left==None and temp.right!=None:
            self.rightChild(temp)
            
        else:
            self.bothChild(temp)
            





    def _inorder_walk(self,nodes, node):
        if node== None:
            return
        self._inorder_walk(nodes, node.left)
        nodes.append(node.key)
        self._inorder_walk(nodes, node.right)

    def inorder_walk(self):
        nodes=[]
        self._inorder_walk(nodes, self._root)
        return nodes
    

    def _preorder_walk(self,nodes, node):
        if node== None:
            return
        nodes.append(node.key)
        self._preorder_walk(nodes, node.left)
        self._preorder_walk(nodes, node.right)

    def preorder_walk(self):
        nodes=[]
        self._preorder_walk(nodes, self._root)
        return nodes
    

    def _postorder_walk(self,nodes, node):
        if node== None:
            return
        self._postorder_walk(nodes, node.left)
        self._postorder_walk(nodes, node.right)
        nodes.append(node.key)

    def postorder_walk(self):
        nodes=[]
        self._postorder_walk(nodes, self._root)
        return nodes
        

       




        
        

            

        

    
        
