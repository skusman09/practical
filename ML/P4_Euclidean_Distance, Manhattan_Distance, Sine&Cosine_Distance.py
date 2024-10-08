'''
WAP to implement different types of distance method without using in-built function
1. Euclidean Distance
2. Manhattan Distance
3. Sine and Cosine Distance
'''


########################### Euclidean Distance ###########################
import numpy as np
def euclidean_distance(x1, x2):
    distance = 0
    for i in range(len(x1)):
        distance += pow((x1[i] - x2[i]), 2)
    return np.sqrt(distance)
print1 = [1, 2, 3]
print2 = [4, 5, 6]
distance = euclidean_distance(print1, print2)
print('Distance: ' + str(distance))


########################### Manhattan Distance ###########################
import numpy as np
def manhattan_distance(x1, x2):
    distance = 0
    for i in range(len(x1)):
        distance += abs(x1[i] - x2[i])
    return distance
print1 = [1, 2, 3]
print2 = [4, 5, 6]
distance = manhattan_distance(print1, print2)
print('Manhattan Distance: ' + str(distance))


########################### Sine And Cosine Distance ###########################
import numpy as np
def cosine_distance(vector1,vector2):
  vector1= np.array(vector1)
  vector2=np.array(vector2)
  dot_product=np.dot(vector1,vector2)
  norm_vector1=np.dot(vector1,vector1)
  norm_vector2=np.linalg.norm(vector1)
  cosine_similarity=dot_product/(norm_vector1*norm_vector2)
  cosine_distance=1-cosine_similarity
  return cosine_distance
#Example usage
vector1=[1, 2, 3]
vector2=[4, 5, 6]
distance =cosine_distance(vector1, vector2)
print(f'Cosine distance between {vector1} and {vector2} is {distance}')

