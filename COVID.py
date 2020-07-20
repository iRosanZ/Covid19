from bs4 import BeautifulSoup as Bs
import requests, os

os.system('clear')
covid = requests.get('http://covid19.go.id')
soup = Bs(covid.text, 'html.parser') 
find_1 = soup.find_all('strong')
find_2 = soup.find_all('div', {'class' : 'pt-4 text-color-grey text-1'}) 
find_3 = soup.find_all('div', {'class' : 'pt-4 text-color-black text-1'}) 
negara = find_1[0].text 
terkonfirmasi = find_1[1].text 
meninggal_global = find_1[2].text
keterangan_global = find_2[0].text
positif_indo = find_1[3].text 
sembuh_indo = find_1[4].text 
meninggal_indo = find_1[5].text 
keterangan_indo = find_3[0].text

os.system("figlet COVID 19")
print("")
print("Tools Covid19 By Adip&Rosan&Felix")
print("Only Termux Not Pc/Vps")
print("")
print("[1]LIVE GLOBAL")
print("[2]LIVE INDONESIA")
print("[3]COMING SOON")
print("[0]EXIT")
print("")
print("")
pilih = input("Choice Mode:")

if pilih == '1':
    os.system("clear")
    print("\tGLOBAL ( Dunia )")
    print('============ LIVE  =============')
    print("Jumlah Negara :", negara)
    print("Terkonfirmasi :", terkonfirmasi)
    print("Meninggal :", meninggal_global)
    print(keterangan_global)
    stuck = input("")

elif pilih == '2':
    os.system("clear")
    print('\tINDONESIA')
    print('============ LIVE =============')
    print('Positif :', positif_indo)
    print('Sembuh :', sembuh_indo)
    print('Meninggal :', meninggal_indo)
    print(keterangan_indo)
    tekan = input("")
    
elif pilih == '3':
	print("COMING SOON")
	
elif pilih == '0':
	exit()
	
else:
	os.system("clear")
	print("TYPO NOOB")
	stuck2 = input("")