# Import module
import os

# Variabel
tasks = []

# Menambahkan task ke dalam list tasks
def add_task():
    task = input("Masukkan task baru: ")
    tasks.append(task)
    print("Task '{}' berhasil ditambahkan!".format(task))

# Menghapus task dari list tasks
def remove_task():
    task = input("Masukkan task yang ingin dihapus: ")
    if task in tasks:
        tasks.remove(task)
        print("Task '{}' berhasil dihapus!".format(task))
    else:
        print("Task '{}' tidak ditemukan.".format(task))

# Menampilkan semua task dari list tasks
def show_tasks():
    if len(tasks) == 0:
        print("Tidak ada task yang tersedia. Silahkan tambahkan terlebih dahulu")
    else:
        print("Daftar Task:")
        for task in tasks:
            print("- {}".format(task))

# Fungsi untuk membersihkan layar
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Pilihan
while True:
    clear_screen()
    print("•••••••••• [ ToDo List App ] ••••••••••")
    print("1. Tambah Task")
    print("2. Hapus Task")
    print("3. Lihat Daftar Task")
    print("4. Keluar")

    choice = input("Masukkan pilihan (1/2/3/4): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        remove_task()
    elif choice == '3':
        show_tasks()
        input("Tekan ENTER untuk kembali ke menu utama.")
    elif choice == '4':
        print("Terima kasih telah menggunakan ToDo List App!")
        break
    else:
        print("Pilihan yang Anda masukkan salah.")
        input("Tekan ENTER untuk kembali ke menu utama.")
