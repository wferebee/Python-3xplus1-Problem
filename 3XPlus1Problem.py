
# Running through the first 10000 numbers of the 3x + 1 Algebra
# - If the number is odd, then multiply by (3x+1)
# - If the number is even, the divide by 2
# - Stop when the number reaches 1
# when a number reaches 1, it enters an infinite loop of "1 -> 4 -> 2 -> 1 -> 4..."

# Scientist have worked out that at least the very first 2^68 digits all reolve to the number loop of "-> 4 -> 2 -> 1 -> 4...",
# but it has not been proven yet if this exists for all numbers

# Here, I am just running through the first 10000 digits as an exercise while learning Python

def ExecuteAlgebra(num):
    starting_num = num
    #region(1) - print statements
        #print(f"Starting Num: {starting_num}")
    steps = 0
    while num != 1:
        if(num % 2 == 0):
            num /= 2
            steps += 1
            #region(2) - print statements
                #print(num)
        else:
            num = ((num * 3) + 1)
            steps += 1
            #region(3) - print statements
                #print(num)
    print(f"Starting Number: {starting_num}, No. Steps: {steps}")

def ExecuteProblem():
    for number in range(1, 10001):
        ExecuteAlgebra(number)


ExecuteProblem()


