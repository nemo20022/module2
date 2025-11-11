x="*"
y=5
# y=int(input())

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
#######6 
# for i in range(1,y+1):
#     for j in range(i):
#         print(i,"", end="")
#     print()
    
#######6 
# count=1
# for i in range(1,y+1):
#     for j in range(i):
#         print(count,"", end="")
#         count+=1
#     print()

########7 
# count=1 
# for i in range(y+1,0,-1):
#     for j in range(i,0,-1):
#         print(" ",end="")
#     for p in range (0,(y+1-i)):
#         print(count,"", end="")
#         count+=1
#     print()
    