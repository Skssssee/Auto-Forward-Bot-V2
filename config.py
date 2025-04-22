from os import environ 

class Config:
    API_ID = environ.get("API_ID", "27479878")
    API_HASH = environ.get("API_HASH", "05f8dc8265d4c5df6376dded1d71c0ff")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8139926505:AAFUbR35uZx4AKeJ42m3Z52TFw3k5vboiNc") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://jowan20678:qGcqHCgAOiYnwG9K@cluster0sddji.3cetple.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0sddji")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0sddji")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7613349267').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
