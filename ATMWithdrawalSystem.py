def ATM(balance):

    new_balance = balance
    while True:
        withdraw = float(input('How much would you like to withdraw from your balance? '))
        
        if withdraw > new_balance:
            print('Insufficient funds. Get back to work.')

        elif new_balance >= withdraw:
            new_balance = new_balance - withdraw
            print(f'Your balance is now {new_balance}.')

        exit = input('Are you finished? Enter "Exit" if finished. ')

        if(exit == 'Exit'):
            break
       
ATM(500)