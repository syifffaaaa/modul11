class ObjekProgram:
    def __init__(self):
        self.nama = None
        self.nilai = None
        
    def set_nama(self, nama):
        self.nama = nama
        
    def get_nama(self):
        return self.nama if self.nama is not None else "None"
    
    def set_nilai(self, nilai):
        self.nilai = nilai
        
    def get_nilai(self):
        return self.nilai if self.nilai is not None else "None"
    
def tampilmenu():
    print("\n==== Program OOP ====")
    print("1. Mendeklarasikan Objek")
    print("2. Menampilkan Objek")
    print("3. Merubah Nilai Objek")
    print("4. Menghapus Objek")
    print("5. Keluar")
    
def milih():
    return input("Masukkan pilihan (1/2/3/4/5): ")

def main():
    objek_program = ObjekProgram()
    
    while True:
        tampilmenu()
        pilihan = milih()
        
        if pilihan == '1':
            innama = input("\nMasukkan nama: ")
            innilai = input("Masukkan nilai: ")
            
            objek_program.set_nama(innama)
            objek_program.set_nilai(innilai)
            
            print("\nDatamu Berhasil Ditambahkan")
            
        elif pilihan == '2':
            print(f"\nNama: {objek_program.get_nama()}")
            print(f"Nilai: {objek_program.get_nilai()}")
            
        elif pilihan == '3':
            mengubah = input("\nApa yang mau kamu ubah (nama/nilai): ")
            if mengubah.lower() == 'nama':
                innama = input("Masukkan nama baru: ")
                objek_program.set_nama(innama)
                print("\nData Nama Berhasil Diubah")
            elif mengubah.lower() == 'nilai':
                innilai = input("Masukkan nilai baru: ")
                objek_program.set_nilai(innilai)
                print("\nData Nilai Berhasil Diubah")
                
        elif pilihan == '4':
            objek_program = ObjekProgram()
            print("\nData Kamu Berhasil Dihapus")
            
        elif pilihan == '5':
            print("\n==Terima Kasih Telah Menggunakan Program Ini==")
            break
        
if __name__ == "__main__":
    main()

        
    