

class Camera:
    def __init__(self, ip, port, login, password):
        self.ip = ip
        self.port = port
        self.login = login
        self.password = password


    def __str__(self):
        return "Configuration camera : ip = {ip}, port = {port}, login = {login}, password = {password}".format(
            ip=self.ip,
            port=self.port,
            login=self.login,
            password=self.password
        )