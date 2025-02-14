def OddandEven(l):

    l1 = [x for x in l if x % 2 == 0]  # List Comprehension
    l2 = {x for x in l if x % 2 != 0}  # Set Comprehension

    return (l1, l2)


print(OddandEven([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# Dictionary Comprehension

keys = ["fName", "lName", "fullName"]
values = ['Tesh', 'Chaudhary', 'Tesh Chaudhary']

d = {keys[i]: values[i] for i in range(len(keys))}
print(d)

dict(zip(keys, values))  # can zip two lists like this too


# Exchanging key values

d1 = {v: k for (k, v) in d.items()}
print(d1)


