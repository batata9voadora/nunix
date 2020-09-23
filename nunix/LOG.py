import time
LOG = '\n'
def add(*string):
	global LOG
	LOG +='\n' +'at '+time.strftime('%D %H:%M')+' : '+str(string) + '\n'
def show():
	global LOG
	print(LOG)
