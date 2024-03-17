# encapsulation --> hide details
# access modifier: public, protected, private
class Bank:
    def __init__(self, holder_name, initial_deposit):
        self.holder_name = holder_name # public
        self._branch = 'banani 11' # protected
        self.__balance = initial_deposit # private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance = self.__balance - amount
            return amount
        else:
            return f'Fokira taka nii'


rafsan = Bank('choto bhai', 1000)
print(rafsan.holder_name)
rafsan.deposit(4000)
print(rafsan.get_balance())