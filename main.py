from kitabxana import Kitabxana, Kitab

kitabxana = Kitabxana()
kitabxana.baglanti_yarat()
while True:
    emr = input("Emri yazin:")
    if emr =="create":
        ad = input("Kitabin adini yazin:")
        muellif = input("Muellifin adini yazin:")
        yayim_evi = input("Yayim evinin adini daxil edin:")
        nesr_ili = int(input("Nesr ilini daxil edin:"))
        kitab = Kitab(ad,muellif,yayim_evi,nesr_ili)
        kitabxana.kitab_elave_et(kitab)
        print("Succesfully added!")
    elif emr=="search":
        kitab_adi = input("Kitabin adini yazin:")
        kitabxana.kitab_axtar(kitab_adi)
    elif emr == "show_all":
        kitabxana.kitablari_goster()