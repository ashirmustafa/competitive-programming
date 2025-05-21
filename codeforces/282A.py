from typing import List
x = 0
n = int(input())
statements = []
for i in range(0,n):
    statements.append(str(input()))

for statement in statements:
    if(statement == "++X" or statement == "X++"):
        x += 1
    elif(statement == "--X" or statement == "X--"):
        x -= 1
        
print(x)
        
