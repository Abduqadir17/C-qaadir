pn = 7786
haraaga = 909
mobile_ka= 610000000
aqoonsiga= 611111111
haraa= 1087
lambark_sirta=5564
account_ka= 55555555
pin_ka_cusub=5542
I_number=612222222
C_number=613333333
magaca="Cabdi Cali Cabdi"
haraa_Bill=850
pin = int(input("Fadlan gali biinkaaga: "))
if pin == pn:
    print("1. Itus Haragayga.")
    print("2. Kaarka ku hadalka.")
    print("3. Bixi biilka")
    print("4. U wareeji EVC-PLUS")
    print("5. Warbixin kooban")
    print("6. Salaam bank")
    print("7.Maareynta")
    print("8.Taaj")
    print("9. Bill payment")
    print("0. kabax")
          
else:
    print("Lambarka sirta ah waa qalad. Fadlan soo gali markale.")

next_step = int(input())
if next_step == 1:
    print("Haraagaagu waa ", haraaga)

elif next_step == 2:
    print("1. Ku shubo airtime.")
    print("2. Ugu shub airtime.")
    print("3. MIFI backages.")
    print("4. ku shubo internet")
    print("5. ugu shub qof kale(MMMT)")
    airtime = int(input())
    if airtime == 1:
        print("Fadlan gali lacagta:")
        lacagta = int(input())
        print("Ma hubtaa inaad lacaga ugu shubto: ")
        print("1. HAA")
        print("2. MAYA")
        haamaya = int(input())
        if haamaya == 1:
            print("Waa lagu shubay")
        else:
            if haamaya == 2:
                print("Waa laga noqday")
            else:
                print("Macasalaama!")
        if airtime == 2:
            print("fadlan geli mobile_ka") 
        mobile_ka =int(input()) 
        print("fadlan geli lacagta")
        lacagta = int(input())  
        print("ma hubtaa inaad lacagta ugu shubtid mobile_ka")    
        print("1. HAA")
        print("2. MAYA")
        HAAMAYA = int(input())
        if HAAMAYA == 1:
            print("waa ugu shubtay")
        if HAAMAYA == 2:
            print("waa laga noday")
        else:
            print("macsalaama") 
        if airtime == 3:
            print("1.ku shubo internet (MIFI)")   
        ku_shubo = int(input()) 
        if ku_shubo == 1:
            print("1. isbuucle(weekly)")           
            print("2. maalinle(daily)")
            print("3. bille(mifi)")



elif next_step == 3:
    print("1. postpaid")
    print("2. ku iibso")
    next_biil=int(input())
    if next_biil==1:
        print("1.Ogow biilka")
        print("2.Bixi Biil")
        print("3.Ka bixi Biil")
    if next_biil==2:   
        print(int(input("Fadlan geli pinkaaga:")))
elif next_step==4:
    print("fadlan geli mobile-ka")
    mobile_ka= int(input())
    print("fadlan geli lacagta")
    lacagta=int(input())
    print("ma hubtaa inaad lacagta u wareejisid moile-kaan")
    print("1.Haa")
    print("2.Maya")
    Haamaya=int(input())
    if Haamaya==1:
        print("Waa lagu guuleystay")
    if Haamaya==2:
        print("waa laga noqday")    
    else:
        print("Macsalaama")
elif next_step==5:
    print("1. Last Action")        
    print("2. Wareejintii u dambeysay")
    print("3. iibsashadii u dambeysay")
    print("4.Last three Action")
    print("5.Email me my activity")
warbixin=int(input())  
if warbixin==1:
    print("u soo saar last action-kiisa")  
if warbixin==2:
    print("1. u dirtay")   
    print("2. ka heshay") 
dookh=int(input())  
if dookh==1:
    print("fadlan geli mobile-ka")  
    mobile_ka=int(input())
    print("operation succeed")
if dookh==2:
    print("fadlan geli mobile-ka")  
    mobile_ka=int(input())
    print("operation succeed")
if warbixin==3:
    print("fadlan geli aqoonsiga") 
    aqoonsiga=int(input())   
    print("operation succeed")
if warbixin==4:
    print("Last three action-kaaga waa")
if warbixin==5:
    print("fadlan geli Email-kaaga")  
elif next_step==6:
    print("1. itus haraaga")   
    print("2. lacag dhigasho") 
    print("3.lacag qaadasho")  
    print("4.ka wareeji Evc plus")
    print("5.ka wareeji accounkaaga")
    print("6.hubi wareejin Account")
    print("7.maareynta bankiga")
    print("8.Kala bax")
    salaam=int(input())
    if salaam==1:
        print("haraagaagu waa", haraa, "$")
    if salaam==2:
        print("fadlan geli lacagta")  
        lacagta=int(input())  
        print("Fadlan geli macluumaad")
        macluumaad=input()
        print("fadlan geli lambarka sirta ee bankiga")
        lambark_sirta=int(input)
        print("ma hubtaa inaad lacag dhiagatid accountkaaga bankiga")
        print("1.haa")
        print("2.maya")
        mayahaa=int(input())
        if mayahaa==1:
            print("waa lagu guuleystay")
        if mayahaa==2:
            print("waa laga noqday")  
        else:
            print("macsalaama")  
    if salaam==3:
        print("fadlan geli lacagta") 
        lacagta=int(input())  
        print("fadlan geli macluumaad")   
        macluumaad=input() 
        print("fadlan geli lambarka sirta ee bankiga ") 
        lambark_sirta=int(input())    
        print("ma hubtaa inaad lacagtaan ka qaadatid accountkaaga bankiga ")
        print("1.haa")
        print("2.maya")
        HaaMaya=int(input())
        if HaaMaya==1:
            print("waa lagu guuleystay")
        if HaaMaya==2:
            print("waa laga noqday")
        else:
            print("macsalaama")   
    if salaam==4:
        print("1.SALAAM SOMALI BANK")
        print("2.daarasalaam bank") 
        print("3.Bank beeraha")   
        print("4.Salaam Sch")    
    insalaam=int(input()) 
    if insalaam==1:
        print("Fadlan geli account_ka")  
        account_ka=int(input())  
        print("fadlan geli macluumaad")
        macluumaad=input()
        print("fadlan geli lambarka sirta ee bankiga ") 
        lambark_sirta=int(input())    
        print("ma hubtaa inaad lacagtaan ka wareejisid Evc plus_ka ")
        print("1.haa")
        print("2.maya")
        HaaMAya=int(input())
        if HaaMAya==1:
            print("waa lagu guuleystay")
        if HaaMAya==2:
            print("waa laga noqday")
        else:
            print("macsalaama") 
    if insalaam==2:
        print("Fadlan geli account_ka")  
        account_ka=int(input())  
        print("fadlan geli macluumaad")
        macluumaad=input()
        print("fadlan geli lambarka sirta ee bankiga ") 
        lambark_sirta=int(input())    
        print("ma hubtaa inaad lacagtaan ka wareejisid Evc plus_ka ")
        print("1.haa")
        print("2.maya")
        HaaMAYa=int(input())
        if HaaMAYa==1:
            print("waa lagu guuleystay")
        if HaaMAYa==2:
            print("waa laga noqday")
        else:
            print("macsalaama")
    if insalaam==3:
        print("Fadlan geli account_ka")  
        account_ka=int(input())  
        print("fadlan geli macluumaad")
        macluumaad=input()
        print("fadlan geli lambarka sirta ee bankiga ") 
        lambark_sirta=int(input())    
        print("ma hubtaa inaad lacagtaan ka wareejisid Evc plus_ka ")
        print("1.haa")
        print("2.maya")
        HaaMAYA=int(input())
        if HaaMAYA==1:
            print("waa lagu guuleystay")
        if HaaMAYA==2:
            print("waa laga noqday")
        else:
            print("macsalaama")  
    if insalaam==4:
        print("Fadlan geli account_ka")  
        account_ka=int(input())  
        print("Fadlan geli account_ka")  
        account_ka=int(input())  
        print("fadlan geli macluumaad")
        macluumaad=input()
        print("fadlan geli lambarka sirta ee bankiga ") 
        lambark_sirta=int(input())    
        print("ma hubtaa inaad lacagtaan ka wareejisid Evc plus_ka ")
        print("1.haa")
        print("2.maya")
        HaaMAya=int(input())
        if HaaMAya==1:
            print("waa lagu guuleystay")
        if HaaMAya==2:
            print("waa laga noqday")
        else:
            print("macsalaama") 
    if salaam==5:
        print("fadlan geli account ama mobile") 
        account_ka=int(input())
        mobile_ka=int(input()) 
        print("Fadlan geli account_ka")  
        account_ka=int(input())  
        print("fadlan geli macluumaad")
        macluumaad=input()
        print("fadlan geli lambarka sirta ee bankiga ") 
        lambark_sirta=int(input())    
        print("ma hubtaa inaad lacagtaan ku wareejinaysid account kale ")
        print("1.haa")
        print("2.maya")
        Haa_maya=int(input())
        if Haa_maya==1:
            print("waa lagu guuleystay")
        if Haa_maya==2:
            print("waa laga noqday")
        else:
            print("macsalaama") 
    if salaam ==6:
        print("fadlan geli OTP ")    
        OTP=input()    
        print("ma hubtaa inaad aqbasho lacag diriddaan")
        print("1. haa")
        print("2. maya")
        HAA_MAYA=int(input())
        if HAA_MAYA==1:
            print("waa lagu guuleystay")
        if HAA_MAYA==2:
            print("waa laga noqday")
        else:
            print("macsalaama")    
    if salaam ==7:
        print("1. bedel pin_ka bangiga")    
        print("2. Bedel passworska Ebank") 
        bedelid=int(input())  
        if bedelid==1:
            print("Fadlan geli lambarkaaga sirta ee bankiga")    
            lambark_sirta=int(input()) 
            print("fadlan geli pin_ka cusub")
            pin_ka_cusub=int(input())
            print("hubi pin_ka_cusub")
            pin_ka_cusub=int(input())
            print("waa lagu guuleystay")
        if bedelid==2:
            print("Fadlan geli lambarkaaga sirta ee bankiga")    
            lambark_sirta=int(input()) 
            print("fadlan geli pin_ka cusub")
            pin_ka_cusub=int(input())
            print("hubi pin_ka_cusub")
            pin_ka_cusub=int(input())
            print("waa lagu guuleystay")
    if salaam ==8:
        print("fadlan geli aqoonsiga codsiga")   
        aqoonsiga =int(input())   
        print("fadlan geli lacagta") 
        lacagta=int(input())
        print("ma hubtaa inaad kala baxdo")
        print("1.haa")
        print("2.maya")
        Haa_Maya=int(input())
        if Haa_Maya==1:
            print("waa lagu guulrystay")
        if Haa_Maya==2:
            print("waa laga noqday") 
        else:
            print("macsalaama")    
elif next_step==7:
    print("1. bedel lambarka sirta")  
    print("2.bedel luqada")  
    print("3.wargelin mobile lumay")   
    print("4. lacag xirasho")   
    print("u celi lacag qaldantay")   
    print("enable mobile banking")  
    maareyn=int(input())
    if maareyn==1:
        print("fadlan geli pin_kaaga cusub")
        pin_ka_cusub=int(input())
        print("fadlan hubi pin_ka cusub")
        pin_ka_cusub=int(input())
        print("waa algu guuleystay")
    if maareyn ==2:
        print("1.English")  
        print("2. Somali") 
    luqad=int(input())    
    if luqad==1:
        print("waad ku guulesatay inaad bedesho luqadda")
    if luqad==2:
        print("waad ku guuleysatay inaad bedesho luqadda")
    if maareyn==3:
        print("fadlan geli mobile_ka lumay")   
        mobile_ka=int(input())  
        print("fadlan geli lambarkiisa sirta")  
        lambark_sirta=int(input()) 
        print("ma hubtaa inaad diiwaan geliso mobile_kaan lumay")
        print("1.haa")
        print("2.maya")
        haa_MAYA=int(input())
        if haa_MAYA==1:
            print("waa lagu guuleystay")
        if haa_MAYA==2:
            print("waa laga noqday") 
        else:
            print("macsalaama")  
    if maareyn==4:
        print("fadlan geli numberka khaladka ah  ")   
        I_number=int(input()) 
        print("fadlan geli lambarka loo rabay")
        C_number=int(input())
        print("fadlan geli macluumaad")
        macluumaad=input()
        print("ma hubtaa inaad xirato lacagtaan")
        print("1.haa")
        print("2.maya")
        HAA_maya=int(input())
        if HAA_maya==1:
            print("waa lagu guuleystay")
        if HAA_maya==2:
            print("waa laga noqday") 
        else:
            print("macsalaama") 
    if maareyn==5:
        print("fadlan geli aqoonsiga lacag diridda")   
        aqoonsiga=int(input()) 
        print("fadlan geli macluumaad")
        macluumaad=input() 
        print("ma hubtaa inaad dirto lacagtaan") 
        print("1. haa")
        print("2.maya")
        maya_haa=int(input())
        if maya_haa==1:
            print("waa lagu guuleystay")
        if maya_haa==2:
            print("waa laga noqday")  
        else:
            print("macsalaama") 
    if maareyn==6:
        print("fadlan geli lambarka isdiie=waan gelinta")  
        mobile_ka=int(input())   
elif next_step==8:
    print("1.gudaha") 
    print("2.dibadda") 
    print("3. ogoow khidmadda")   
    print("4.macluumaadka xawaaladda")  
    print("5. jooji xawaaladda")  
    print("6. fur xawaaladda")  
    taaj=int(input())  
    if taaj==1:
        print("E_kaafi") 
        print("E_sahal") 
        E_taaj=int(input())
        if E_taaj==1:
            print("fadlan geli lambarka qaataha")
        mobile_ka=int(input()) 
        print("fadlan geli magaca qaataha oo seddexan")  
        magaca=input() 
        print("ma hubtaa")
        print("1.haa")
        print("2.maya")
        MAYA_haa=int(input())
        if MAYA_haa==1:
            print("waa lagu guuleystay")
        if MAYA_haa==2:
            print("waa laga noqday")  
        else:
            print("macsalaama")      
        if E_taaj==2:
            print("fadlan geli lambarka qaataha")
        mobile_ka=int(input()) 
        print("fadlan geli magaca qaataha oo seddexan")  
        magaca=input() 
        print("ma hubtaa")
        print("1.haa")
        print("2.maya")
        MAYA_HAA=int(input())
        if MAYA_HAA==1:
            print("waa lagu guuleystay")
        if MAYA_HAA==2:
            print("waa laga noqday")  
        else:
            print("macsalaama") 
        if taaj==2:
            print("fadlan geli lambarka qaataha")
        mobile_ka=int(input()) 
        print("fadlan geli magaca qaataha oo seddexan")  
        magaca=input() 
        print("ma hubtaa")
        print("1.haa")
        print("2.maya")
        mAYA_hAA=int(input())
        if mAYA_hAA==1:
            print("waa lagu guuleystay")
        if mAYA_hAA==2:
            print("waa laga noqday")  
        else:
            print("macsalaama") 
        if taaj==3:
            print("1. pay to evc plus")
            print("2. Taaj") 
            print("3. Taajpay") 
            print("4. New Etaaj") 
            print("5. taajIPS") 
            taaj_3=int(input())
            if taaj_3==1:
                print("fadlan geli taleefanka qaataha")
                mobile_ka=int(input())
                print("fadlan geli lacagta")
                lacagta=int(input())
                print("ma hubtaa")
                print("1.haa")
                print("2.maya")
                MAYa_HAa=int(input())
                if MAYa_HAa==1:
                    print("waa lagu guuleystay")
                if MAYa_HAa==2:
                    print("waa laga noqday") 
                else:
                    print("macsalaama")
            if taaj_3==2:
                print("fadlan geli taleefanka qaataha")
                mobile_ka=int(input())
                print("fadlan geli lacagta")
                lacagta=int(input())
                print("ma hubtaa")
                print("1.haa")
                print("2.maya")
                MAya_Haa=int(input())
                if MAya_Haa==1:
                    print("waa lagu guuleystay")
                if MAya_Haa==2:
                    print("waa laga noqday") 
                else:
                    print("macsalaama")
            if taaj_3==3:
                print("fadlan geli taleefanka qaataha")
                mobile_ka=int(input())
                print("fadlan geli lacagta")
                lacagta=int(input())
                print("ma hubtaa")
                print("1.haa")
                print("2.maya")
                MaYa_haa=int(input())
                if MaYa_haa==1:
                    print("waa lagu guuleystay")
                if MaYa_haa==2:
                    print("waa laga noqday") 
                else:
                    print("macsalaama")
            if taaj_3==4:
                print("fadlan geli taleefanka qaataha")
                mobile_ka=int(input())
                print("fadlan geli lacagta")
                lacagta=int(input())
                print("ma hubtaa")
                print("1.haa")
                print("2.maya")
                MaYa_HAa=int(input())
                if MaYa_HAa==1:
                    print("waa lagu guuleystay")
                if MaYa_HAa==2:
                    print("waa laga noqday") 
                else:
                    print("macsalaama")  
            if taaj_3==5:
                print("fadlan geli taleefanka qaataha")
                mobile_ka=int(input())
                print("fadlan geli lacagta")
                lacagta=int(input())
                print("ma hubtaa")
                print("1.haa")
                print("2.maya")
                MaYa_HAA=int(input())
                if MaYa_HAA==1:
                    print("waa lagu guuleystay")
                if MaYa_HAA==2:
                    print("waa laga noqday") 
                else:
                    print("macsalaama")              


        if taaj==4:
            print("fadlan geli aqoonsiga lacag diridda")   
            aqoonsiga=int(input()) 
            print("fadlan geli macluumaad")
            macluumaad=input() 
            print("ma hubtaa inaad dirto lacagtaan") 
            print("1. haa")
            print("2.maya")
            maya_hAa=int(input())
            if maya_hAa==1:
                print("waa lagu guuleystay")
            if maya_hAa==2:
                print("waa laga noqday")
            else:
                print("macsalaama") 
        if taaj==5:
            print("fadlan geli aqoonsiga lacag diridda")   
            aqoonsiga=int(input())    
            print("fadlan geli macluumaad")
            macluumaad=input()
            print("ma hubtaa in aad xirto aqoonsiga xawilaadda lambarkaan")
            print("1.haa")
            print("2. maya")
            mAYA_HAA=int(input())
            if mAYA_HAA==1:
                print("waa lagu guuleystay")
            if mAYA_HAA==2:
                print("waa laga noqday")  
            else:
                print("macsalaama")
        if taaj==6:
            print("fadlan geli aqoonsiga lacag diridda")   
            aqoonsiga=int(input())      
            print("fadlan geli macluumaad") 
            macluumaad=input() 
            print("ma hubtaa inaad u furto aqoonsiga xawilaadda lambarkaan") 
            maya_haA=int(input())  
            if maya_haA==1:
                print("waa lagu guuleystay")
            if maya_haA==2:
                print("waa laga noqday")  
            else:
                print("macsalaama")

elif next_step==9:
    print("1. itus haraaga Bill_ka")   
    print("2. wada bixi Bill_ka")   
    print("3. Qeyb ka bixi Bill_ka")    
    Bill_ka=int(input())    
    if Bill_ka==1:
        print("haraaga Bill_ka waa", haraa_Bill , "$")   
    if Bill_ka==2:
        print("fadlan geli Bill reference number") 
        mobile_ka=int(input())   
        print("fadlan geli lacagta")
        lacagta=int(input())
        print("fadlan geli macluumaad")
        macluumaad=input()
        print("ma hubtaa inaad wada bixiso bill_ka")
        print("1. haa")
        print("2. maya")
        mayA_haa=int(input())
        if mayA_haa==1:
            print("waa lagu guuleystay")
        if mayA_haa==2:
            print("waa laga noqday")  
        else:
            print("macsalaama")      
    if Bill_ka==3:
        print("fadlan geli Bill reference number") 
        mobile_ka=int(input())   
        print("fadlan geli lacagta")
        lacagta=int(input())
        print("fadlan geli macluumaad")
        macluumaad=input()
        print("ma hubtaa inaad qeyb ka  bixiso bill_ka")
        print("1. haa")
        print("2. maya")
        mAya_haa=int(input())
        if mAya_haa==1:
            print("waa lagu guuleystay")
        if mAya_haa==2:
            print("waa laga noqday")  
        else:
            print("macsalaama") 


        



                        








            
    













        



    

