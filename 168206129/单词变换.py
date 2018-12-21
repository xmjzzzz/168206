A="hit"
B="cog"
D=["hot","dot","dog","lot","log"]
def link(a,b):
	n=len(a)
	same=0
	for i in range(n):
		if a[i]==b[i]:
			same+=1
	if same==n-1:
		return True
	else:
		return False
suc=[]
path=[]
path.append(A)
def searchPath(path):
	n=len(path)
	for d1 in D:
		if link(path[-1],d1):
			if(d1 in path):
				pass
			else:
				path.append(d1)
				if link(d1,B):
					path.append(B)
					suc.append(path)
					break;
				searchPath(path)
			
		path=path[:n]		
searchPath(path)
for s in suc:
	print (len(s),s)
