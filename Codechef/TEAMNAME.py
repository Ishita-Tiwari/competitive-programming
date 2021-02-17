# how do we calculate here?
# here, we find all alphabets that a suffix has and select the unique ones.
# these can be swapped hence these are the answer.

# tried: 1. 4 dictionaries 2. mathematics (P and C) 3. current

for _ in range(int(input())):
    n = int(input())
    l = [x for x in input().split()]

    total = 0
    end = []
    alpha = dict()

    '''We get each suffix and the corresponding alphabets. It is
    necessary so that we can calculate the total swaps'''
    for i in l:
        alpha[i[1:]] = []
        end.append(i[1:])
        
    end = list(set(end))

    for i in l:
        alpha[i[1:]].append(i[0])

    for i in range(len(end)):
##        print(i, end[i])
        for j in range(i + 1, len(end)):
##            here, we do not need to consider the previous ones as they have
##            already been counted and would result in redundancy
            end1_alpha, end2_alpha = alpha[end[i]], alpha[end[j]]
            l1, l2 = len(end1_alpha), len(end2_alpha)
            ln = len(set(end1_alpha + end2_alpha))

##            we need to consider the unique ones only. repeated: funny
            cur_swaps = (ln - l1) * (ln - l2) * 2
            total += cur_swaps

    print(total)
