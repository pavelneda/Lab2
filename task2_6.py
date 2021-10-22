class Node:
    price=[]
    def __init__(self, data,quantity):
        self.left = None
        self.right = None
        self.data = data
        self.quantity=quantity
    def set_price(self,*prices):
        Node.price.append(None)
        for price in prices:
            if not(isinstance(price,(int,float)) and price>0):
                raise ValueError
            Node.price.append(price) 
            

    def insert(self, data,quantity):

        if self.data:
            if data < self.data:
                if not self.left:
                    self.left = Node(data,quantity)
                else:
                    self.left.insert(data,quantity)
            elif data > self.data:
                if not self.right:
                    self.right = Node(data,quantity)
                else:
                    self.right.insert(data,quantity)
        else:
            self.data = data
            self.quantity=quantity
            
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.quantity*Node.price[root.data])
            res = res + self.inorderTraversal(root.right)
        return res
try:
    
    code, qty = map(int, input().split())
    if not(0<code<=10 and qty>0):
        raise ValueError
    root = Node(code,qty)
    root.set_price(1,2,3,4,5,6,7,8,9,10)
    for i in range(4):
        code, qty = map(int, input().split())
        if not(0<code<=10 and qty>0):
            raise ValueError
        root.insert(code,qty)
    print(root.inorderTraversal(root))
except ValueError:
    print("Value error")
