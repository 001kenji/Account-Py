# account
# create account-save-
# login - number password
import json
import random
import re


writtingStructure =   {
        'accounts': {
            'KENJI CLADIA': {
                'PhoneNumber': '+254712456789',
                'EmailAddresss': 'briannjuguna7474@gmial.com',
                'PassCode': 'kenjicladia'
            },
            'CLACK KENT': {
                'PhoneNumber': '+254712456789',
                'EmailAddresss': 'clackkent344@gmial.com',
                'PassCode': 'clackkent'
            },
            'CLOE SULEVAN': {
                'PhoneNumber': '+254712456789',
                'EmailAddresss': 'cloesulevan3423@gmial.com',
                'PassCode': 'cloesulevan'
            },
            'JOHN MON': {
                'PhoneNumber': '+254712456789',
                'EmailAddresss': 'johnmon2323@gmial.com',
                'PassCode': 'johnmon'
            }


        },
        'ADMIN': {

        },
        'messages': {

        }
    }

realDatabase =   {
            'briannjuguna7474@gmial.com': {
                'PhoneNumber': '+254712456789',
                'name': 'BRIAN NJUGUNA',
                'PassCode': 'kenjicladia'
            },
            'clackkent344@gmial.com': {
                'PhoneNumber': '+254712456789',
                'name': 'CLACK KENT',
                'PassCode': 'clackkent'
            },
            'cloesulevan3423@gmial.com': {
                'PhoneNumber': '+254712456789',
                'name': 'CLOE SULEVAN',
                'PassCode': 'cloesulevan'
            },
            'johnmon2323@gmial.com': {
                'PhoneNumber': '+254712456789',
                'name': 'JOHN MON',
                'PassCode': 'johnmon'
            }


        }


# database = open('damaincLog.json', 'w')
# database.write('kenji is writting kenji is the one. What a kenji')
# database.close()
#database = open('damaincLog.json', 'r')
# print(database.readline())
# x = database.read()

# word = re.split('kenji', x)
# print(word)

# for character in range(1, 20, 1):
#     values = database.read(character)
#     print(values)

# iterator = iter(database)
# print(next(iterator))



#this impliments the knowladge of working with a database which is actually a json arrayed data
# database = open('damaincLog.json', 'w')
# database.write(str(writtingStructure))
# database.close()



class ChangeEmailAuto:
    with open('trial.json', 'w') as JsonData:
        JsonData.write(json.dumps(writtingStructure))
        JsonData.close()

    with open('trial.json', 'r') as ReadingJson:
        # the value to change is KENJIC CLADIA EmailAddresss
        name = 'KENJI CLADIA'
        value = ReadingJson.read()
        data = json.loads(value)
        randomNum = random.randrange(100, 10000)
        for index, value in data.items():
            if index == 'accounts':
                data2 = value
                for x, y in data2.items():
                    if x == name:
                        email = 'kenjicladia{0}@gmial.com'
                        emailFor = email.format(randomNum)
                        y['EmailAddresss'] = emailFor
                        with open('trial.json', 'w') as ChangeData:
                            ChangeData.write(json.dumps(data))
                            ChangeData.close()
                        print(y['EmailAddresss'])

        ReadingJson.close()
        # research on how big companies like facebook use a technique of changing their database

callEmailChanger = ChangeEmailAuto()
#callEmailChanger

class RealisticDataSect:
    def __int__(self, name, email, passCode, number):
        self.FuncName = name
        self.FuncEmail = email
        self.FuncPass = passCode
        self.PhoneNumber = number

    determiner = input('Enter \'log-in\' if you want to log in or \'create\'  if you want to create an account or \'delete\' to delete an account: ')

    def Loger():
        email = input('Enter your Email: ')
        passWord = input('Enter your password: ')
        emailFound = False
        with open('RealDatabase.json', 'r') as RealDB:
            data = json.loads(RealDB.read())
            for index, value in data.items():
                if index == email:
                    data2 = value
                    if data2['PassCode'] == passWord:
                        emailFound = True
                        print('Your Successfully logged in!...')
                    elif data2['PassCode'] != passWord:
                        print('Either you \'name\' or your \'password\' is incorrenct.Try again')
            if emailFound == False:
                print('Sorry Incorrent Email! or no account found...')
            RealDB.close()

    def AccountCreator():
        name = str(input('Enter Name: '))
        email = str(input('Enter Email: '))
        number = int(input('Enter Phone-Number:+254 '))
        passCode = str(input(('Enter a new strong password: ')))
        with open('RealDatabase.json', 'r') as SignUp:
            data = json.loads(SignUp.read())
            numberData = '+254 {}'
            numberFormat = numberData.format(number)
            data[email] = {
                'PhoneNumber': numberFormat,
                'name': name,
                'PassCode': passCode
            }
            with open('RealDatabase.json', 'w') as RightSingUp:
                RightSingUp.write(json.dumps(data, indent=4))
                RightSingUp.close()
            print(data[email])
            SignUp.close()
        print('Your successfully Signed Up. Enjoy the service...')

    def DeleteAccount():
        email = input('Enter your Email: ')
        passWord = input('Enter your password: ')
        emailFound = False
        with open('RealDatabase.json', 'r') as RealDB:
            data = json.loads(RealDB.read())
            for index, value in data.items():
                if index == email:
                    data2 = value
                    if data2['PassCode'] == passWord:
                        emailFound = True
                        del data[index]

                        with open('RealDatabase.json', 'w') as Deleted:
                            Deleted.write(json.dumps(data, indent= 4))
                            Deleted.close()
                        print('Your have successfully deleted your account!...')
                        RealDB.close()
                        return 0
                    elif data2['PassCode'] != passWord:
                        print('Either you \'name\' or your \'password\' is incorrenct.Try again')
            if emailFound == False:
                print('Sorry Incorrent Email! or no account found...')
            RealDB.close()

    if determiner.lower() == 'log-in':
        Loger()
    elif determiner.lower() == 'create':
        AccountCreator()
    elif determiner.lower() == 'delete':
        DeleteAccount()
    else:
        print('Invalid Input. Try again later.')


realCaller = RealisticDataSect()


