x = input("Enter something to count its components : ").lower()

def counting (x):
    input_dict  = {}
    for i in set(x) :
       input_dict[i] = x.count(i)
    return input_dict

print("input_dict = ", counting(x))
