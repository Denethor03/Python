class Fibonacci:
    def __init__(self,iterations):
        self.iter = iterations
        self.a = 0
        self.b = 1
        self.current_iter = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current_iter < self.iter:
            value = self.a
            self.a, self.b = self.b, self.a+self.b
            self.current_iter+=1
            return value
        else:
            raise StopIteration
        

if __name__ == "__main__":
    fib = Fibonacci(10)
    for i in fib:
        print(i)