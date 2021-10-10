class Node:
    price=[]
    def __init__(self, data,quantity):
        self.left = None
        self.right = None
        self.data = data
        self.quantity=quantity
    def set_price(self,*prices):
        Node.price.append('')
        for price in prices:
            if isinstance(price,(int,float)) and price>0:
                Node.price.append(price) 
            else:
                raise ValueError

    def insert(self, data,quantity):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data,quantity)
                else:
                    self.left.insert(data,quantity)
            elif data > self.data:
                if self.right is None:
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
    if 0<code<=10 and qty>0:
            root = Node(code,qty)
    else:
        raise ValueError
    root.set_price(1,2,3,4,5,6,7,8,9,10)
    for i in range(4):
        code, qty = map(int, input().split())
        if 0<code<=10 and qty>0:
            root.insert(code,qty)
        else:
            raise ValueError

    print(root.inorderTraversal(root))
except ValueError:
    print("Value error")
