import os
l = [
'black','blue','green','green ish blue','red','purple','yellow','white','gray'
,'bright blue','bright green','bright green ish blue','bright red','bright purple','bright yellow','bright white']
colors = {
	'black':'0'
	,'blue':'1'
	,'green':'2'
	,'green ish blue':'3'
	,'red':'4'
	,'purple':'5'
	,'yellow':'6'
	,'white':'7'
	,'gray':'8'
	,'bright blue':'9'
	,'bright green':'A'
	,'bright green ish blue':'B'
	,'bright red':'C' 
	,'bright purple':'D'
	,'bright yellow':'E'
	,'bright white':'F'
	}


def fg(color):
	j=[]
	for i in range(len(l)):
		j.append(color==l[i])
	if (any(j)==True): return os.system('color '+colors.get(color,''))
	else: print('no such color')
def colors_list():
	for i in range(len(l)):print(l[i])