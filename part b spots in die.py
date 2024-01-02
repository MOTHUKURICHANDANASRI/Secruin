'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def undoom_dice(Die_A, Die_B):
    original_probs = [0] * (2 * len(Die_A) + 1)
    for a in Die_A:
        for b in Die_B:
            original_probs[a + b] += 1
    total_outcomes = len(Die_A) * len(Die_B)
    original_probs = [prob / total_outcomes for prob in original_probs]
    New_Die_A = [4] * len(Die_A)
    max_sum = 2 * max(Die_A) + max(Die_B)
    New_Die_B = []
    for i in range(1, 7):
        count = sum(original_probs[i-1:i+max(Die_A)])  
        New_Die_B += [i] * int(count * total_outcomes)

    return New_Die_A, New_Die_B[:len(Die_B)]

# Example usage
Die_A = [1, 2, 3, 4, 5, 6]
Die_B = Die_A

New_Die_A, New_Die_B = undoom_dice(Die_A, Die_B)
print("New Die A:", New_Die_A)
print("New Die B:", New_Die_B)


