from atm import Atm




while True:

    choice = input('''
    
    1-) Giriş
    2-) Kayıt
    3-) Çıkış
    
    
    
     : ''' )
    atm = Atm()
    if choice == "1":
        atm.login()
    elif choice == "2":
        atm.register()
    elif choice == "3":
        exit()
    else:
        print('Yalnış seçenek çıkış yapılıyor...')
        exit()
