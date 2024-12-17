#slicing

isim = "Ezgi"

slicing= isim[1:3]

slicing2= isim[1:]

######################

#Casting: Tip dönüştürme

a = 5.1

#input

#x= int(input("Bir sayı girin"))
#print(x)

#print(5==4)

####################################
#if-else-elif

""""
x = int(input("Bir sayı girin: "))
if x%2==0:
    print("Sayınız çift.")
else:
    print("Sayınız tek.")
    
"""
"""
a = int(input("Bir sayı girin: "))
if a<10:
    print("sayı 10'dan küçük.")
elif a==10:
    print("sayı 10'a eşit.")
else:
    print("sayı 10'dan büyük.")    
print("program sona ulaştı")    
"""

#nested if
"""
b = int(input("bir sayı girin "))

if b%2==0:
    if b%3==0:
        print("sayı hem 2'ye 3'e tam bölünüyor.")
    else:
        print("Sayı 2'ye bölünüyor ama 3'e bölünmüyor.")    
"""
#DÖNGÜLER
#While

"""
x = int(input("bir sayı girin: "))

while x<0:
    print("sayı negatif, lütfen pozitif bir sayı girin.")
    x = int(input("bir sayı girin: "))

print("girdiğiniz sayı: " , x)    

"""
"""
x = 0
while x<5:
    print(x)
    x+=1
"""

#FOR
"""
for i in "hey":
    print(i)

toplam = 0
for x in range(101):
    toplam += x
print(toplam)    

for a in range(5): 
    print(a)

toplam = 1
for _ in range(5): #kullanılmayacağı için değişken yerine _ konabilir.
    toplam *=5
print(toplam)    

"""

#continue & break
"""
for i in range(10):
    if i == 3:
        break
    print(i)
"""
"""
x = 0
while x<10:
    x += 1
    if x == 3:
        break
    print(x)
"""
"""
for i in range(10):
    if i == 3:
        print("hey")
        continue
    print(i)
"""
##################################################3
#List
ogrenciler = ["Ezgi", "Melih", "Nazlı"]
notlar = [79, 52, 60]
l = [1, 2, "a", "b", True, 4.5, [1,2,3]]
print(notlar[0])
#elemanlar değiştirilebilir. 
notlar[1] += 5
print(notlar[1])

#elemanları değiştirme
notlar[0:3] = 80, 50, 60
print(notlar)
print(notlar[1])

#Tuple
#Listler gibi, tek farkı elemanların değiştirilemez olması(immutable)

#dictionary
#{key:value}
"""
student_grades = {'Deniz' : 92, 'Kenan' : 81, 'Yağmur' : 73}
print(student_grades["Deniz"])
"""

#set: mutable, indexlenemez.
"""
s = {1,2,3,4,5}
print(s)
"""

#split()
"""
s = "merhaba nasılsın"
print(s.split(" "))
t = "limon,portakal,çilek"
print(t.split(","))
"""
#join(): listenin elemanları arasında belirtilen yapıyı koyup stringe dönüştürür. 

#variable unpacking: birden fazla değişkene tek bir seferde değer verme.
(x, y) = (3, 4)
print(x)

#Enumerate: nesneleri numaralandırmak için kullanılır.
adlar = ["Tyler", "Blake", "Fineas"]

for i, e in enumerate(adlar):
    print(i, "indexindeki eleman: ", e)

#HACKERRANK

A = "Ali,Ayşe,Fatma,Kaan,Kerem"
B = "Ali,Veli,Ahmet"

# Listeleri oluştur
A = "Ali,Ayşe,Fatma,Kaan,Kerem"
B = "Ali,Veli,Ahmet"

words_A = A.split(",")
words_B = B.split(",")
"""
# Ortak değerleri bul
common_words = []
for word in words_A:
    if word in words_B:
        common_words.append(word)

# Sonuçları yazdır
print("List A:", words_A)
print("List B:", words_B)
if common_words:
    print("Ortak Değerler:", common_words)
else:
    print("Ortak değer yok.")
"""
    
############################################3

#HACKERRANK2
"""
n = int(input())
    
mylist = []

a=0    
while a<n:
    a+=1
    values=str(a)
    mylist.append(values)
print("".join(mylist))

"""
#HACKERRANK
"""
def is_leap(year):
    leap = False  
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True  
        else:
            leap = True  
    
    return leap  


year = int(input("Enter a year: "))
print(is_leap(year))

"""

#python bitirme ödevi
"""
def flattened_list(input_list: list):
 flattened = []

 for sublist in input_list:
    for sublist2 in sublist:
        for element in sublist2:
            flattened.append(element)
    

 return flattened          


if __name__ == '__main__':

     mylist = [[['cat','dog'],[2,3]],[[8,7],[1,9]]]

print(flattened_list(mylist))
"""
l = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
l1 = []

def flatten(l):

 for i in l:
    if isinstance(i, list):
        flatten(i)
    else:
        l1.append(i)

flatten(l)
print(l1)

#2
mylist = [[1, 2], [3, 4], [5, 6, 7]]

def reverse_list(inputlist: list):
 for i in inputlist:
        i.reverse()
 inputlist.reverse()    
 return(inputlist)

print(reverse_list(mylist))

 





   
    


   
        
          
    
        