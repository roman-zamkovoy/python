def double(arg):
    print('Before: ', arg)
    arg = arg * 2
    print('After: ', arg)

def change(arg: list):
    print('before')
    arg.append('123242y867736')
    print('After: ', arg)


change([1, 2, 3])