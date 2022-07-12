#Global Variable
x = "Keren secara global"

def myfunc():
    global x
    x = "Keren secara lokal"
    print("Penggunaan variabel secara "+x)

#In this statament, we call everything inside myfunc()
myfunc()

print("Penggunaan variabel secara "+x)