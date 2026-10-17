def calc(s1):
    l=len(s1)
    sum=0
    c=0
    for i in range(0,l):
        if(s1[i].isdigit()):
            sum=sum + int(s1[i])
            c=c+1

    avg=sum/c
    return sum,avg

s1="a123bn"
sum,avg=calc(s1)

print(f"the sum is : {sum}")
print(f"the average is : {avg}")

