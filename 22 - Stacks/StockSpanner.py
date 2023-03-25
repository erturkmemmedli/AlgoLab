class StockSpanner:
    def __init__(self):
        self.stack = []
                
    def next(self, price: int) -> int:
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            pr, sp = self.stack.pop()
            span += sp
        
        self.stack.append((price, span))

        return span        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

# Official solution

class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price):
        answer = 1

        while self.stack and self.stack[-1][0] <= price:
            answer += self.stack.pop()[1]
        
        self.stack.append([price, answer])
        return answer
