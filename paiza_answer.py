#C107　ランクの計算
N,K=map(int, input().split())
al=[]
bl=[]
cl=[]
al_answer=[]
bl_answer=[]
cl_answer=[]

for i in range(N):
    al.append(int(input()))
for i in range(N):
    bl.append(int(input()))
for i in range(N):
    cl.append(int(input()))
    
for i in range(N-K+1):
    al_answer.append(sum(al[0+i:K+i])/K)
for i in range(N-K+1):
    bl_answer.append(sum(bl[0+i:K+i])/K)
for i in range(N-K+1):
    cl_answer.append(sum(cl[0+i:K+i])/K)
# print(al_answer,bl_answer,cl_answer)
# print(min(al_answer),min(bl_answer),min(cl_answer))
# print(al,bl,cl)
if min(al_answer)<min(bl_answer) and min(al_answer)<min(cl_answer):
    print('1')
elif min(bl_answer)<min(cl_answer) and min(bl_answer)<min(al_answer):
    print('2')
elif min(cl_answer)<min(al_answer) and min(cl_answer)<min(bl_answer):
    print('3')

#C108 観光の計画
N = int(input())
time = []
program=[]
for i in range(N):
    time.append(int(input()))
move_time = [list(map(int, input().split())) for l in range(N)]
# print(time,move_time)


K = int(input())
for i in range(K):
    program.append(int(input()))
# print(K,program)
count = 0
# print(move_time[1][0])
for i in range(K):
    # print('roop',i)
    # print('所要',time[program[i]-1])
    count = count + time[program[i]-1]
    if i+1 <K:
        # print(program[i + 1])
        # print('移動',move_time[program[i]-1][program[i+1]-1])
        count = count + move_time[program[i]-1][program[i+1]-1]

    # print(move_time[program[i]][program[i+1]])
print(count)

#C028 単語テストの採点
N = int(input())
point = 0
for i in range(N):
    correct, answer = input().split()
    minus = 0
    if len(correct)==len(answer):
        for i in range(len(answer)):
            if not correct[i]==answer[i]:
                minus +=1
        if minus == 0:
            point +=2
        elif minus == 1:
            point +=1
print(point)

#C16 Leet 文字列
s = input()
# print(s)

for i in range(len(s)):
    # print(s[i])
    if s[i]=='A':
        s = s.replace(s[i],'4')
    elif s[i]=='E':
        s = s.replace(s[i],'3')
    elif s[i]=='G':
        s = s.replace(s[i],'6')
    elif s[i]=='I':
        s = s.replace(s[i],'1')
    elif s[i]=='O':
        s = s.replace(s[i],'0')
    elif s[i]=='S':
        s = s.replace(s[i],'5')
    elif s[i]=='Z':
        s = s.replace(s[i],'2')

print(s)

#C075 ポイント払い
N, M = map(int, input().split())
point = 0
for i in range(M):
    fee = int(input())
    if point>=fee:
        point -= fee
    else:
        N -= fee
        point += fee*0.1
    print(N,int(point))
    