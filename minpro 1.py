order0 = ["Hakim", "Jl. Suryanata", "081347055827", "Rumah", "Menyapu halaman","sedang dalam antrian"]
order1 = ["Alip", "Jl. Pattimura", "081335396774", "Kantor", "Membersihkan toilet", "sedang dalam antrian"]
order2 = ["Alya", "Jl. Pramuka", "081333637409", "Sekolah", "Sedot WC", "pesanan dibatalkan"]
order3 = ["Rasya", "Jl. Teuku Umar", "081347120196", "Kantor", "Membersihkan ruang kerja", "pesanan diterima"]
order4 = ["Anggita", "Jl. Malioboro", "085248335528", "Rumah", "Mencuci piring ", "pesanan diterima"]
order5 = ["Vidya", "Jl. Jakarta", "081347110004", "Sekolah", "Pengangkutan sampah", "pesanan dibatalkan"]

orderan = [order0, order1, order2, order3, order4, order5] #list orderan

status0 = ["sedang dalam antrian"]
status1 = ["pesanan dibatalkan"]
status2 = ["pesanan diterima"]

status= [status0, status1, status2] #list status

Layanan0 = ["Membersihkan halaman"]
Layanan1 = ["Membersihkan dan menyedot WC"]
Layanan2 = ["Memotong rumput"]

layanan = [Layanan0, Layanan1, Layanan2 ] #jenis layanan

Lingkungan0 = ["Rumah"]
Lingkungan1 = ["Sekolah"]
Lingkungan2 = ["Kantor"]

lingkungan = [Lingkungan0, Lingkungan1, Lingkungan2] # kategori lingkungan

print("Selamat Datang di Pelayanan Kebersihan")
print()
#layanan yang tersedia
print("===PELAYANAN KEBERSIHAN===")
print("1. Pesan pelayanan")
print("2. Lihat pesanan pelayanan")
print("3. Ubah status pesanan pelayanan")
print("4. Hapus pesanan pelayanan")
print("5. Keluar")

print()

Pilihan = input("Pilih menu(1-5): ")

if Pilihan == "1":
    print()
    print("++ Silahkan memilih layanan ++")
    print("\n1.", lingkungan[0], "\n2.", lingkungan[1], "\n3.", lingkungan[2])
    x = int(input("\nSilahkan pilih kategori lingkungan: "))
    print()

    #layanan rumah
    if x == 1:
        print("==Linngkunga Rumah==")
        print("\n1.", layanan[0], "\n2.", layanan[1], "\n3.", layanan[2] )
        print("-" * 40)
        m = int(input("Pilih layanan yang diinginkan: "))
        print("-" * 40)
        if m == 1:
            print("\nMasukkan biodata diri anda")
            nama    = input("Masukkan nama  :")
            alamat  = input("Masukkan alamat: ")
            no_telpon = input("Masukkan No.Telpon: ")
            print(f"\n{nama} {alamat} {no_telpon}", status[0])
        elif m == 2:
            print("\nlayanan diproses")
            nama    = input("Masukkan nama  :")
            alamat  = input("Masukkan alamat: ")
            no_telpon = input("Masukkan No.Telpon: ")
            print(f"\n{nama} {alamat} {no_telpon} ", status[0])
        elif m == 3:
            print("\nlayanan diproses")
            nama    = input("Masukkan nama  :")
            alamat  = input("Masukkan alamat: ")
            no_telpon = input("Masukkan No.Telpon: ")
            print(f"\n{nama} {alamat} {no_telpon}", status[0])
        else:
            d = (input("salah masukkin indeks broo......"))

    #Layanan Sekolah
    elif x == 2:
        print("==Lingkungan Sekolah==")
        print("\n1.", layanan[0], "\n2.", layanan[1], "\n3.", layanan[2] )
        print("-" * 40)
        l = int(input("Pilih layanan yang diinginkan: "))
        print("-" * 40)
        if l == 1:
            print("\nlayanan diproses")
            nama    = input("Masukkan nama  :")
            alamat  = input("Masukkan alamat: ")
            no_telpon = input("Masukkan No.Telpon: ")
            print(f"\n{nama} {alamat} {no_telpon}", status[0])
        elif l == 2:
            print("\nlayanan diproses")
            nama    = input("Masukkan nama  :")
            alamat  = input("Masukkan alamat: ")
            no_telpon = input("Masukkan No.Telpon: ")
            print(f"\n{nama} {alamat} {no_telpon}", status[0])
        elif l == 3:
            print("\nlayanan diproses")
            nama    = input("Masukkan nama  :")
            alamat  = input("Masukkan alamat: ")
            no_telpon = input("Masukkan No.Telpon: ")
            print(f"\n{nama} {alamat} {no_telpon}", status[0])
        else:
            c = (input("salah masukkin indeks broo...... "))

    #Layanan Kantor
    elif x == 3:
        print("==Lingkungan Kantor==")
        print("\n1.", layanan[0], "\n2.", layanan[1], "\n3.", layanan[2] )
        print("-" * 40)
        n = int(input("Pilih layanan yang diinginkan: "))
        print("-" * 40)
        if n == 1:
            print("\nlayanan diproses")
            nama    = input("Masukkan nama  :")
            alamat  = input("Masukkan alamat: ")
            no_telpon = input("Masukkan No.Telpon: ")
            print(f"\n{nama} - {alamat} - {no_telpon}" , status[0])
        elif n == 2:
            print("\nlayanan diproses")
            nama    = input("Masukkan nama  :")
            alamat  = input("Masukkan alamat: ")
            no_telpon = input("Masukkan No.Telpon: ")
            print(f"\n{nama} {alamat} {no_telpon}", status[0])
        elif n == 3:
            print("\nlayanan diproses")
            nama    = input("Masukkan nama  :")
            alamat  = input("Masukkan alamat: ")
            no_telpon = input("Masukkan No.Telpon: ")
            print(f"\n{nama} {alamat} {no_telpon}", status[0])
        else:
            c = (input("salah masukkin indeks broo......"))

elif Pilihan == "2":
    if len(orderan) == 0:
        print("\nBelum ada orderan ;0")
    else:
        print("Berikut orderan yang anda pesan: " )
        print("\n1.", orderan[0],"\n2.",orderan[1], "\n3.",orderan[2], "\n4.",orderan[3], "\n5.",orderan[4], "\n6.", orderan[5])

elif Pilihan == "3":
    if len(orderan) == 0:
        print("Belum ada orderan ;0")
    else:
        print("Berikut orderan yang anda pesan: " )
        print("\n1.", orderan[0],"\n2.",orderan[1], "\n3.",orderan[2], "\n4.",orderan[3], "\n5.",orderan[4], "\n6.", orderan[5])
        ubah = int(input("\nSebutkan ID yang ingin diubah: "))
        if 0 <= ubah <= 5:
            print("\nUpdate status menjadi: \n0 = sedang dalam antrian, \n1 = pesanan dibatalkan, \n2 = pesanan diterima")
            statusbaru = int(input("\nMasukkan status: "))
            if 0 <= statusbaru <=2 :
                orderan[ubah][5] = status[statusbaru]
                print("\n", orderan[ubah] )
                print("data berhasil diubah")
            else:
                print("Pilihan tidak valid")
        else:
            print("Pilihan kamu tidak valiiidd!!!!!")
        
        
            
    

elif Pilihan == "4":
    print("\n1.", orderan[0],"\n2.",orderan[1], "\n3.",orderan[2], "\n4.",orderan[3], "\n5.",orderan[4], "\n6.", orderan[5])
    hapus = int(input("\nSebutkan layanan apa yang ingin dihapus (ID): "))
    if hapus == 1:
        data = orderan.pop(0)
        print(f"Data {data} berhasil dihapus")
    elif hapus == 2:
        data = orderan.pop(1)
        print(f"Data {data} berhasil dihapus")
    elif hapus == 3:
        data = orderan.pop(2)
        print(f"Data {data} berhasil dihapus")
    elif hapus == 4:
        data = orderan.pop(3)
        print(f"Data {data} berhasil dihapus")
    elif hapus == 5:
        data = orderan.pop(4)
        print(f"Data {data} berhasil dihapus")
    elif hapus == 6:
        data = orderan.pop(5)
        print(f"Data {data} berhasil dihapus")
    else:
        print("Pilihan kamu tidak valiiidd!!!!!")

elif Pilihan == "5":
    print()
    print("Terima kasih telah menghubungi kami :) ")
    
else:
    print("ADA MASALAH APA KAWAN??!!!!!")