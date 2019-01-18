"""
Assignment 4 Program: ATM that gives you 3 chances to write the correct pin
"""
def main():
    """ Main function code here"""
print('     ***Welcome to DT Bank!***'
      '\n***Please follow the steps below***')
COUNTER = 0
while COUNTER < 10:
    COUNTER += 1
    PIN = str(input('Please enter your 4 digit numerical Pin:    '))
    if COUNTER == 3 and PIN != '1234':
        print('Account Locked: Please Contact Corporate Security')
        break
    if PIN != '1234':
        print('Invalid Pin!')
        continue
    if PIN == "1234":
        print('Your Balance is $22,000. Goodbye!')
        break
if __name__ == '__main__':
    main()
