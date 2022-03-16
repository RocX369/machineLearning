# so what shall we do today rocky? Lets push value representing a quadratic formular's
# first derivitive toward 0.
#  f(x) = x^2 + 2x -3

# f'(x) = 2x + 2 : Cost

x = 3

for i in range(5):
    if 2*x+2 != 0:
        x = x - (2*x+2)/10
    print(x)

