import pickle
def run():
	try:total = pickle.load(open('node.dat','rb'));classes,result = total[0],total[1]
	except Exception:print('no stored nodes');classes,result = [],[]

	def convert(ask):
		for i in range(len(classes)):
			if ask == classes[i]:return int(i)


	def add(ask):
		classes_add = input('@input ')
		result_add = input('result ')
		g = convert(classes_add)
		try:
			classes.remove(classes_add)
			result.remove(result[g])
		except Exception:pass
		classes.append(classes_add)
		result.append(result_add)


	def rem(ask):
		classes_rem = input('remove ... ')
		try:
			g=convert(classes_rem)
			classes.remove(classes[g])
			result.remove(result[g])
		except Exception:print('no such node')

	def show(ask):
		try: g=convert(ask);print(result[g])
		except Exception: print('"a problem occoured or this node in not stored"')

	def debug(ask):
		print(classes)
		print(result)
	commands_s = ['add','rem','debug']
	commands_f = [add,rem,debug]
	d = {}
	for i in range(len(commands_s)):
		d[commands_s[i]] = commands_f[i]
	while True:
		com = input('\n$')
		if com == 'quit':break
		d.get(com,show)(com)
		total = [classes,result]
		pickle.dump(total, open('node.dat','wb'))
if __name__=='__main__':run()