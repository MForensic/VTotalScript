f = open("mName.txt","r");
for i in f:
	name=i.split('/')
	name[-1]=name[-1].strip()
	if (len(name)>2):
		print (name[2])
	

