# queue implementation

q=[]
def Enqueue(size):
    if len(q)==size: # check wether the stack is full or not
        print("Queue is Full!")
    else:
        element=input("Enter the element:")
        q.append(element)
        print(element,"is added to the Queue!")


def dequeue():
    if not q:# or if len(stack)==0
        print("Queue is Empty!")
    else:
        e=q.pop(0)
        print("element removed!:",e)


def display():
    print("current queue status: ",q)
    size=int(input("Enter the size of Queue:"))
    while True:
        print("Select the Operation: 1.Add, 2.Delete, 3.Display, 4.Quit")
        choice=int(input(":::"))
        if choice==1:
            Enqueue(size)
        elif choice==2:
            dequeue()
        elif choice==3:
            display()
        elif choice==4:
            break
        else:
            print("Invalid Option!")

display()

