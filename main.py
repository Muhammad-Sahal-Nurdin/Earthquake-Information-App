"""
Aplikasi Informasi Gempa Terkini
MODULARISASI DENGAN FUNCTION
"""
from gempa_terkini import ekstraksi_data, tampilkan_data

if  __name__ == '__main__':
    print('Aplikasi Utama')
    result = ekstraksi_data()
    tampilkan_data(result)