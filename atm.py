from model import collection,getAllUsers


class Atm:
    def __init__(self):
        pass

    def login(self):
        username = input('Kullanıcı adınız ?')
        password = input('Şifreniz ?')
        cursor = collection.find({})

        for client in cursor:
            if client['username'] == username and client['password'] == password:
                print('Giriş başarılı..')
            else:
                print('Kullanıcı adı veya şifre yalnış')
        
    def register(self):
        username = input('Kullanıcı adınız ?')
        name = input('Adınız ?')
        surname = input('Soyadınız ?')
        password = input('Şifreniz ?')
        credentials = {
            'username': username,
            'name': name,
            'surname':surname,
            'password':password
        }
        cursor = collection.find({})
        try:
            for client in cursor:
                if len(cursor) == 0:
                    if credentials['username'] == client['username']:
                        print('kullanıcı adı daha önce kayıtlı.')
                        exit()
                    else:
                        collection.insert_one(credentials).inserted_id
                        print('Kayıt yapıldı.')

                    client = Client(name=name,surname=surname,password=password,isRegistered=True)
                else:
                    collection.insert_one(credentials).inserted_id
                    print('Kayıt yok.')
        except TypeError:
            print("kayıt yapıldı.")
            collection.insert_one(credentials).inserted_id

        

    # def withdraw(self):
    #     if self.isLoggedIn == True:
    #         print('giriş yapıldı.')
    #     else:
    #         print('Lütfen Giriş Yapınız.')



    def deposit():
        pass


class Client(Atm):
    def __init__(self,name,surname,password,isRegistered):
        self.name = name,
        self.surname = surname,
        self.isRegistered = isRegistered,
        self.password = password
