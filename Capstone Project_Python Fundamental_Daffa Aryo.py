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

#menu utama
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
                cari_barang = input('Masukan id barang yang ingin dicari:') #masih salah
                barang_ditemukan = False
                for barang in barang_toserba:
                    if cari_barang == barang['id']:
                        print('barang ditemukan!')
                        print("id\t| Nama\t\t\t\t| Stock\t\t| Harga\t\t| Total Penjualan")
                        print('{}\t| {}\t\t\t| {}\t\t| {}\t\t| {}'.format(barang['id'],barang['nama'],barang['stock'],barang['harga'],barang['total penjualan']))
                        barang_ditemukan = True
                        continue
                if not barang_ditemukan:
                    print(f'Barang dengan id {cari_barang} tidak ditemukan!')
                    continue

            elif pilihan_menu_1 == '3':
                break
            else:
                print('\nInput tidak valid!')
                continue
            
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

                barang_sudah_ada = False
                for barang in barang_toserba:
                    if id_barang == barang['id'] or nama_barang.capitalize() == barang['nama']:
                        print('Barang sudah ada di toko!')
                        barang_sudah_ada = True
                        continue
                
                if not barang_sudah_ada:
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
        #menu update data
        elif pilih_menu == '3':
            pilihan_menu_3 = input('''
                \t Menu Update Barang "TOSERBA PASTI ADA"
                1. Update Data Barang
                2. Kembali ke Menu Utama
                
                Masukan angka Menu Update Barang:
                ''')
            if pilihan_menu_3 == '1':
                print('\t\t\t\t List Barang "TOSERBA PASTI ADA"\n')
                print("id\t| Nama\t\t\t\t| Stock\t\t| Harga\t\t| Total Penjualan")
                for barang in barang_toserba:
                    print('{}\t| {}\t\t\t| {}\t\t| {}\t\t| {}'.format(barang['id'],barang['nama'],barang['stock'],barang['harga'],barang['total penjualan']))
                
                pilih_barang_update = input('Masukan id barang yang ingin di Update: ')
                barang_ada = False
                for barang in barang_toserba:
                    if pilih_barang_update == barang['id']:
                        print("id\t| Nama\t\t\t\t| Stock\t\t| Harga\t\t| Total Penjualan")
                        print('{}\t| {}\t\t\t| {}\t\t| {}\t\t| {}'.format(barang['id'],barang['nama'],barang['stock'],barang['harga'],barang['total penjualan']))
                        copy_barang = barang.copy()
                        barang_ada = True

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

                if not barang_ada:
                    print(f'Barang dengan id {pilih_barang_update} tidak ditemukan.')
                    continue
            
            elif pilihan_menu_3 == '2':
                break
            else:
                print('\nInput tidak valid!')
                continue

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
                 
        elif pilih_menu == '5':
            pilihan_menu_5 = input('''
                \t Menu Belanja "TOSERBA PASTI ADA"
                1. Belanja Barang
                2. Kembali ke Menu Utama
                
                Masukan angka Menu Update Barang:
                ''')
            if pilihan_menu_5 == '1':
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
                        keranjang.clear()  # Bersihkan keranjang setelah transaksi selesai
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
                        keranjang.clear()  # Bersihkan keranjang setelah transaksi selesai
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

        elif pilih_menu == '6':
            print('Terima Kasih, sampai jumpa lagi! :D')
            running = False
            break

        else:
            print('\nInput tidak valid')
            break
