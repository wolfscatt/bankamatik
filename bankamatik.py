omerHesap = {
    'Ad':'Ömer Faruk BİNGÖL',
    'Hesap No':'232132894',
    'Bakiye': 3500,
    'Ek Hesap Bakiye': 1300
    }

TunahanHesap = {
    'Ad':'Tunahan PAMUK',
    'Hesap No':'581123724',
    'Bakiye': 5000,
    'Ek Hesap Bakiye': 1000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['Ad']}")
    if(hesap['Bakiye']>= miktar):
        hesap['Bakiye'] -= miktar
        print("Paranızı çekebilirsiniz.")
    else:
        toplam = hesap['Bakiye'] + hesap['Ek Hesap Bakiye']
        if(toplam >= miktar):
            ekHesapKullan = input('Ek Hesap Kullanılsın mı? (e/h)')
            if(ekHesapKullan=='e'):
                ekHesapKullanilacakMiktar = miktar - hesap['Bakiye']
                hesap['Bakiye'] = 0
                hesap['Ek Hesap Bakiye'] -= ekHesapKullanilacakMiktar
                print("Ek Hesap Kullanımı Başarılı. Paranızı Çekebilirsiniz.")
            else:
                print(f"{hesap['Hesap No']} no'lu hesabınızda {hesap['Bakiye']} TL bulunmaktadır.")
        else:
            print(f"Üzgünüz Hesabınızda Toplam {toplam} TL Bulunmaktadır.")

paraCek(omerHesap,5000)
