

def get_account_amount():
    reader = open('AdditionaFiles/remainingAmount.txt', 'r')
    remaining_amount = float(reader.read())
    reader.close()
    return remaining_amount

def change_account_amount(new_amount):
    reader = open('AdditionaFiles/remainingAmount.txt', 'w')
    reader.write(str(new_amount))
    reader.close()