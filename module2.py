#Chrsitmas tree assignments
x="*"
y=5
# y=int(input())
#normal code 
######1
# for i in range(y+1):
#     for j in range(i):
#         print(x, end="")
#     print()
######2
# for i in range(y+1):
#     for j in range(i):
#         print(x+" ", end="")
#     print()
######3
# for i in range(y+1,0,-1):
#     for j in range(i,0,-1):
#         print(x, end="")
#     print()
######4
# for i in range(y+1,0,-1):
#     for j in range(i,0,-1):
#         print(" ",end="")
#     for p in range (0,(y+1-i)):
#         print(x, end="")
#     print()
########5   
# for i in range(y+1,0,-1):
#     for j in range(i,0,-1):
#         print(" ",end="")
#     for p in range (0,(y+1-i)):
#         print(x+" ", end="")
#     print()
    
#######6   
# for i in range(y):
#     for j in range(y - i - 1):
#         print(" ", end="")
#     for p in range(i + 1):
#         if p == 0 or p == i or i == y - 1:
#             print(x, end=" ")
#         else:
#             print("  ", end="")
#     print()  
#######7
# for i in range(1,y+1):
#     for j in range(i):
#         print(i,"", end="")
#     print()
    
#######8
# count=1
# for i in range(1,y+1):
#     for j in range(i):
#         print(count,"", end="")
#         count+=1
#     print()

########9
# count=1 
# for i in range(y+1,0,-1):
#     for j in range(i,0,-1):
#         print(" ",end="")
#     for p in range (0,(y+1-i)):
#         print(count,"", end="")
#         count+=1
#     print()
    
    
#function method 
######Triangle
def triangle(num):
    for i in range(num+1):
        for j in range(i):
            print(x, end="")
        print()
# triangle(y)
######Triangle with extra spaces
def triangle2(num):
    for i in range(num+1):
        for j in range(i):
            print(x+" ", end="")
        print()
# triangle2(y)
######Flipped up-side-down triangle
def triangle3(num):
    for i in range(num+1,0,-1):
        for j in range(i,0,-1):
            print(x, end="")
        print()
# triangle3(y)
######Turned triangle
def triangle4(num):
    for i in range(num+1,0,-1):
        for j in range(i,0,-1):
            print(" ",end="")
        for p in range (0,(num+1-i)):
            print(x, end="")
        print()
# triangle4(y)

########Christmas tree
def triangle5(num):
    for i in range(num+1,0,-1):
        for j in range(i,0,-1):
            print(" ",end="")
        for p in range (0,(num+1-i)):
            print(x+" ", end="")
        print()
# triangle5(y)

#######Empty Christmas tree  
def triangle6(num):
 
    for i in range(y):
        for j in range(num-i-1):
            print(" ", end="")
        for p in range(i + 1):
            if p == 0 or p == i or i == num - 1:
                print(x, end=" ")
            else:
                print("  ", end="")
        print()  
# triangle6(y)

#######Alternating numbers 
def triangle7(num):

    for i in range(1,num+1):
        for j in range(i):
            print(i,"", end="")
        print()
# triangle7(y)

####### Numbered triangle 
def triangle8(num):
    count=1
    for i in range(1,num+1):
        for j in range(i):
            print(count,"", end="")
            count+=1
        print()
# triangle7(y)

########Numbered Christmas tree 
def triangle8(num):
    count=1 
    for i in range(num+1,0,-1):
        for j in range(i,0,-1):
            print(" ",end="")
        for p in range (0,(num+1-i)):
            print(count,"", end="")
            count+=1
        print()
# triangle8(y)

    