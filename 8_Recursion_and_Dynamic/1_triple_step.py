class TripleStep:
    def __init__(self):
        self.memo = {}
        
    def triple_step(self, n):
        
        if n < 0:
            return 0
        
        elif n == 0:
            return 1
        
        if n in self.memo.keys():
            return self.memo[n]
        
        n_ways = self.triple_step(n-1) + self.triple_step(n-2) + self.triple_step(n-3)
        
        self.memo[n] = n_ways
        
        return self.memo[n]
    
triple = TripleStep()
n_ways = triple.triple_step(10)
