# Global variable `init`
init = 1

# Define `plus()` function to accept a variable number of arguments
def plus(*args):
  # Local variable `sum()`
  total = 0
  for i in args:
    total += i
  return total
  
# Access the global variable
print("this is the initialized value " + str(init))

print("this is the sum " , plus(12,32,44))
