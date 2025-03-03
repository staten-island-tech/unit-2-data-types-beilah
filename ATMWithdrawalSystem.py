withdraw = input('How much would you like to withdraw from your balance? ')

def ATM(balance, withdraw):

    withdraw = (float(withdraw))

    if withdraw > balance:
        print('Insufficient funds. Get back to work.')

    elif balance >= withdraw:
        New_Balance = balance - withdraw
        print(f'Your balance is now {New_Balance}.')
    
    return()

(ATM(500, withdraw))