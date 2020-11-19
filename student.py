import re 
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

stud_list = {}
stud_count = 1
def create():
    global stud_count
    stud_name = 'student'+ str(stud_count)
    stud_list[stud_name] = {}
    stud_list[stud_name]['id'] = input('enter student id: ')
    stud_list[stud_name]['name'] = input('enter student name: ')
    email = input('enter student email: ')
    if(re.search(regex, email)):
        stud_list[stud_name]['email'] = email
    else:
        print('enter valid email')
        del stud_list[stud_name]
        create()
    stud_count = stud_count + 1

def view(id):
    for i in range(1, stud_count):
        if stud_list['student'+str(i)]['id'] == id:
            print(stud_list['student'+str(i)])
            #u = stud_list['student'+str(i)]
            for key, value in stud_list.items():
                print('       '+key)
    
                for k, v in value.items():
                    print(k + ':', v)

        else:
            pass

def delete(id):
    for i in range(1, stud_count):
        if stud_list['student'+str(i)]['id'] == id:
            del stud_list['student'+str(i)]
            print('deletion is completed....') 
        else:
            pass

def update(id):
    for i in range(1, stud_count):
        if stud_list['student'+str(i)]['id'] == id:
            print(stud_list['student'+str(i)])
            print('which field you want to update: id, name, email...')
            up = input('update to: ')
            stud_list['student'+str(i)][up] = input()
            print('updation is completed....')
        else:
            pass    

x = 1
while(x):
    x = 0
    print('********* Student Management **********')
    print('for create: 1 \nfor view: 2 \nfor update: 3 \nfor delete: 4 \nshow all: 5')
    funct = input('function: ')
    if funct == '1':
        create()
    elif funct == '2':
        view(input('enter id: '))
    elif funct == '3':
        update(input('enter id: '))
    elif funct == '4':
        delete(input('enter id: '))
    elif funct == '5':
        print(stud_list)
    x = int(input('if you want to continue, enter 1 otherwise enter 0: '))


