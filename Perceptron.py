# preceptron

class Perceptron:
#   Constructor
    def __init__(self, x_1, x_2, w_1, w_2):
        self.x1Values = x_1
        self.x2Values = x_2
        self.wValues = [w_1, w_2]
        self.yValues =[]
        self.out = []
        self.predict = []
        
# Activator Function
#@ Takes 3 arguments, perceptron_object_name and max value(range/limit), index, limit/test
def sign(n,x,y):
    if y > n.x1Values[x]*n.x2Values[x]:
        return 1
    else:
        return 0
    
# Calculate output of perceptron
def calc_y(n):
    for i in range(len(n.x1Values)):
        n.yValues.append(n.x1Values[i]*n.wValues[0]+n.x2Values[i]*n.wValues[1])
        n.out.append(sign(n,i,30))

def predict(n):
    for i in range(len(n.out)):
        if n.yValues[i]<30:
            n.predict.append(1)
        else:
            n.predict.append(0)

######## Code - Program ########

l = [2,1,6,8,9,5,7,8,2,4]
w = [3,7,2,3,4,9,5,6,2,5]
p1 = Perceptron(l, w,2,4)
print(p1.x1Values,"\n",p1.x2Values,"\n",p1.wValues)

calc_y(p1)
print(p1.yValues)
print("Actual out:\t", p1.out)
predict(p1)
print("Predicted out:\t",p1.predict)