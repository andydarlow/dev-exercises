# a possible solution for the rod problem here: https://www.geeksforgeeks.org/cutting-a-rod-dp-13/?ref=lbp
#
# take a different approach to the recursive solution above...
#
# to solve it, I've taken a vector approach. The approach is to find all vectors [x1 ... xn] that when multiplied by (dot product)
# the vector [1...n] will result in the value n.
# To find the vector [x1 ... xn], the code recurses using simple division to find the vectors. 
# for example:. if n = 3
# then the vectors that add to 3 when multiplied by [1 2 3] are [3,0,0], [1,1,0] [0,0,3]
# [1,1,0] is worked out by 3/2 = 1 remainder 1. Then recursing on 1 as n. 1/1 = 1. Hence [1,1,0] is a sultion that adds to 3
# Once you have found all the vectors, you can do another multiple to work out the cost of that solution. for example if the coses are
# [10,11,15] then [1,1,0] would result in a cost of 10*1+11*2+0*3=32
from functools import reduce

#---------------------------------------------------------------
# vector functions (do maths on vectots)
#---------------------------------------------------------------


def new_vector(size):
    """ create a vector of size (filled with 0)"""
    return [0] * size


def merge(vector1, vector2):
    """ overite the contents of vector2 with vector1
        (vector 1/2 unchanged). Vector1 <= vector2 in size
        if vector1 < vector2 then only the digits in vector1 are overriden in vector2. Remaining digitd in vector2 
        are left unchanged
    """
    new_vector = vector1.copy()
    for i in range(0, len(vector2)):
       new_vector[i] = vector2[i]
    return new_vector
 
       
def dot_product(vector1, vector2):
    """ mutpliy the 2 vectors together"""
    return reduce(lambda t,p: t + (p[0]*p[1]),zip(vector1,vector2) , 0)


def vector_max(vector, cost_function):
    """max value in the vector. cost function calculates size of value"""
    max = None
    for i in vector:
        value = cost_function(i)
        max = i if max is None or value > cost_function(max) else max
    return max


def vector_set_index(vector, index, new_value):
    """set value at inext to value"""
    copy = vector.copy()
    copy[index-1] = new_value
    return copy


#---------------------------------------------------------------
#  the porblem to solve
#---------------------------------------------------------------

def max_combination(vector_size, costs):
    vectors = []
    for i in range(1,vector_size+1):
        base_vector = vector_set_index(new_vector(vector_size),i, vector_size // i)
        vector = base_vector if vector_size % i == 0 else merge(base_vector, max_combination(vector_size % i, costs))
        vectors = vectors + [vector]
    return  vector_max(vectors, lambda v: dot_product(v, costs))

# simple example
if __name__ == '__main__':
  costs = [1, 5,8,9,10,17,17,20]
  max_fit = max_combination(len(costs),costs)
  print (f"max found {max_fit} with (highest) cost of {dot_product(max_fit, costs)}")