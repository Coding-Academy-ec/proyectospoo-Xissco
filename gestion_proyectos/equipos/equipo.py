class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"Usuario: {self.name}, Correo: {self.email}"

class Team:
    def __init__(self, id):
        self.id = id
        self.users = []
    
    def add_user(self, user):
        self.users.append(user)
        
    def __str__(self):
        users = ""
        users = [users + str(user) + "\n" for user in self.users]
        return f'Equipo: {self.id}\nConformado por {"".join(users)}'