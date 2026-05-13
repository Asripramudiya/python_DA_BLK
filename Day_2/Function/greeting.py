from datetime import datetime


def sapa_nama(nama=None):
    if nama is None:
        print("Silahkan masukkan nama ")
        return
    print(f"Hello {nama}")


sapa_nama()
sapa_nama("AS")

# print(datetime.now())
