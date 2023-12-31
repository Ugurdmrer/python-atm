from model import collection


class Atm:
    def __init__(self):
        pass
    
    # Login sonrası ekran
    def banking(self,username):
        cursor = collection.find_one({'username': f'{username}'})
        if cursor:
            amount = cursor['amount']
            while True:
                print(f'''
                    
                {amount}

                1-) Para yatır
                2-) Para çek
                3-) Geri git

                ''')
                choice = input('Yapacağınız işlem')
                if choice == "1":
                    amount = self.deposit(amount=amount,username=username)
                elif choice == "2":
                    amount = self.withdraw(amount,username)
        else:
            print('paranız yok para yükleyin')

    # Giriş
    def login(self):
        username = input('Kullanıcı adınız ? ')
        password = input('Şifreniz ? ')
        cursor = collection.find({})

        for client in cursor:
            if client['username'] == username and client['password'] == password:
                print('Giriş başarılı..')
                self.banking(username=username)
            else:
                print('Kullanıcı adı veya şifre yalnış')
    # Kayıt
    def register(self):
        username = input('Kullanıcı adınız ? ')
        name = input('Adınız ? ')
        surname = input('Soyadınız ? ')
        password = input('Şifreniz ? ')

        credentials = {
            'username': username,
            'name': name,
            'surname':surname,
            'password':password,
            'amount': 0
        }
        cursor = collection.find({})
        try:
            for client in cursor:
                if len(cursor) == 0:
                    if credentials['username'] == client['username']:
                        print('kullanıcı adı daha önce kayıtlı.')
                        break
                    else:
                        collection.insert_one(credentials).inserted_id
                        print('Kayıt yapıldı.')
                        break


                    # client = Client(name=name,surname=surname,password=password,isRegistered=True)
                else:
                    collection.insert_one(credentials).inserted_id
                    print('Kayıt yok.')
        except TypeError:
            print("kayıt yapıldı.")
            collection.insert_one(credentials).inserted_id

        

    def withdraw(self,amount,username):
        withdraw_money = input('Kaç para çekmek istiyorsunuz ? ')
        withdraw_money = int(withdraw_money)
        amount = int(amount)
        if withdraw_money > 0:
            amount -= withdraw_money
            mongo_filter = {'username': f'{username}'}
            update_amount = {'$set': {'amount': f'{int(amount)}'}}
            collection.update_one(mongo_filter,update_amount)
            print('Para çekildi.')
            return str(amount)







    # Para yatırma
    def deposit(self,amount,username):
        money = input('Kaç para yatırmak istiyorsunuz ?')
        amount += int(money)
        mongo_filter = {'username': f'{username}'}
        update_amount = {'$set': {'amount': f'{int(amount)}'}}
        collection.update_one(mongo_filter,update_amount)
        print('Para yatırıldı.')
        return amount
        

class Client(Atm):
    def __init__(self,name,surname,password,isRegistered):
        self.name = name,
        self.surname = surname,
        self.isRegistered = isRegistered,
        self.password = password
