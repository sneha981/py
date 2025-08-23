import random
no=int(input("Enter num of teams "))
teams=[]
matches=[]
for i in range(no):
    d=input("Enter team name:")
    teams.append(d)
meet=int(input("Enter of meet bw same teams"))
for i in range(no):
    for j in range(i+1,no):
        for k in range(meet):
            matches.append([teams[i],teams[j]])
random.shuffle(matches)
for i in range(len(matches)):
    print("matches {} . {} vs {}".format(i+1,matches[i][0],matches[i][1]))

