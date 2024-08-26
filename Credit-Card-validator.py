def checkSum(card_number):
    sum = 0
    x = len(card_number)
    for i in range(x-2,-1,-2):
        doubled = int(card_number[i]) * 2
        sum += (doubled if doubled < 10 else doubled - 9)
    for i in range(x-1,-1,-2):
        sum += int(card_number[i])
    return sum % 10 == 0
def validate(cardNumber):
    if not cardNumber.isdigit():
        print("Not valid card")
    elif cardNumber.startswith(('34', '37')):
        if(checkSum(cardNumber)==True):
            print("American Express")
        else:
            print("Not valid card")
    elif cardNumber.startswith(('51', '52','53','54','55'),):

        if(checkSum(cardNumber)==True):
            print("MasterCard")
        else:
            print("Not valid card")
    elif cardNumber.startswith(('4')):
        if(checkSum(cardNumber)==True):
            print("visa")
        else:
            print("Not valid card")
    else:
        print("Not valid card")
validate("378282246310005")
validate("5555555555554444")
validate("4111111111111111")
validate("1234567890")
