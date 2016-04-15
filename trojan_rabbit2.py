num = input('Informe o numero de cavaleiros para a invasão: ');
num_knight = int(num)
enemy = input('Entre com o tipo do inimigo: ');

if enemy == 'Killer Bunny':
    print('Holy Hand Grenade')
else:
    if num_knight < 4:
        print('Retreat')
    elif num_knight >= 10:
        print('Trojan Rabbit !!')
    else:
        print('Truce ?')
