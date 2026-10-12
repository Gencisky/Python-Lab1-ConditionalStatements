print("|Ad günu tapmaca oyununa xoş gəlmisiniz!|")
set1=[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]
set2=[2,3,6,7,10,11,14,15,18,19,22,23,26,27,30,31]
set3=[4,5,6,7,12,13,14,15,20,21,22,23,28,29,30,31]
set4=[8,9,10,11,12,13,14,15,24,25,26,27,28,29,30,31]
set5=[16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

print(f" Qrup 1: {set1}\n Qrup 2: {set2}\n Qrup 3: {set3}\n Qrup 4: {set4}\n Qrup 5: {set5}\n")
while True:
    try:
        lst=list(map(int,input("Yuxarıdakı setlere bax ad gunun hansı qrupdadırsa 1 olmayanlar üçün 0 yaz): ").split()))
    except ValueError:
        print("Sehvdir zəhmət olmasa yalnız reqem yaz ")
    else:
        break
first=[1,2,4,8,16]
sum=0
for i in range(5):
    if lst[i]==0:
        continue
    sum+=first[i]
print(sum)