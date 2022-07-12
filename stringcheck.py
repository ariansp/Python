def punyaHuruf (kataPertama, kataKedua):
 
    for char in kataPertama.casefold():
        if char in kataKedua.casefold():
            return True
        else:
            return False
 
print(punyaHuruf('cat','antarctica'))
print(punyaHuruf('cat','australia'))
print(punyaHuruf('cat','ANTARCTICA'))