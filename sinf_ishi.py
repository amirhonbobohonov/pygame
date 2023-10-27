import datetime


class User:
    users = []

    def __init__(self, fist_name, last_name, username, password):
        self.first_name = fist_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.created_date = datetime.datetime.today()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_info(self):
        print(
            self.first_name,
            self.last_name,
            self.username,
            self.password,
            self.created_date
        )

    def register(self):
        first_name = self.first_name
        last_name = self.last_name
        username = self.username
        password = self.password
        created = self.created_date

        filtered_user = list(filter(lambda user: user.get('username') == username, self.users))
        if len(filtered_user) != 0:
            for user in filtered_user:
                print(f"{user.get('username')}-Malumotlar bazasida mavjud!")
        else:
            self.users.append(
                {
                    "first_name": first_name,
                    "last_name": last_name,
                    "username": username,
                    "password": password,
                    "created": created
                }
            )
            print(f'{self.first_name}-foydalnuvchisi malumotlar bazasida yaratildi!')


while True:
    print("1. Ro'hattan o'tish")
    print("2. Foydalnuvchilar ro'yhati")
    print("3. Tizmda chiqish")

    selection = int(input())

    if selection == 1:
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        username = input("Username: ")
        password = input("password: ")

        user = User(
            fist_name=first_name, last_name=last_name,
            username=username, password=password
        )
        user.register()

    elif selection == 2:
        for user in User.users:
            print(user.get('first_name'), user.get('last_name'), user.get('created'))

    elif selection == 3:
        break
