class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_access_level(self):
        return self.__access_level

    def __str__(self):
        return f"User(ID: {self.__user_id}, Name: {self.__name}, Access Level: {self.__access_level})"


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'

    def add_user(self, user_list, user_id, name):
        new_user = User(user_id, name)
        user_list.append(new_user)
        print(f"Пользователь {name} добавлен в систему.")

    def remove_user(self, user_list, user_id):
        for user in user_list:
            if user.get_user_id() == user_id:
                user_list.remove(user)
                print(f"Пользователь с ID {user_id} удалён из системы.")
                return
        print(f"Пользователь с ID {user_id} не найден.")

    def __str__(self):
        return f"Admin(ID: {self.get_user_id()}, Name: {self.get_name()}, Access Level: {self.__access_level})"


if __name__ == "__main__":
    users = []

admin = Admin(1, "John Admin")

admin.add_user(users, 2, "Alice User")
admin.add_user(users, 3, "Bob User")

for user in users:
    print(user)

admin.remove_user(users, 2)

for user in users:
    print(user)