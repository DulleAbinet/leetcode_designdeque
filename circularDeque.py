class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = [0]*k
        self.capacity = k
        self.front = 0
        self.rear = 0
        self.size = 0
        

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            if self.isEmpty():
                self.deque[self.front] = value
            else:     
                self.front = (self.front - 1)%self.capacity
                self.deque[self.front] = value
            self.size +=1
           
            return True
        else:
            return False
        
        
    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            if self.isEmpty():
                self.deque[self.rear] = value
            else:
                self.rear = (self.rear + 1)%self.capacity
                self.deque[self.rear] = value
            self.size +=1
            return True
        else:
            return False
        

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.front = (self.front + 1)%self.capacity
            self.size -=1
            if self.isEmpty():
                self.rear = self.front
            return True            
        return False
        

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.rear = (self.rear - 1)%self.capacity
            self.size -=1
            if self.isEmpty():
                self.front = self.rear
            return True
        
        return False
        
        

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.deque[self.front]
        
        return -1
        

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.deque[self.rear]
        return -1
        

    def isEmpty(self) -> bool:
        return self.size == 0  
        

    def isFull(self) -> bool:
        return self.size == self.capacity
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
