from functions import *

order_list = []
food_list = []
order_no = 1

while True:
    print('1. Create an order')
    print('2. Display an order')
    print('3. Exit')
    menu = int(input('Please select a menu number. e.g \'2\'\n'))

    if menu == 1:
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
        food_list = []
        order_no += 1

    if menu == 2:
        # As a user I want to see my order
        while True:
            which_order = int(input('Please enter the number of the order e.g. \'1\'\n'))
            print(read_file('order' + str(which_order) + '.txt'))
            input('\n Press enter/return to continue.\n')
            break

    if menu == 3:
        print('Have a great day!')
        break