# create and write order to file
def create_write_file(file_name, order_contents):
    with open(file_name, 'a+') as f:
        f.write(order_contents)

def read_file(file_name):
    with open(file_name, 'r') as file:
        y = file.readlines()
        x = 1
        for i in y:
            print(str(x), '-', i.rstrip('\n').title())
            x += 1