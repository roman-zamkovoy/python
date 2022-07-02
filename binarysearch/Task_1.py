class Solution:
    def solve(self, n):
        for i in range(len(n)):
            if (n[i] % 3 == 0):
                n[i] = "Fizz"
            if (n[i] % 5 == 0):
                n[i] = "Buzz"
            if (n % 3 == 0 and n % 5 == 0):
                n[i] = "FizzBuzz"
print(1)



