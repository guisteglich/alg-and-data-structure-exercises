class Stack:

    def __init__(self):
        self.data = []
        
    def enqueue(self, data):
        self.data.append(data)
        
    def dequeue(self):
        self.data.pop(0)
        
    def get_first_element(self):
        return self.data[0]
         

if __name__ == '__main__':
    stack = Stack()
        
    q = int(input())
    for _ in range(q):
        cmd = str(input()).split(" ")
        if int(cmd[0]) == 1:
            stack.enqueue(cmd[1])
        elif int(cmd[0]) == 2:
            stack.dequeue()
        else:
            print(stack.get_first_element())