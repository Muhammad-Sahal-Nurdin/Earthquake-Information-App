import requests
from bs4 import BeautifulSoup


def ekstraksi_data():
    """
    Tanggal: 09 Maret 2022
    Waktu: 08:49:18 WIB
    Magnitudo: 5.2
    Kedalaman: 14 km
    Lokasi: LU= 2.57 BT=128.43
    Pusat Gempa: Pusat gempa berada di Laut 60 km TimurLaut Daruba
    Dirasakan: Dirasakan (Skala MMI): II-III Morotai
    :return:
    """
    try:
        content = requests.get('https://www.bmkg.go.id')
    except Exception:
        return None
    if content.status_code == 200:
        print(content.text)
        # soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
        # print(soup.prettify())
        hasil = dict()
        hasil['tanggal'] = '09 Maret 2022'
        hasil['waktu'] = '08:49:18 WIB'
        hasil['magnitudo'] = 5.2
        hasil['kedalaman'] = '14 km'
        hasil['lokasi'] = {'ls': 2.57, 'bt': 128.43}
        hasil['pusat gempa'] = 'Pusat gempa berada di Laut 60 km TimurLaut Daruba'
        hasil['dirasakan'] = 'Dirasakan (Skala MMI): II-III Morotai'

        return hasil
    else:
        return None

def tampilkan_data(result):
    if result is None:
        print('Tidak dapat menampilkan data terkini.')
        return
    print('Informasi Gempa Berdasarkan BMKG')
    print(f"Tanggal: {result['tanggal']}")
    print(f"Waktu: {result['waktu']}")
    print(f"Magnitudo: {result['magnitudo']}")
    print(f"Kedalaman: {result['kedalaman']}")
    print(f"Lokasi: LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Pusat Gempa: {result['pusat gempa']}")
    print(f"Dirasakan: {result['dirasakan']}")

# if  __name__ == '__main__':
#     print('Ini adalah package gempa terkini')