# evaluation of postfix

a = list(input("Enter the postfix expression: ").split(" "))  
stack = []  
for i in a:  
    if(i in ["+", "-", "*", "/"]):  
        b = stack.pop()  
        c = stack.pop()  
        if(i=="+"):  
            stack.append(c+b)  
        elif(i=="-"):  
            stack.append(c-b)  
        elif(i=="*"):  
            stack.append(c*b)  
        elif(i=="/"):  
            stack.append(c/b)  
    elif i==" ":  
        continue  
    else:  
        stack.append(int(i))  

# 3 8 + 9 8 / -
# 12 34 + 44 1 * -

print("The result of the expression: ",stack[0])