import random

class generate_password():
    symbol = ['@','#']
    digits = ['0','1','2','3','4','5','6','7','8','9']
    password_length = 8
    
    def generate_char_password(self):
        combined_char = self.digits + self.symbol
        # take a at least one symbol for first character for password string
        symbol_char = random.choice(self.symbol)
        password = symbol_char
        # generate the 6 randon choice character from combine character.
        for x in range(self.password_length - 2):
            password = password + random.choice(combined_char)
        # generate and add last symbol in password string
        last_char = random.choice(self.symbol)
        full_password = password + last_char
        return full_password

password = generate_password()  # creating the objects
print(password.generate_char_password())    # call the class method for generate password.

