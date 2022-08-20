# Create a function that takes three parameters of equation and returns the roots of this equation: 
# For example: 
# 2×2+4x−6
# Find the roots of this equation: 
# Formula and Solution: 

# x =  −b ± √(b^2 − 4ac)
#          2a
# x =  −4 ± √(4^2 − 4(2)(-6))
#          2(2)

# x =  −4 ± √(16 − -48))
#           4

# x =  −4 ± √64
#         4

# x =  −4 ± 8
#         4

# x =   4         x = - 12
#       4               4 

# which becomes

# x = 1
# x = -3

# Hence the roots of this equation are 1 and -3
# Paste your Python code with some example results here in this assignment.


# import complex with math module
import cmath

a = 3
b = -2
c = 6

def quad_eq(x,y,z):
    # calculate the discriminant
    discriminant = (y**2) - (4*x*z)
    # find two solutions
    first_sol = (-y-cmath.sqrt(result))/(2*x)
    second_sol = (-y+cmath.sqrt(result))/(2*x)
    result = first_sol, second_sol
    # print('The solution of this quadratic equation is: ', first_sol, 'and', second_sol)
    return result


print(quad_eq(a,b,c))