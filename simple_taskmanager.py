class Tehtava:
    id = 0
    def __init__(self, kuvaus: str, koodari: str, tyomaara: int):
        Tehtava.id += 1
        self.valmis = False
        self.kuvaus = kuvaus
        self.koodari = koodari
        self.tyomaara = tyomaara
        self.id = Tehtava.id

        self.valmistxt = "VALMIS" if self.valmis == True else "EI VALMIS"

    def on_valmis(self):
        return self.valmis
    
    def merkkaa_valmiiksi(self):
        self.valmis = True

    def __str__(self):
        self.__valmistxt = "VALMIS" if self.valmis == True else "EI VALMIS"
        return f"{self.id}: {self.kuvaus} ({self.tyomaara} tuntia), koodari {self.koodari} {self.__valmistxt}"


class Tilauskirja:
    def __init__(self):
        self.tehtavat = []

    def lisaa_tilaus(self, kuvaus, koodari, tyomaara):
        self.kuvaus = kuvaus
        self.koodari = koodari
        self.tyomaara = tyomaara

        if self.kuvaus == None or self.koodari == None or self.tyomaara == None:
            return
        else:
            self.tehtavat.append(Tehtava(self.kuvaus, self.koodari, self.tyomaara))

    def kaikki_tilaukset(self):
        return self.tehtavat

    def koodarit(self):
        koodarit2 = []
        for k in self.tehtavat:
            koodarit2.append(k.koodari)
        return list(set(koodarit2))

    def merkkaa_valmiiksi(self, id: int): 
        idt = [t.id for t in self.tehtavat]
        if id not in idt:
            raise ValueError()

        for t in self.tehtavat:
            if t.id == id:
                t.merkkaa_valmiiksi()

    def valmiit_tilaukset(self):
        return [v for v in self.tehtavat if v.valmis == True]

    def ei_valmiit_tilaukset(self):
        return [v for v in self.tehtavat if v.valmis == False]

    def koodarin_status(self, koodari: str):
        if koodari not in self.koodarit():
            raise ValueError()
        
        vt = 0
        evt = 0
        valmiit = len([v for v in self.tehtavat if v.koodari == koodari and v.valmis == True])
        ei_valmiit = len([v for v in self.tehtavat if v.koodari == koodari and v.valmis == False])
        vt += sum([v.tyomaara for v in self.tehtavat if v.koodari == koodari and v.valmis == True])
        evt += sum([v.tyomaara for v in self.tehtavat if v.koodari == koodari and v.valmis == False])

        return (valmiit, ei_valmiit, vt, evt)


class TilauskirjaSovellus:

    def valikko(self):
        print("komennot:\n0 lopetus\n1 lisää tilaus\n2 listaa valmiit\n3 listaa ei valmiit\n4 merkitse tehtävä valmiiksi\n5 koodarit\n6 koodarin status")

    def suorita(self):
        tk = Tilauskirja()
        self.valikko()
        while True:
            
            komento = input("\nkomento: ")
            if komento == "0":
                break

            elif komento == "1":
                try:
                    kuvaus = input("kuvaus: ")
                    koodari_tyomaara = input("koodari ja työmääräarvio:")
                    koodari = koodari_tyomaara.split()[0]
                    tyomaara = int(koodari_tyomaara.split()[1])

                    # if koodari == "" or int(tyomaara)==
                    
                    tk.lisaa_tilaus(kuvaus, koodari, tyomaara)
                    print("lisätty!")
                except:
                    print("virheellinen syöte")

            elif komento == "2":
                if len(tk.valmiit_tilaukset()) == 0:
                    print("ei valmiita")
                else:
                    for valmiit in tk.valmiit_tilaukset():
                        print(valmiit)

            elif komento == "3":
                if len(tk.ei_valmiit_tilaukset()) == 0:
                    print("kaikki valmiita")
                else:
                    for ei_valmiit in tk.ei_valmiit_tilaukset():
                        print(ei_valmiit)

            elif komento == "4":
                tunniste = input("tunniste: ")
                try:
                    tk.merkkaa_valmiiksi(int(tunniste))
                    print("merkitty valmiiksi")
                except:
                    print("virheellinen syöte")

            elif komento == "5":
                for k in tk.koodarit():
                    print(k)
            elif komento == "6":
                koodari = input("koodari: ")
                try:
                    ko = tk.koodarin_status(koodari)
                    print(f"työt: valmiina {ko[0]} ei valmiina {ko[1]}, tunteja: tehty {ko[2]} tekemättä {ko[3]}")
                except:
                    print("virheellinen syöte")
                

sovellus = TilauskirjaSovellus()
sovellus.suorita()



    


        


