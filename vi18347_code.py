#for the submission uncomment the submission statements
#so submission.README

from math import *
import numpy as np

from submission import *

def seven_segment(pattern):

    def to_bool(a):
        if a==1:
            return True
        return False
    

    def hor(d):
        if d:
            print(" _ ")
        else:
            print("   ")
    
    def vert(d1,d2,d3):
        word=""

        if d1:
            word="|"
        else:
            word=" "
        
        if d3:
            word+="_"
        else:
            word+=" "
        
        if d2:
            word+="|"
        else:
            word+=" "
        
        print(word)

    pattern_b=list(map(to_bool,pattern))

    hor(pattern_b[0])
    vert(pattern_b[1],pattern_b[2],pattern_b[3])
    vert(pattern_b[4],pattern_b[5],pattern_b[6])

    number=0
    for i in range(0,4):
        if pattern_b[7+i]:
            number+=pow(2,i)
    print(int(number))

submission=Submission("angelos_charitidis")
submission.header("Angelos Charitidis")

six=[1,1,-1,1,1,1,1,-1,1,1,-1]
three=[1,-1,1,1,-1,1,1,1,1,-1,-1]
one=[-1,-1,1,-1,-1,1,-1,1,-1,-1,-1]

patterns = []
patterns.append(six)
patterns.append(three)
patterns.append(one)

seven_segment(three)
seven_segment(six)
seven_segment(one)

weight_matrix = np.zeros(11*11).reshape(11,11)

for i in range(weight_matrix.shape[0]):
	weight_matrix[i][i] = 0

for i in (range(weight_matrix.shape[0])):
	for j in (range(weight_matrix.shape[1])):
		if i!=j:
			weight_matrix[i][j] = 1/3 * (patterns[0][i]*patterns[0][j]+patterns[1][i]*patterns[1][j]+patterns[2][i]*patterns[2][j])
			# weight_matrix[i][j] = np.round(weight_matrix[i][j],2)

def keep_sign(number):
	if number>=0:
		return 1
	if number<0:
		return -1

def network(pattern):
	iterations = 1
	stop = False
	while (stop==False):
		temp_pattern = np.zeros(11)
		for i in range(len(pattern)):
			for j in range(len(pattern)):
				temp_pattern[i]+=pattern[j]*weight_matrix[i][j]
			temp_pattern[i] = keep_sign(temp_pattern[i])
		if (np.array_equal(pattern,temp_pattern)):
			stop = True
			pattern = temp_pattern
			submission.seven_segment(pattern)
			energy = energy_of_configuration(pattern)
			submission.print_number(energy)
		else:
			iterations += 1
			pattern = temp_pattern
			submission.seven_segment(pattern)
			energy = energy_of_configuration(pattern)
			submission.print_number(energy)
	return pattern

def energy_of_configuration(pattern):
	energy = 0
	for i in range(len(pattern)):
		for j in range(len(pattern)):
			energy += pattern[i] * weight_matrix[i][j] * pattern[j]
	energy = -(1/2) * energy
	return energy

##this assumes you have called your weight matrix "weight_matrix"
submission.section("Weight matrix")
submission.matrix_print("W",weight_matrix)

submission.section("Test 1")

test1=[1,-1,1,1,-1,1,1,-1,-1,-1,-1]
# test1 --> three

submission.seven_segment(test1)
##for COMSM0027

##where energy is the energy of test
energy = energy_of_configuration(test1)
submission.print_number(energy)


network(test1)


##this prints a space
submission.qquad()

#here the network should run printing at each step
#for the final submission it should also output to submission on each step


submission.section("Test 2")

test2=[1,1,1,1,1,1,1,-1,-1,-1,-1]

submission.seven_segment(test2)
##for COMSM0027

##where energy is the energy of test
energy = energy_of_configuration(test2)
submission.print_number(energy)


network(test2)


##this prints a space
submission.qquad()

#here the network should run printing at each step
#for the final submission it should also output to submission on each step


submission.bottomer()
