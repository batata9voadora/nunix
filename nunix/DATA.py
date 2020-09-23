import pickle
file = 'data.dat'
def formatt(name=False,login=False,password=False,problem=True):
    global data,file
    if problem:
        data = ['','','']
        name,login,password = True,True,True
        print('a problem has occurred')
        print(f'the file {file} was not found')
    if name:
        name = input("what'ts your name?: ")
        data[0] = name
    if login:
        login = input('create a login: ')
        data[1] = login
    if password:
        password = input('create a password: ')
        data[2] = password
    pickle.dump(data,open(file,'wb'))

    start()

def start():
    global data,file
    try:
        data=pickle.load(open(file,'rb'))
        return data
    except Exception:
        formatt()

def save():
    global data,file
    pickle.dump(data,open(file,'wb'))
    
if __name__ == '__main__':
    import nunix
