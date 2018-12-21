A = [0,0,0,0] #偷窃表，0表示没偷，1偷
B = [0,0,0,0] #真假表，0表示假，1表示真
refer = ['A','B','C','D']

userinput = [['A',0,0],['A',3,1],['A',1,1],['B',1,0]]
###-----比如，['A',0,0]表示的是，第一个人，说了关于A表的判断，并判断0号不是小偷

for i in range(4):
    for j in range(4):
        A[i],B[j]= 1,1
        flag = True
        for tmp in range(4):
            statement = userinput[tmp]
            if B[tmp]:
                if statement[0]=='A' and A[statement[1]]==statement[2]:
                    continue
                elif statement[0] == 'B' and B[statement[1]] == statement[2]:
                    continue
                else:
                    flag = False
            else:
                if statement[0]=='A' and A[statement[1]]!=statement[2]:
                    continue
                elif statement[0]=='B'and B[statement[1]]!=statement[2]:
                    continue
                else:
                    flag = False
        if flag:
            print("%c说了真话,%c是小偷" %(refer[j], refer[i]))
        A[i], B[j] = 0, 0
