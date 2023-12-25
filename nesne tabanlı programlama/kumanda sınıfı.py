çimport random
import time
print("********kumanda uygulaması********")
class kumanda():
    def __init__(self,tv_durumu= "kapalı",ses_ayarları = 0,kanal_listesi = ["trt"],kanal = "trt"):
        self.tv_durumu = tv_durumu
        self.ses_ayarları = ses_ayarları
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_aç(self):
        if(self.tv_durumu == "açık"):
            print("televizyon zaten açık")
        else:
            self.tv_durumu = "açık"
            print("televizyon açıldı")

    def tv_kapat(self):
        if(self.tv_durumu == "kapalı"):
            print("televizyon zaten kapalı")
        else:
            self.tv_durumu = "kapalı"
            print("televizyon kapandı")

    def ses_ayar(self):
        while True:
            gir = input("azaltmak için : '-'\nartırmak için : '+'\nçıkmak için : 'çıkış'\ngirin:")
            if(gir == "-"):
                if(self.ses_ayarları != 0):
                    self.ses_ayarları -= 1
                    print("ses:",self.ses_ayarları)
            elif(gir == "+"):
                if(self.ses_ayarları != 32):
                    self.ses_ayarları += 1
                    print("ses:",self.ses_ayarları)
            else:
                print("güncel ses:",self.ses_ayarları)
                break

    def kanal_değiştir(self):
        rastgele = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        print("şuan açık olan kanal:",self.kanal)

    def kanal_ekle(self,yeni_kanal):
        print("kanal ekleniyor..")
        time.sleep((1))
        print("kanal eklendi")
        self.kanal_listesi.append(yeni_kanal)
    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return "tv durumu: {}\nses: {}\nkanallar: {}\nkanal: {}".format(self.tv_durumu,self.ses_ayarları,self.kanal_listesi,self.kanal)


kumanda = kumanda()
print("tv açmak için : 1\ntv kapatmak için: 2\nses ayarları için :3\nkanal değiştirmek için: 4\nkanal eklemek için: 5\nkanal sayısı için :6\ntv durumu için: 7\nçıkmak için: 'q'\n**********************************")

while True:
    işlem = input("yapmak istediğiniz işlemi giriniz:")
    if(işlem == "q"):
        print("programdan çıkıldı")
        break
    elif (işlem == "1"):
        kumanda.tv_aç()
    elif (işlem == "2"):
        kumanda.tv_kapat()
    elif (işlem == "3"):
        kumanda.ses_ayar()
    elif (işlem == "4"):
        kumanda.kanal_değiştir()
    elif (işlem == "5"):
        ekle = input("eklemk istediğiniz kanlları aralarında ',' olacak şekilde giriniz:")
        eklenenler = ekle.split(",")
        for i in eklenenler:
            kumanda.kanal_ekle(i)
    elif (işlem == "6"):
        print("kanal sayısı:",len(kumanda))
    elif (işlem == "7"):
        print(kumanda)
    else:
        print("geçersiz işlem")





