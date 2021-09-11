class OptionInvalidError(Exception):

    def __init__(self,option=None):
        self.option = option

    def __str__(self):
        if self.option is not None:
            return f'InvalidOptionError: Option {self.option} does not exist'
        return f'InvalidOptionError: Option is absent'

dic = {'1':'1', '2':'2'}

try:
    op = input('Digite qualquer numero: ')

    if op not in dic.keys():
        raise OptionInvalidError(op)

except OptionInvalidError as err:
    print(err)
except Exception as err:
    print(err)
else: 
    print(dic[op])
