'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

word = input("Enter the three letter word:")
result = []
for i in range(len(word)):
    for j in range(len(word)):
        if j==i:
            continue
        for k in range(len(word)):
            if  j==k or i==k:
                continue
            result.append(word[i]+word[j]+word[k])
print("The permutation of three letter is:")            
print(result)


