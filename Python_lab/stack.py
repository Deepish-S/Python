ch=1
l1=[20,30,40,50]
l2=[45,35,65,85,95]
while(ch==1):
    print('1.stack operation\n')
    print('2.queue operation\n')
    ch=int(input('enter your choice'))
    if(ch==1):
        print('stack is',l1)
        print('1.push\n')
        print('2.pop\n')
        print('enter your choice')
        ch2=int(input())
        if(ch2==1):
            no=int(input('enter a no to push'))
            l1.append(no)
            print('list after push',11)
        elif(ch2==2):
            print('popped element is',l.pop())
            print('list after pop is',l1)
        else:
            print('illegal choice')
    elif(ch==2):
        print('queue is',l2)
        print('1.insert')
        print('2.delete')
        print('enter your choice')
        ch2=int(input())
        if(ch2==1):
            no=int(input('enter a no to insert'))
            l2.insert(len(l2),no)
            print(l2)
        elif(ch2==2):
            print('deleted element is',l2.pop(0))
            print(l2)
        else:
            print('wrong choice')
    else:
        print('wrong choice')
print('enter 1 to continue')
ch=int(input())
