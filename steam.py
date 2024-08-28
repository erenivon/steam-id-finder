import requests
from bs4 import BeautifulSoup

def check_steam_id(number):
    url = f"https://steamcommunity.com/id/{number}/"
    response = requests.get(url)
    
    # Sayfanın başlığını ve içeriğini kontrol et
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string if soup.title else ""
    
    # HTML içeriğinden spesifik bir hata mesajını kontrol et
    error_message = soup.find(string="The specified profile could not be found.")

    # Başlık ve içerik mesajı kontrolü
    if "Steam Topluluğu :: Hata" in title or error_message:
        return True  # Kullanılmıyor
    else:
        return False  # Kullanılıyor

def find_unused_steam_id(start=1, end=99999):
    with open("C:/Users/pc_user/Desktop/filename.txt", "w") as file: # TXT Dosya yolunu girin
        for number in range(start, end + 1):
            formatted_number = f"{number:04d}"  # Sayıyı dört basamaklı string olarak formatla
            # print(f"Kontrol ediliyor: {formatted_number}")  # Denenen sayıyı göster
            if check_steam_id(formatted_number):
                print(f"Kullanılmayan ID bulundu: {formatted_number}")
                file.write(formatted_number + "\n")
        print("Verilen aralıkta kullanılmayan bir ID bulunamadı.")
        return None

# Kullanılmayan bir ID bulmaya çalış
find_unused_steam_id(1, 99999)
