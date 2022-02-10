from user_dao import UserDAO
from logger_base import  log

option = None
while option!= 5:
    print('''Options
                1. list
                2. add
                3. modify
                4.delete
                5.exit''')
    option = int(input('choose option'))

    if option == 1:
        users = UserDAO.select()
        for user in users:
            log.info(user)
    elif option == 2:
        pass
else:
    print('closing app')
