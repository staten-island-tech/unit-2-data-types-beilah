withdraw = input('How much would you like to withdraw from your balance? ')

def ATM(balance, withdraw):

    withdraw = (float(withdraw))

    while balance > withdraw:

        if withdraw > balance:
            print('Insufficient funds. Get back to work.')

        elif balance >= withdraw:
            New_Balance = balance - withdraw
            print(f'Your balance is now {New_Balance}.')

        exit = input('Are you finished? Enter "Exit" if finished. ')

        if(exit == 'Exit'):
            break

        elif(exit == 'No'):
            input('How much would you like to withdraw from your balance? ')
          
(ATM(500, withdraw))

"""if withdraw > balance:
                print('Insufficient funds. Get back to work.')

            elif balance >= withdraw:
                New_Balance = balance - withdraw
                print(f'Your balance is now {New_Balance}.')

                input('Are you finished? ')"""