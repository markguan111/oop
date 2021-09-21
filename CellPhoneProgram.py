import CellPhoneClass


def main():
    man = input('Enter the manufacturer:')
    mod = input('Enter the model number:')
    retail = float(input('Enter the retail price:'))

    phone = CellPhoneClass.Phone(man,mod,retail)

    print('Here is the data that you entered:')
    print('manufacturer:', phone.get_manufact())
    print('model Number:',phone.get_model())
    print('Retail Price: $', phone.get_retail_price(), '.2f', sep = '')

main()