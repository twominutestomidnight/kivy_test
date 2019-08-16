class User:
    def __init__(self, ip, port, login, password, name, origin_image):
        self.ip = ip
        self.port = port
        self.login = login
        self.password = password
        self.name = name
        self.origin_image = origin_image

    def __str__(self):
        return "Configuration user : ip = {ip}, port = {port}, login = {login}, password = {password}, " \
               "username : {name}".format(
            ip=self.ip,
            port=self.port,
            login=self.login,
            password=self.password,
            username=self.name
        )