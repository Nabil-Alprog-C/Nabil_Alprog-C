class RekeningBank:
    def __init__(self ,nama, saldo):
      self.nama = nama
      self.saldo = saldo



      self.score = score 
      self.name = name 


akun_budi =RekeningBank("Budi", 1000000)
print(f"saldo awal Budi : {akun_budi.saldo}")

akun_budi.saldo = -500000
print(f"saldo akhir budi : {akun_budi.saldo}")