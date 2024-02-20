# Capstone-Module-1-Python-Fundamental-Daffa-Aryo-Utomo-Sudranto-

Berikut adalah deskripsi umum mengenai program yang telah dibuat beserta penjelasan mengenai fungsi dari program tersebut:

## TOSERBA PASTI ADA

### Deskripsi Program:
Program ini adalah aplikasi toko sederhana yang memungkinkan pengguna untuk mengelola daftar barang, termasuk menampilkan, menambah, memperbarui, dan menghapus barang, serta melakukan transaksi belanja.

### Fungsi dari Program:
1. **Daftar Barang:**
    - Menampilkan semua barang yang tersedia di toko.
    - Mencari barang berdasarkan ID barang.
2. **Menambah Barang:**
    - Memungkinkan pengguna untuk menambahkan barang baru ke dalam daftar toko.
3. **Update Barang:**
    - Mengizinkan pengguna untuk memperbarui data barang yang sudah ada.
4. **Menghapus Barang:**
    - Memungkinkan pengguna untuk menghapus barang dari daftar toko.
5. **Belanja Barang:**
    - Mengizinkan pengguna untuk memilih barang yang ingin dibeli dan melakukan transaksi pembayaran.

### Fitur dari Program:
- **Interaktif:** Program menyediakan antarmuka yang interaktif yang memungkinkan pengguna untuk dengan mudah berinteraksi dengan aplikasi melalui terminal.
- **Manajemen Barang yang Fleksibel:** Pengguna dapat dengan mudah menambahkan, memperbarui, dan menghapus barang dari toko.
- **Transaksi Belanja yang Mudah:** Program memungkinkan pengguna untuk melakukan transaksi belanja dengan cepat dan efisien, termasuk perhitungan total harga dan kembalian.

### Penjelasan Blok Kode:
1. **Variabel `barang_toserba` dan `keranjang`:**

           barang_toserba = [
             {  'id' : 'atk01', 
                'nama' : 'Pulpen Hitam',
                'stock' : 25,
                'harga' : 7000,
                'total penjualan' : 200
            },
            {
                'id' : 'atk02',
                'nama' : 'Pensil 2B',
                'stock' : 18,
                'harga' : 4000,
                'total penjualan' : 92
            },
            {
                'id' : 'atk03',
                'nama' : 'Buku Tulis',
                'stock' : 30,
                'harga' : 10000,
                'total penjualan' : 131
            },
            {   'id' : 'snk01', 
                'nama' : 'Keripik',
                'stock' : 100,
                'harga' : 11000,
                'total penjualan' : 88
            },
            {
                'id' : 'snk02',
                'nama' : 'Biskuit',
                'stock' : 88,
                'harga' : 8000,
                'total penjualan' : 123
            },
            {
                'id' : 'snk03',
                'nama' : 'Susu Vanilla',
                'stock' : 53,
                'harga' : 17000,
                'total penjualan' : 222
            },
            ]
        
        
        keranjang = []

   
    - Variabel `barang_toserba` merupakan list dictionary untuk menyimpan daftar barang yang tersedia di toko dengan rincian seperti ID, nama, stok, harga, dan total penjualan.
    - Variabel `keranjang` digunakan untuk menyimpan barang yang dipilih oleh pengguna saat berbelanja.
    
2. **Menu Utama:**
   
       #Menu Utama
       running = True
       while running :
            pilih_menu = input('''
                \t Selamat Datang di 
                \t "TOSERBA PASTI ADA"
                Menu Utama:
                1. Daftar Barang
                2. Menambah Barang
                3. Update Barang 
                4. Menghapus Barang
                5. Belanja Barang
                6. Exit Program
                Masukkan angka Menu Utama : ''')
   


    - Menu utama aplikasi yang menampilkan pilihan fitur dari program.
    - varible `running` sebagai nilai boolean True
    - `while` loop digunakan untuk menjaga program tetap berjalan dan kembali ke menu utama hingga pengguna memilih untuk menghentikan program.
    - `pilih_menu` digunakan untuk melakukan input user yang berfungsi untuk memilih angka fitur yang terdapat pada menu utama.

3. **Menu Read Data:**

        #menu read data
        while True:
            if pilih_menu == '1':
                pilihan_menu_1 = input('''
                \t Menu Daftar Barang "TOSERBA PASTI ADA"
                1. Tampilkan Semua Barang
                2. Mencari Barang
                3. Kembali ke Menu Utama    
            Masukan angka Menu Barang:
                ''')
            if pilihan_menu_1 == '1':
                if not barang_toserba:
                    print('Tidak ada barang di Toko!')
                    break
                else:
                    print('\t\t\t\t List Barang "TOSERBA PASTI ADA"\n')
                    print("id\t| Nama\t\t\t\t| Stock\t\t| Harga\t\t| Total Penjualan")
                    for barang in barang_toserba:
                        print('{}\t| {}\t\t\t| {}\t\t| {}\t\t| {}'.format(barang['id'],barang['nama'],barang['stock'],barang['harga'],barang['total penjualan']))
                
            elif pilihan_menu_1 == '2':
                cari_barang = input('Masukan id barang yang ingin dicari:')
                barang_ada1 = False
                for barang in barang_toserba:
                    if cari_barang == barang['id']:
                        print('barang ditemukan!')
                        print("id\t| Nama\t\t\t\t| Stock\t\t| Harga\t\t| Total Penjualan")
                        print('{}\t| {}\t\t\t| {}\t\t| {}\t\t| {}'.format(barang['id'],barang['nama'],barang['stock'],barang['harga'],barang['total penjualan']))
                        barang_ada1 = True
                        continue
                if not barang_ada1:
                    print(f'Barang dengan id {cari_barang} tidak ditemukan!')
                    continue

            elif pilihan_menu_1 == '3':
                break
            else:
                print('\nInput tidak valid!')
                continue

   - Didalam `while` loop menu utama, terdapat juga `while` loop untuk setiap conditional statement `if` ketika user memilih angka dari fitur yang terdapat di menu utama. Loop tersebut berfungsi untuk kembali ke menu fitur yang dipilih sehingga tidak kembali ke menu utama.
   - `pilih_menu_1` adalah user input yang diisi dengan angka dari menu fitur read data.
   - `if not barang_toserba` merupakan conditional statement untuk memeriksa apakah ada data list dictionary di `barang_toserba`, jika data kosong maka conditional statement ini akan di proses program.
   - `for barang in barang_toserba` looping yang berfungsi untuk melakukan print seluruh data yang ada di list dictionary `barang_toserba`, jika seluruh data sudah diperiksa, maka looping akan berhenti.
   - `if cari_barang == barang['id']:` conditional statement untuk mencari barang berdasarkan `id` barang pada `barang_toserba` dimana `cari_barang` merupakan input str untuk diisi `id` barang.
   - `barang_ada1 = False` merupakan variable dengan value boolean untuk memeriksa apakah barang yang dicari terdapat pada `barang_toserba`. Jika barang terdapat pada list dictionary, maka nilainya akan menjadi `True`
   - `if not barang_ada1` adalah conditional statement yang di proses ketika `id` barang yang dicari tidak dapat ditemukan.
   - Tiap menu fitur memiliki pilihan untuk kembali ke menu utama dengan melakukan `break` pada menu fitur yang sedang berjalan sehingga dapat kembali ke menu utama.
   - Jika input angka di menu fitur tidak sesuai, hasil dari input tersebut adalah tetap berada di menu fitur karena terdapat `continue` ketika conditional statement tidak terpenuhi.
     
4.  **Menu Create Data:**

         #menu create data2
            elif pilih_menu == '2':
            pilihan_menu_2 = input('''
                \t Menu Menambahkan Barang "TOSERBA PASTI ADA"\n
                1. Menambahkan barang
                2. Kembali ke Menu Utama
                
                Masukan angka Menu Menambahkan Barang:
                ''')
            if pilihan_menu_2 == '1':
                print('Menambahkan barang di "TOSERBA PASTI ADA"')
                print('Rules: Huruf depan harus menggunakan capital!')
                id_barang = input('Masukan id barang yang ditambahkan: ')
                nama_barang = input('Masukan nama barang yang ditambahkan: ')

                barang_ada2 = False
                for barang in barang_toserba:
                    if id_barang == barang['id'] or nama_barang.capitalize() == barang['nama']:
                        print('Barang sudah ada di toko!')
                        barang_ada2 = True
                        continue
                
                if not barang_ada2:
                    stock_barang = int(input('Masukan stock barang yang ditambahkan: '))
                    harga_barang = int(input('Masukan harga barang yang ditambahkan: '))
                    total_penjualan_barang = int(input('Masukan total penjualan barang yang ditambahkan: '))
                    barang_toserba.append({
                            'id' : id_barang,
                            'nama' : nama_barang,
                            'stock' : stock_barang,
                            'harga' : harga_barang,
                            'total penjualan' : total_penjualan_barang
                            })
                    menyimpan_barang = input('Apakah ingin menyimpan barang? (yes/no)')
                    if menyimpan_barang == 'yes':
                        print('Barang berhasil disimpan!')
                        print('\t\t\t\t List Barang "TOSERBA PASTI ADA"\n')
                        print("id\t| Nama\t\t\t\t| Stock\t\t| Harga\t\t| Total Penjualan")
                        for barang in barang_toserba:
                            print('{}\t| {}\t\t\t| {}\t\t| {}\t\t| {}'.format(barang['id'],barang['nama'],barang['stock'],barang['harga'],barang['total penjualan']))
                    
                    elif menyimpan_barang == 'no':
                        barang_toserba.pop()
                        print('Barang tidak disimpan!')
                    else:
                        barang_toserba.pop()
                        print('Barang tidak disimpan!')

            elif pilihan_menu_2 == '2':
                break
            else:
                print('\nInput tidak valid!')
                continue
    - Dalam melalukan penambahan barang, terdapat pemeriksaan di input `id_barang` dan `nama_barang` menggunakan conditional statement `if id_barang == barang['id'] or nama_barang.capitalize() == barang['nama']:`. Code tersebut digunakan untuk memerikasa apakah `id` dan `nama` barang yang baru di input sudah terdapat di `barang_toserba`. Jika input `id` dan `nama` sudah ada di `barang_toserba`, maka penambahan barang tidak dapat dilanjutkan.
    - Jika data `id` dan `nama` barang belum tersedia di `barang_toserba`, maka dapat melanjutkan untuk melakukan penambahan data barang baru lain nya yang mencakup `stcok`, `harga` , dan `total penjualan`.
    - Penambahan data baru akan di proses menggunakan method `barang_toserba.append`. Dengan method tersebut, maka input data barang baru dapat ditambahkan ke list dictionary `barang_toserba` di bagian paling bawah.
    - Setelah memasukan input, akan dilanjutkan dengan input konfirmasi untuk menyimpan data baru atau tidak.
    - Jika konfirmasi disetujui, maka program akan melakukan print untuk menampilkan semua data `barang_toserba` dan data input barang baru.
    - Jika konfirmasi tidak disetujui, maka data input yang sudah masuk ke `barang_toserba` dapat dihapus menggunakan method `barang_toserba.pop()` untuk menghapus data baru yang paling bawah pada list dictionary.
    - Program juga tidak akan menyimpan data baru jika input konfirmasi tidak menggunakan input yang sesuai dari keterangan yang ada (input selain yes dan no).

5.  **Menu Update Data:**

        #menu update data
        elif pilih_menu == '3':
            pilihan_menu_3 = input('''
                \t Menu Update Barang "TOSERBA PASTI ADA"
                1. Update Data Barang
                2. Kembali ke Menu Utama
                
                Masukan angka Menu Update Barang:
                ''')
            if pilihan_menu_3 == '1':
                if not barang_toserba:
                    print('Tidak ada barang di Toko!')
                    break
    
                print('\t\t\t\t List Barang "TOSERBA PASTI ADA"\n')
                print("id\t| Nama\t\t\t\t| Stock\t\t| Harga\t\t| Total Penjualan")
                for barang in barang_toserba:
                    print('{}\t| {}\t\t\t| {}\t\t| {}\t\t| {}'.format(barang['id'],barang['nama'],barang['stock'],barang['harga'],barang['total penjualan']))
                
                pilih_barang_update = input('Masukan id barang yang ingin di Update: ')
                barang_ada3 = False
                for barang in barang_toserba:
                    if pilih_barang_update == barang['id']:
                        print("id\t| Nama\t\t\t\t| Stock\t\t| Harga\t\t| Total Penjualan")
                        print('{}\t| {}\t\t\t| {}\t\t| {}\t\t| {}'.format(barang['id'],barang['nama'],barang['stock'],barang['harga'],barang['total penjualan']))
                        copy_barang = barang.copy()
                        barang_ada3 = True

                        confirm_update = input('Apakah ingin melakukan update? (yes/no)')
                        if confirm_update == 'yes':
                            pilih_update = input('''
                                \t Menu Update Barang
                                1. Update Data nama Barang
                                2. Update Data stock Barang
                                3. Update Data harga Barang
                                4. Update Data total penjualan Barang
                                
                                Masukan angka Menu Update Barang:
                                ''')
                            if pilih_update == '1':
                                update_nama = input('Masukan nama barang baru: ')
                                barang['nama'] = update_nama
                            elif pilih_update == '2':
                                update_stock = int(input('Masukan stock barang baru: '))
                                barang['stock'] = update_stock                           
                            elif pilih_update == '3':
                                update_harga = int(input('Masukan harga barang baru: '))
                                barang['harga'] = update_harga
                            elif pilih_update == '4':
                                update_total_penjualan = int(input('Masukan total penjualan barang baru: '))
                                barang['total penjualan'] = update_total_penjualan
                            else:
                                print('\n Input tidak valid!')

                            menyimpan_update = input('Apakah ingin menyimpan update? (yes/no)')
                            if menyimpan_update == 'no': #masih salah
                                barang = copy_barang
                                for item in barang_toserba:
                                    if item['id'] == barang['id']:
                                        item['nama'] = barang['nama']
                                        item['stock'] = barang['stock']
                                        item['harga'] = barang['harga']
                                        item['total penjualan'] = barang['total penjualan']
                                print('Update dibatalkan!')

                            elif menyimpan_update == 'yes':
                                print('\t\t\t\t List Barang "TOSERBA PASTI ADA"\n')
                                print("id\t| Nama\t\t\t\t| Stock\t\t| Harga\t\t| Total Penjualan")
                                for barang in barang_toserba:
                                    print('{}\t| {}\t\t\t| {}\t\t| {}\t\t| {}'.format(barang['id'],barang['nama'],barang['stock'],barang['harga'],barang['total penjualan']))
                                print('Update berhasil disimpan!')

                            else:
                                barang = copy_barang
                                for item in barang_toserba:
                                    if item['id'] == barang['id']:
                                        item['nama'] = barang['nama']
                                        item['stock'] = barang['stock']
                                        item['harga'] = barang['harga']
                                        item['total penjualan'] = barang['total penjualan']
                                print('Update dibatalkan!')       

                        elif confirm_update == 'no':
                            print('Update dibatalkan!')
                            continue   
                        else:
                            print('Update dibatalkan!')

                if not barang_ada3:
                    print(f'Barang dengan id {pilih_barang_update} tidak ditemukan.')
                    continue
            
            elif pilihan_menu_3 == '2':
                break
            else:
                print('\nInput tidak valid!')
                continue
    - Data yang ingin di update, perlu diperiksa keberadaan datanya menggunakan variable boolean `barang_ada3`.
    - Barang yang ingin diupdate dicari dengan melakukan input data `id` barang yang terdapat di `barang_toserba`.
    - variable `copy_barang = barang.copy()` berfungsi untuk menyimpan salinan dari data `barang` yang telah dipilih user.
    - Setelah memilih barang, user dapat memilih salah satu data yang akan di update. Data yang dapat dipilih dianataranya nama, stock, harga, dan total penjualan.
    - Perubahan data akan terinput ke `barang_toserba`.
    - Setelah melakukan perubahan data, user akan dimunculkan pesan konfirmasi untuk melakukan perubahan data atau tidak.
    - Jika user melakukan input 'no' atau dengan input lainnya, maka data tidak tersimpan.
    - Data yang sebelumnya sudah tersimpan, akan diubah kembali dengan data sebelum user melakukan input perubahan data dengan varible `copy_barang`. Data `copy_barang` akan mengubah data `barang` yang sudah di input dengan looping `for item in barang_toserba:` dengan conditional statement `if item['id'] == barang['id']:` dimana varible `item` dapat mengubah data pada `barang_toserba` yang sudah di update sehingga program tidak melakukan update data.
    - Jika user melakukan input 'yes', update data berhasil dilakukan pada `barang_toserba`.

7.  **Menu Delete Data:**

           elif (pilih_menu == '4'):
                pilihan_menu_4 = input('''
                \t Menu Hapus Barang "TOSERBA PASTI ADA"
                1. Menghapus Barang
                2. Menghapus seluruh barang Toko
                3. Kembali ke Menu Utama
                
                Masukan angka Menu Hapus Barang:
                ''')
            
            if pilihan_menu_4 == '1':
                print('\t\t\t\t List Barang "TOSERBA PASTI ADA"\n')
                print("id\t| Nama\t\t\t\t| Stock\t\t| Harga\t\t| Total Penjualan")
                for barang in barang_toserba:
                    print('{}\t| {}\t\t\t| {}\t\t| {}\t\t| {}'.format(barang['id'],barang['nama'],barang['stock'],barang['harga'],barang['total penjualan']))

                pilih_barang_delete = input('Masukan id barang yang ingin dihapus: ')
                barang_ada4 = False
                for barang in barang_toserba:
                    if pilih_barang_delete == barang['id']:
                        print('barang yang ingin dihapus')
                        print("id\t| Nama\t\t\t\t| Stock\t\t| Harga\t\t| Total Penjualan")
                        print('{}\t| {}\t\t\t| {}\t\t| {}\t\t| {}'.format(barang['id'],barang['nama'],barang['stock'],barang['harga'],barang['total penjualan']))
                        barang_ada4 = True
                        
                        confirm_delete = input('Apakah ingin menghapus barang ini dari toko? (yes/no)')
                        if confirm_delete == 'yes':
                            barang_toserba.remove(barang)
                            print('Barang telah di hapus dari toko!')
                        elif confirm_delete == 'no':
                            print('Barang tidak di hapus dari toko!')
                        else:
                            print('Barang tidak di hapus dari toko!')     
                
                if not barang_ada4:
                    print(f'Barang dengan id {pilih_barang_delete} tidak ditemukan!')

            elif pilihan_menu_4 == '2':
                clear_toko = input('Apakah anda yakin untuk menghapus seluruh data di Toko? (yes/no)')
                if clear_toko == 'yes':
                    print('Seluruh barang di toko berhasil di hapus!')
                    barang_toserba.clear()
                else:
                    print('Barang tidak di hapus dari Toko!')
                    continue
            
            elif pilihan_menu_4 == '3':
                break
            else:
                print('\nInput tidak valid!')
                continue

    - Delete barang pada `barang_toserba` dilakukan dengan memilih `id` barang.
    - Setelah memilih `barang` yang ingin dihapus, akan muncul pesan konfirmasi untuk melakukan delete data.
    - Jika user melakukan input 'yes', maka data `barang` pada `barang_toserba` akan dihapus. Delete data dilakukan dengan method `barang_toserba.remove(barang)`, dimana method ini dapat menghapus `barang` yang telah di input user dari `barang_toserba`.
    -  Jika user melakukan input 'no' atau input lainnya, maka program tidak akan melakukan delete.
    -  Selain menghapus `barang` dari `barang_toserba`, terdapat pilihan untuk menghapus seluruh data pada `barang_toserba` dengan menggunakan `barang_toserba.clear()`.
    -  Jika `barang_toserba` tidak memiliki data, maka fitur read data, update data, dan belanja barang tidak dapat digunakan. Create data dapat dilakukan untuk memasukan data baru pada `barang_toserba`
      
8.  **Menu Belanja Barang:**

             elif pilih_menu == '5':
                pilihan_menu_5 = input('''
                \t Menu Belanja "TOSERBA PASTI ADA"
                1. Belanja Barang
                2. Kembali ke Menu Utama
                
                Masukan angka Menu Update Barang:
                ''')
            if pilihan_menu_5 == '1':
                if not barang_toserba:
                    print('Tidak ada barang di Toko!')
                    break
    
                print('\t\t\t\t List Barang "TOSERBA PASTI ADA"\n')
                print("id\t| Nama\t\t\t\t| Stock\t\t| Harga\t\t| Total Penjualan")
                for barang in barang_toserba:
                    print('{}\t| {}\t\t\t| {}\t\t| {}\t\t| {}'.format(barang['id'],barang['nama'],barang['stock'],barang['harga'],barang['total penjualan']))
                
                while True:
                    pilih_id_barang = input('Masukan id barang yang ingin dibeli: ')
                    jumlah_barang = int(input('Masukan jumlah barang yang dipilih: '))
                    
                    barang_ditemukan = False
                    for barang in barang_toserba:
                        if pilih_id_barang == barang['id']:
                            if jumlah_barang > barang['stock']:
                                print('Jumlah pembelian melebihi stock barang! Stock yang tersedia: {}'.format(barang['stock']))
                            else:
                                keranjang.append({
                                    'nama': barang['nama'],
                                    'jumlah': jumlah_barang,
                                    'harga': barang['harga']
                                })
                                print('Barang telah ditambahkan ke keranjang!')
                                barang_ditemukan = True
                            break
                    
                    if not barang_ditemukan:
                        print(f'Barang dengan id {pilih_id_barang} tidak ditemukan.')
                        break

                    checker = input('Ingin membeli barang lain? (yes/no): ')
                    if checker == 'no':
                        break
                        
                print('\n\t\t\tList Belanja\n')
                print("Nama\t\t\t\t| Jumlah\t| Harga\t\t\t| Total Harga")
                total_harga = 0
                for barang in keranjang:
                    print('{}\t\t\t\t| {}\t\t| {}\t\t\t| {}'.format(barang['nama'], barang['jumlah'], barang['harga'], barang['harga'] * barang['jumlah']))
                    total_harga += barang['jumlah'] * barang['harga']

                while True:
                    print('Total pembayaran: {}'.format(total_harga))
                    jumlah_uang = int(input('Masukkan jumlah uang: '))
                    if jumlah_uang == total_harga:
                        print('Terima kasih!')
                        for barang in keranjang:
                            for item in barang_toserba:
                                if item['nama'] == barang['nama']:
                                    item['stock'] -= barang['jumlah']
                                    item['total penjualan'] += barang['jumlah']
                        keranjang.clear() 
                        break

                    elif jumlah_uang > total_harga:
                        kembalian = jumlah_uang - total_harga
                        print('Terima kasih! Uang kembali: {}'.format(kembalian))

                        # Mengurangi stok dan menambah total penjualan untuk setiap barang yang dibeli
                        for barang in keranjang:
                            for item in barang_toserba:
                                if item['nama'] == barang['nama']:
                                    item['stock'] -= barang['jumlah']
                                    item['total penjualan'] += barang['jumlah']
                        keranjang.clear() 
                        break
                    
                    elif jumlah_uang < total_harga:
                        uang_kurang = total_harga - jumlah_uang
                        print('Uang kurang sebesar {}'.format(uang_kurang))
                        konfirmasi_ulang = input('Apakah tetap ingin melakukan pembayaran?(yes/no): ')
                        if konfirmasi_ulang == 'yes':
                            continue
                        else:
                            print('Belanja dibatalkan')
                            keranjang.clear()
                            break
                    else:
                        print('Belanja dibatalkan')
                        keranjang.clear()
                        break


            elif pilihan_menu_5 == '2':
                break
            else:
                print('\nInput tidak valid!')
                continue
    - Pada fitur belanja barang, `while` loop digunakan untuk melakukan input `pilih_id_barang` dan `jumlah_barang` secara terus menerus hingga user selesai memilih barang untuk dibeli 

10. **Exit Program:**

        elif pilih_menu == '6':
            print('Terima Kasih, sampai jumpa lagi! :D')
            running = False
            break

        else:
            print('\nInput tidak valid')
            break

Dengan demikian, program ini cocok untuk digunakan oleh pengguna yang ingin mempelajari konsep dasar pemrograman Python serta manajemen data sederhana.
Terima Kasih.
