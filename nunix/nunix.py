import os
os.system('cls')
def title(new_title):
	os.system('title '+str(new_title))
title('nx')
__copyright__= 'version:  0.75\nby Owsei \ngit @owsei-was-taken  \nstack @owsei \n\n'
def r(end,start=0):
	d=type(end)
	if d==list : return r(len(end))
	if d==int  : return range(start,end)
	if d==float: return range(start,int(end))
	if d==str  : return r(len(end))
	if d==bool : return range(start,int(end))
	




import random,time,sys,datetime,LOG,pickle,shutil,DATA,text_editor,json,node,colors

try:from colored import fg,bg,attr;color = False
except Exception:color = True

DATA.start()
if not color:
	green = fg('green')
	white = fg('white')
	blue = fg('blue')
	red = fg('red')
else:
	white = ''
	green = ''
	blue  = ''
	red   = ''



def use_file(file,mode,obj=None):
	if mode[-1]!='b':mode+='b'
	if obj == None:
		return pickle.load(open(file,mode))
	else:
		pickle.dump(obj,open(file,mode))

def js(file,obj=None):
	if file.split('.')[-1]!='json':
		file+='.json'
	if obj == None:
		return json.load(open(file))
	else:
		json.dump(obj, file)

commands=js('coms')["commands"]
commands_descriptions=js('coms')["commands_descriptions"]






def data_():
	try:return DATA.data
	except Exception:
		print('no data.dat file found\n if it is still existing rename to data.dat\n if deleted return Error 2\n else just return nothing')
		if input() == 'Error 2':
			use_file('data.dat','w','')
			DATA.formatt()


try:LOG.LOG=use_file("nunix_log.dat","rb")

except Exception:use_file("nunix_log.dat", 'wb','')

__copyright__dat = use_file('copyright.dat','rb')

if __copyright__ != __copyright__dat:use_file("copyright.dat",'wb',__copyright__)

def log_():LOG.show()

def exit_():sys.exit()

def help_():
	print('\n')
	for i in r(commands):
		print(commands[i])
		print()

def help2_():
	print('\n')
	for i in r(commands):
		print(commands[i]+':')
		print(commands_descriptions[i])
		print('\n')

def clean_():os.system("cls")

def time_():
	today = datetime.date.today()
	week_days = ['segunda','terça','quarta','quinta','sexta','sabado','domingo']
	weekday = week_days[today.isoweekday()-1]

	i = input('redefine your birthday? (y/n)').strip().lower()
	if i == 'n':
		try:birthday = use_file('birthday.dat','rb')
		except Exception:
			print("your birthday is not save in the nunix data files")
			print("when is your birthday?")
			year = int(time.time()/(3600*24*365))+1970
			birthday = datetime.date(year,eval(input('month: ')),eval(input('\nday: ')))
	if i == 'y':
		print("when is your birthday?")
		year = int(time.time()/(3600*24*365))+1970
		birthday = datetime.date(year,eval(input('month: ')),eval(input('\nday: ')))
	till_birthday = birthday - today
	print(f'today is {today}')
	print(f"in {till_birthday.days} days it is going to be your birthday!!!\n")

def currency_():
   print("it is just not working\n i am sorry")

def os_():
	data=data_()
	name = data[0]
	b = 1
	print('enter "quit" to stop entering commands in the os \n')
	while True:
		title('nx-os')
		b+=1
		if (a:=input(f'{green}nx{white}@{red}{name}{white}-{blue}os{white} {b}$ ')) == 'quit':break
		else:
			print()
			os.system( str(a) )
			LOG.add('the user entered the command '+a+' in the computer os')

def text_():
	import text_editor
	try:text_editor.run()
	except Exception:pass

def RNG_():
	r = input('from .. to .. ')
	r.split()
	print(r)
	for i in r(int(input('how many times?'))):
		print(random.randint(min(r),max(r)))

def start_():
	a = input('start: ')
	os.system(f'start {a}')

def python_():
	os.system('title nx-python')
	os.system('python')

def python_IDLE_():os.system('start IDLE python')

def calc_():
	print('enter quit to stop')
	while True:
		if (a:=input('your calc here: ')) == 'quit':break
		try:a=eval(a);print((a))
		except Exception:print('uh no')

def copyright_():print(__copyright__)


def translate_():
	print('sorry not done \nyet')

def new_directory_():
	os.system('cd')
	os.system('mkdir ' + input('directory name:  '))

def delete_directory_():
	os.system('dir')
	try:shutil.rmtree(input('delete folder: '))
	except Exception: print('no such file directory')

def delete_file_():
	os.system('dir')
	try:os.unlink(input('file'))
	except Exception:print('no such file')

def cd_():
	go_to = input(os.system('cd'))
	os.chdir(go_to)
	os.system('cd')
	LOG.add('the user enter cd' + go_to)

def dir_():os.system('dir')

def wikipedia_():
	import wikipedia
	article = input('what article?  ')
	try:result = wikipedia.page(article).content;print(result)
	except Exception:print('no such article')

def rename_():DATA.formatt(name=True,problem=False)

def signup_():DATA.formatt(name=True,login=True,password=True,problem=False)

def log_in_():
	data=data_()
	name = data[0]
	login = data[1]
	password = data[2]
	if login != input('login: ') or password != input('password: '):
		print('wrong password or login')
		sys.exit()

def nodes_():
	import node;node.run()


def no_command_():print('inexisting command\nyou can try "help" or "help 2" for help')


def run():
	copyright_()
	log_in_()
	print('\npress enter to send command')
	print('enter help or help 2 for the commands and their descriptions')
	if True:
		func=[
		log_
		,exit_
		,help_
		,help2_
		,clean_
		,time_
		,currency_
		,calc_
		,os_
		,text_
		,RNG_
		,start_
		,python_
		,python_IDLE_
		,translate_
		,copyright_
		,new_directory_
		,delete_directory_
		,delete_file_
		,dir_
		,wikipedia_
		,rename_
		,signup_
		,nodes_
		]


	commands_dict = {'':print}
	for i in r(commands):commands_dict[commands[i]] = func[i]
	entered_commands = 1
	try:shutil.rmtree('__pycache__')
	except Exception:pass
	while True:
		#DATA.save()
		data=data_()
		name = data[0]
		os.system('title nunix')
		if entered_commands == 1:print(f'\nwelcome back {name}!!')
		command = input(f'\n{green}nx{white}@{red}{name}{white} {entered_commands}$ ').strip().lower()
		LOG.add(f'the user entered the command {command}')
		pickle.dump(LOG.LOG,open("nunix_log.dat", 'wb'))
		entered_commands+=1
		#try:
		commands_dict.get(command,no_command_)()
		#except Exception:print('a problem has occoured')
if __name__ =='__main__':run()