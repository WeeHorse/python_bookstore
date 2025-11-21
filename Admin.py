from User import User

# final class Admin extends User
class Admin(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.name = name
        self.email = email
        self.password = password

