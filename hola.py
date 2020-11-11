import sys

clients = [ 
    {
        'name': 'Max',
        'company': 'Makeasy',
        'email': 'max@mekasy.io',
        'position': 'Sofware Engineer',
    },
    {
        'name': 'Elef',
        'company': 'Easybill',
        'email': 'elef@easybill.pe',
        'position': 'Data Engineer',
    },
    ]


def add_client(client):
    global clients
    
    if client not in clients:
        clients.append(client)
    else:
        print("The client already exist!!")


def update_client(client_id, updated_client):
    global clients

    if len(clients) - 1 >= client_id:
        clients[client_id] = updated_client
    else:
        print('Client not in client\'s list')


def search_client(client_name):
    global clients
    for client in clients:
        if client != client_name:
            continue
        else:
            return True


def delete_client(client_name):
    global clients
    
    if client_name in clients:
        clients.remove(client_name)
    else:
        print("The client not exist!!")


def list_client():
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'
        .format(uid=idx, 
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']
            ))


def _get_client_from_user():
    client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position'),
    }

    return client


def _get_client_name():
    client_name = None
    while not client_name:
        client_name =  input("What's client Name? ")
        if client_name == 'exit':
            client_name == None
            break
    if not client_name:
        sys.exit()
    return client_name


def _get_client_field(field_name):
    field = None

    while not field:
        field = input('What is the client {}? '.format(field_name))

    return field


def _print_welcome():
    mesaje ="""
        WELCOME TO PLATZI VENTAS
        '*'*50
        What would you lke to do today?
        [C] Create Client
        [R] List Client
        [U] Update Client
        [D] Delete Client
        [S] Search Client
        [E] Salir
        : """
    option  = input(mesaje)
    return option


if __name__ == "__main__":
    
    active = True

    while active:

        option = _print_welcome()
        if option == 'R' or option == 'r':
            list_client()

        elif option == 'C' or option == 'c':

            client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position')
            }
            add_client(client)
            list_client()
        elif option == 'S' or option == 's':
            name = _get_client_name()
            found = search_client(name)
            if found:
                print('The client is in the client\'s list')
            else:
                print('The client: {} is not in our client\'s list'.format(name))

        elif option == 'U' or option == 'u':
            client_id = int(_get_client_field('id'))
            updated_client = _get_client_from_user()
            update_client(client_id, updated_client)
            list_client()

        elif option == 'D' or option == 'd':
            name = _get_client_name()
            delete_client(name)
            list_client()

        elif option == 'E' or option == 'e':
            active = False