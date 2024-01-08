#Debug true es el modo de desarrollo para que actualice automaticamente
class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Su_Contrasena'
    MYSQL_DB = 'Especies'
    

config = {
    'development': DevelopmentConfig
}