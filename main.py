from functions import *

order_list = []
food_list = []
order_no = 1

while True:
    order = input('Do you want to create an order? y/n\n')
    if order == 'y':
        while True:
            # I want a program to ask for food
            food = str(input('What food do you want? Write \'done\' if you\'re finished\n'))
            if 'done' in food:
                # As a user I ask for any amount of food
                break
            else:
                food_list.append(food)
        # As a user I create different orders(different files)
        [create_write_file('order' + str(order_no) + '.txt', i + '\n') for i in food_list]
        order_list.append(food_list)
        order_no += 1
    elif order == 'n':
        while True:
            list_order = input('Do you want to see your order? y/n\n')
            if list_order == 'y':
                which_order = int(input('Please enter the number of the order e.g. \'1\'\n'))
                print(read_file('order' + str(which_order) + '.txt'))
            elif list_order == 'n':
                break
            else:
                print('Error: Please enter y(yes) or n(no)!!!')
        print ('Have a great day!')
        break
    else:
        print('Error: Please enter y(yes) or n(no)!!!')


