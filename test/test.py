import torchgpipe

seq = ('h', 'e', 'l', 'l', 'o')
print(' '.join(seq))
print(''.join(seq))
for epoch in range(2):
    print(epoch)

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
for i, data in enumerate(seasons, start=0):
    print(i, data)
print('---------\n')

class NewInt(int):
    def __new__(cls, value):
        print('调用__new__方法')
        return int.__new__(cls, abs(value))

a = NewInt(-4.822)
print(a)

