
memori = {
    14: 2,
    15: 3,
    13: 0    
}

ACC = 0

def LOAD(alamat):
    global ACC
    ACC = memori[alamat]

def ADD(alamat):
    global ACC
    ACC = ACC + memori[alamat]

def STORE(alamat):
    memori[alamat] = ACC

def HALT():
    print("Program berhenti")

# ===== Program Assembly =====
LOAD(14)      # ACC = 2
ADD(15)       # ACC = 2 + 3
STORE(13)     # simpan hasil ke alamat 13
HALT()

# Cek hasil
print("Isi memori alamat 13:", memori[13])
