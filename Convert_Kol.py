
from math import floor
def Convert_Kol(path,name):
	temp = open(path,'r')
	content = temp.readlines()
	temp.close()
	new_file = open(name+'.csv', 'w+')
	new_file.write('Month,Day,time,Quantity,Cost\n')
	for line in content:
		new_line = line[2:]
		new_line = new_line.replace(',','')
		new_line = new_line.replace('@','')
		new_line = new_line.replace('bought','')
		new_line = ' '.join(new_line.split()).split()
		temp = new_line[2][:-3].split(':')
		hour = float(temp[0])%12+float(temp[1])/60
		if new_line[2][-3:-1]=='pm':
			hour=hour+12
		new_line[2] = str(hour)
		new_line =','.join(new_line)
		new_line=new_line+'\n'
		new_file.write(new_line)
	new_file.close()