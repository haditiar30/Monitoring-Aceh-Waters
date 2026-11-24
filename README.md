# Monitoring Aceh Waters — pembaca daftar EN4

Program Python ini mengambil dan menampilkan isi daftar unduhan EN4 dari Met Office:

`https://www.metoffice.gov.uk/hadobs/en4/EN.4.2.2.analyses.g10.download-list.txt`

## Persyaratan

Python 3.9 atau yang lebih baru. Tidak memerlukan paket tambahan.

## Menjalankan

```bash
python read_en4_download_list.py
```

Untuk menyimpan salinan daftar ke file lokal sekaligus menampilkannya:

```bash
python read_en4_download_list.py --save download-list.txt
```

Program memerlukan koneksi internet. Jika server tidak dapat diakses, pesan kesalahan akan ditampilkan.
