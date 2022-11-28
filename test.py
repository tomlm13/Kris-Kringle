from random import randint
secret_santas_kelly = {
    'name' : 'Kelly',
    'secret_one' : '',
    'secret_two' : '',
    'buyer_one' : '',
    'buyer_two' : ''
}
secret_santas_jason = {
    'name' : 'Jason',
    'secret_one' : '',
    'secret_two' : '',
    'buyer_one' : '',
    'buyer_two' : ''
}
secret_santas_tom = {
    'name' : 'Tom',
    'secret_one' : '',
    'secret_two' : '',
    'buyer_one' : '',
    'buyer_two' : ''
}
secret_santas_mike = {
    'name' : 'Mike',
    'secret_one' : '',
    'secret_two' : '',
    'buyer_one' : '',
    'buyer_two' : ''
}
secret_santas_andy = {
    'name' : 'Andy',
    'secret_one' : '',
    'secret_two' : '',
    'buyer_one' : '',
    'buyer_two' : ''
}
secret_santas_dan = {
    'name' : 'Dan',
    'secret_one' : '',
    'secret_two' : '',
    'buyer_one' : '',
    'buyer_two' : ''
}
rando_list = []
santa_list = [secret_santas_kelly,secret_santas_jason,secret_santas_tom,secret_santas_mike,secret_santas_andy,secret_santas_dan]

for iter_one,i in enumerate(santa_list):
    while i['secret_one'] == '':
        x = randint(0,((len(santa_list))-1))
        if(x != iter_one and rando_list.count((santa_list[x])['name']) < 1):
            if(i['secret_one'] == '' and (santa_list[x])['buyer_one'] == ''):
                i['secret_one'] = (santa_list[x])['name']
                (santa_list[x])['buyer_one'] = i['name']
                rando_list.append((santa_list[x])['name'])

rando_list = []

for iter,j in enumerate(santa_list):
    while j['secret_two'] == '':
        y = randint(0,((len(santa_list))-1))
        if(y != iter and rando_list.count((santa_list[y])['name']) < 1):
            if((j['secret_two'] == '' and (santa_list[y])['buyer_two'] == '') and (santa_list[y]['name'] != j['secret_one'])):
                j['secret_two'] = (santa_list[y])['name']
                (santa_list[y])['buyer_two'] = j['name']
                rando_list.append((santa_list[y])['name'])

print(santa_list)
print(rando_list)

