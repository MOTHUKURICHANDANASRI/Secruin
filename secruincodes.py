'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
#Question 1(total combination possible)
numberOfDice =2
numberOfFaces =6
x=(numberOfFaces**numberOfDice)
print(x)

#Question 2(Distribution)
sides=6
for i in range(1,sides+1):
    for j in range(1,sides+1):
        sum=i+j
        print("sum:",sum)
        print("die a:",i)
        print("die b:",j)
    
#Question 3(probability)
total_combinations = 6 * 6
distribution = [0] * 11
sides=6
for die_a in range(1, sides+1):
    for die_b in range(1, sides+1):
        current_sum = die_a + die_b
        distribution[current_sum - 2] += 1

probability_map = {}
for i, count in enumerate(distribution):
    probability = f"{count}/36"
    probability_map[i + 2] = probability

for sum_value, probability in probability_map.items():
    print(f"P(Sum {sum_value}) = {probability}")
