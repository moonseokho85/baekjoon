''' Repeating Characters '''
T = input()

for i in range(int(T)):
    S = input()

    # Split the string
    S = S.split()
    
    # Setting the repeat variables
    R = S[0]

    # Setting the paragraph variables
    P = ""
    
    for j in range(len(S[1])):
        P += S[1][j] * int(R)
    
    print(P)