#question 8

def lambda_exp():
    seq = ['soup','dog','salad','cat','great']
    l = list(filter(lambda item:item.startswith("s"), seq))
    print(l)

lambda_exp()