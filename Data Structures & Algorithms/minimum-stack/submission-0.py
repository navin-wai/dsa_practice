class MinStack:
    # so for this question , we make two stack ,in one we store the push , pop methods 
    #and in the other we keep the trak of the min value.
    output = []

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val , self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return (self.minstack[-1])
