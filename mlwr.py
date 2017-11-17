import requests
import time
import json


# This script gets malware hashes from file and contacts virustotal to get their report.
# It then saves the report in the current directory with the name "hash.json". Where hash malware hash. 



def CallAPI(mname):

	
	params = {'apikey': '7f493bb73cbd6821b92a420bbc6e7f8bc1eebf480a25f93bc446ad8acb2a1c08', 'resource': mname}
	headers = {
	  "Accept-Encoding": "gzip, deflate",
	  "User-Agent" : "gzip,  My Python requests library example client or username"
	  }
	response = requests.get('https://www.virustotal.com/vtapi/v2/file/report',
	  params=params, headers=headers)
	return response;



# reads the hash from file calls the virus total API saves the last hash line number
# it called and starts from next hash where it stopped when qouta request had reached the limit. 

def fReader(): 
	fi = open('index.txt')	#index file
	idx=int(fi.readline());
	with open('mName.txt') as f:	# file containing malware names
		for i in xrange(idx):		# Start from last known line
			f.next();
		for x, j in enumerate(f):		
			if j.rstrip(): 
				fi = open('index.txt','w')   #save last hash index into the file so that we can start again from that index in case of failure
				c= idx+x;
				fi.write(str(c));
				fi.close()
		        name=j.split('/')
		        name[-1]=name[-1].strip()
		        if (len(name)>2):
		        	mname =name[2]
		        	Jresp=CallAPI(mname)		#response object
       				if(Jresp.status_code==200):
               				with open(mname+".json", 'w') as f:
                        			json.dump(Jresp.json(),f);
                        			print (Jresp.json());
        			elif(Jresp.status_code==204):
                			fi.close();
                			time.sleep(60);         
       				else:
                			time.sleep(300);     


def main():

	fReader();



if __name__== "__main__":
  main()
	




					
