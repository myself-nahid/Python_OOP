class Phone:
    manufactured = 'china'

    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price

    def send_sms(self, phone, sms):
        text = f'sending to: {phone} {sms}'
        print(text)


my_phone = Phone('kala chan', 'oppo', 9800)
print(my_phone.owner, my_phone.brand, my_phone.price)

her_phone = Phone('Mari jan', 'iphone', 120000)
print(her_phone.owner, her_phone.brand, her_phone.price)
