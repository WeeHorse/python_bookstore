from User import User

# final class Customer extends User
class Customer(User):
    def __init__(self, name, email, password, cart):
        super().__init__(name, email, password)
        self.name = name
        self.email = email
        self.password = password
        self.cart = cart

    

