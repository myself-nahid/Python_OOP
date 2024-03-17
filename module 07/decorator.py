def timer(func):
    def inner():
        print('time started')
        print(func)
        print('time ended')
    return inner

# timer()()

@timer
def get_factorials():
    print('factorial starting')

get_factorials()