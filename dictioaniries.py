languages={'sam':'english',
           'sara':'french',
           'roy':'russian',
           'dig':'spanish'
            }
names=['sam','sara','ali','vali','anvar']
for name in names:
    if name in languages.keys():
        print(f'Thank you responding to the poll {name.title()}')
    else:print(f'{name.title()} you need to take the poll,please')

     











