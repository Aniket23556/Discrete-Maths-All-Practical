# For any number n, write a program to list all the solutions of the equation x1 + x2 + x3 + ...+ xn = C, 
# where C is a constant (C<=10) and x1, x2, x3,...,xn are nonnegative integers, using brute force strategy.

######### Use any of the two code

def find_solutions(n, C):
    solutions = []
    def generate_solution(current_solution, remaining_sum):
        if len(current_solution) == n - 1:
            current_solution.append(remaining_sum)
            solutions.append(current_solution[:])
            current_solution.pop()
            return
        for i in range(remaining_sum + 1):
            current_solution.append(i)
            generate_solution(current_solution, remaining_sum - i)
            current_solution.pop()
    generate_solution([], C)
    return solutions


n = int(input("Enter the value of n(variable): "))
Constant = int(input("Enter the value of Constant (C <= 10): "))

if n < 1 or Constant < 0 or Constant > 10:
     print("Invalid input!")
else:
    solutions = find_solutions(n, Constant)
    print("Solutions:")
    for solution in solutions:
        print(solution)



## Code below is given by Roshni

# def find_solutions(n, C):
#     def helper(current_combination, remaining_sum, index):
#         if index == n:
#             if remaining_sum == 0:
#                 results.append(current_combination.copy())
#             return

#         for i in range(remaining_sum + 1):
#             current_combination[index] = i
#             helper(current_combination, remaining_sum - i, index + 1)

#     results = []
#     helper([0] * n, C, 0)
#     return results

# # Example usage
# n = 3  # number of variables
# C = 5  # constant sum
# solutions = find_solutions(n, C)
# for solution in solutions:
#     print(solution)
