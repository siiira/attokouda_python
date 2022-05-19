s = input()
answer = ''
if len(s)==3:
  for i in range(2):
    answer += s
  print(answer)
elif len(s)==2:
  for i in range(3):
    answer += s
  print(answer)
elif len(s)==1:
  for i in range(6):
    answer += s
  print(answer)