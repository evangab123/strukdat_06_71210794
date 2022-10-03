class NodeTabungan:
    no_rekening = None
    nama = None
    saldo = None
    next = None

    def __init__(self,no_rekening,nama,saldo=0):
        self.no_rekening = no_rekening
        self.nama = nama
        self.saldo = saldo
        self.next = None

class SLNC:

    def __init__(self):
        self._head=None
        self._tail=None
        self._size = 0

    def __len__(self):
        return self._size

    def apaKosong(self):
        return self._size == 0

    def insert_head(self, no_rekening, nama, saldo=0):
        new = NodeTabungan(no_rekening, nama, saldo)
        if self._size == 0:
            self.head = new
            self.tail = new
            self.tail.next = self.head
            self._size += 1
        else:
            new.next = self.head
            self.head = new
            self._size += 1
    
    def print(self):
        if self._size == 0:
            print('Kosong')
        else:
            bantu = self.head
            while(bantu!=self.tail.next):
                print('Norek: ', bantu.no_rekening)
                print('Nama: ', bantu.nama)
                print('Saldo: ', bantu.saldo)
                bantu = bantu.next
                print('Norek: ', bantu.no_rekening)
                print('Nama: ', bantu.nama)
                print('Saldo: ', bantu.saldo) 

    def update(self,angka):
        if angka > 100:
            print("Maaf Besaran Persen Harus 0-100")
        else:
            bantu = self.head
            while(bantu!=self.tail.next):
                self.saldo = self.saldo + (self.saldo * (angka/100))
            print("Semua saldo rekening berhasil ditambah sebanyak",angka)


#testcase
slnc = SLNC()
slnc.insert_head(201,"Hanif",2500000)
slnc.insert_head(101,"Yudha",1500000)
slnc.print()
slnc.update(200)
slnc.update(50)