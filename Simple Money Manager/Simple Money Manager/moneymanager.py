class MoneyManager():

    def __init__(self, user_number, pin_number, balance, transaction_list):
        self.user_number = user_number
        self.pin_number = pin_number
        self.balance = balance
        self.transaction_list = transaction_list

    def add_entry(self, amount, entry_type):
        self.balance = str(float(self.balance) - float(amount))
        self.transaction_list.append((entry_type, amount))

    def deposite_funds(self, amount):
        self.balance = str(float(self.balance) + int(amount))

    def get_transaction_string(self):
        transaction_string = str()
        for x in self.transaction_list:
            transaction_string = transaction_string + \
                x[0] + '\n' + str(float(x[1])) + '\n'
        else:
            transaction_string[:-1]
        return transaction_string

    def save_to_file(self):
        file_name = f"{self.user_number}.txt"
        with open(file_name, 'w') as file:
            file.write(self.user_number + '\n')
            file.write(self.pin_number + '\n')
            file.write(self.balance + '\n')
            file.write(self.get_transaction_string())
