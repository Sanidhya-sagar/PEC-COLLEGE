# stack operations

stack = []
stack_length = int(input("enter your stack size:"))
n="y"

def push(element):
    if len(stack)<stack_length:
        stack.append(element)
    else:
        print("stack overflow")

def pop():
    if len(stack)!=0:
        stack.pop()
    else:
        print("stack is empty")


while n=="y":
    print("1.push element")
    print("2.pop element")
    a=int(input("enter your choice:"))

    if a==1:
        b=int(input("enter number to be pushed in the stack:"))
        push(b)
        

    elif a==2:
        pop()

    print("Stack status:",stack)

    n=input("enter y to continue and n to quit:")

    





