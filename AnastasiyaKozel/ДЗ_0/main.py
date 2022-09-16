from numpy import dot  #задача4
from numpy.linalg import norm
def task4(List1, List2):
    result = dot(List1, List2) / (norm(List1) * norm(List2))
    print(result)
n = [5, 7, 18, 3]
m = [55, 5, 17, 18]
task4(n, m)

from scipy import spatial #задача4
def task41(List1, List2):
    result2 = 1 - spatial.distance.cosine(List1, List2)
    print(result2)
task41(n, m)

def task5(List1, List2): #задача5
    result3 = dot(List1, List2)
    print(result3)
task5(n, m)