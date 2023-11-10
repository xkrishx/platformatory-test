#scores=["3:2", "4:1", "1:4", "3:3"]
scores=[]
n=int(input("enter number of match results: "))
for i in range(n):
    scores.append(input("enter match score in the format -> x:y : "))

print("the scores received are: ", scores)

def calc(scores):
    points=0
    for i in range(len(scores)):
        x=int(scores[i][0])
        y=int(scores[i][2])

        if (0<=x<=4 and 0<=y<=4):
            if x>y:
                points+=3
            elif x==y:
                points+=1
        else:
            print("entered scores are not valid")
            break
    print("total points obtained is: ", points)

calc(scores)