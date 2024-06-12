class SakuraServerConfig:
    """Represents the configuration for the Sakura Server"""
    def __init__(self, hostname: str, ip_address: str, username: str, password: str):
        self.hostname = hostname
        self.ip_address = ip_address
        self.username = username
        self.password = password