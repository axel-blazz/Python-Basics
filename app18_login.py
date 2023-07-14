print('Create your account')

userName = input('Input username: ')
passWord = input('Input password: ')

class User():
    def __init__(self, userName, passWord) :
        self.userName = userName
        self.passWord = passWord

p1 = User(userName, passWord)

print('User',p1.userName, 'created successfully!')

print('Login now !')
userName2 = input('Input username: ')
passWord2 = input('Input password: ')

if(p1.userName == userName2 and p1.passWord == passWord2):
    print('Login successful!')
else :
    print('Id or password incorrect')