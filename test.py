n=5
shared = [5]
like=[2]
sum=2

for i in range(1,n):
	shared.append(like[i-1]*3)
	like.append(shared[i]//2)
	sum+=like[i]
print(sum)