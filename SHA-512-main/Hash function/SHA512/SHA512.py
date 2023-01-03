import math

#ASCII to hex

def text_to_hex(s):
    d = ''
    c = []
    for i in s:
        c.append(hex(ord(i)))           #Chuyên kí tự ASCII về số hexa
    for i in range(len(c)):
        c[i] = c[i].replace('0x', '')   #loại bỏ phần '0x' của số hexa
    for i in range(len(c)):
        if len(c[i]) == 1:              #thêm '0' đối với các số hexa chỉ
            c[i] = '0' + c[i]           #có 1 kí tự
    for i in c:
        d += i
    d = d.upper()
    return d

#CHuyển số hexa về số nhị phân
def hex_to_bin(s):
    trans = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111"}
    binary = ""
    for i in range(len(s)):
        binary = binary + trans[s[i]]
    return binary

#Chuyển số nhị phân về hexa
def bin_to_hex(s):
    trans = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": "A",
        "1011": "B",
        "1100": "C",
        "1101": "D",
        "1110": "E",
        "1111": "F"}
    hexa = ""
    for i in range(0, len(s), 4):
        ch = ""
        ch += s[i]              #chuyển từng 4bit thành 1 số hexa
        ch += s[i+1]
        ch += s[i+2]
        ch += s[i+3]
        hexa = hexa + trans[ch]
    return hexa

#Chuyển thập phân sang nhị phân
def dec_to_bin(s):
    res = bin(s).replace("0b", "") # loai bo 0b cua ham bin
    if(len(res) % 4 != 0):
        div = len(res) / 4
        div = int(div)
        counter = (4 * (div + 1)) - len(res)
        for i in range(0, counter):
            res = '0' + res
    return res

#chia khối
def divide(s):
    c = []
    length = hex(len(s) * 4)            #lưu giá trị độ dài của message (theo bit)
    length  = length.replace('0x', '')  #dưới dạng chuỗi hexa
    length = length.upper()
    s += '8'
    while 1:                            #padding thêm bit vào message
        if len(s) % 256 == 224:         #bit đầu là '1', các bit sau là '0'
            break
        s += '0'
    while 1:                              
        if (len(s) + len(length)) % 256 == 0:
            s += length                 #lưu giá trị độ dài vào cuối dãy
            break
        s += '0'
    for i in range(0, len(s), 256):     #chia thành các khối 1024bit (256 số hexa)
        c.append(s[i:i + 256])
    return c

#Chia từng khối 1024bit thành các khối 64bit
def div(s):
    n = []
    for i in range(len(s)):
        m = []
        for j in range(0, 256, 16):       #mỗi khối 1024bit(256 số hexa) được chia thành
            m.append(s[i][j:j+16])          #16 khối 16 bit
        n.append(m)
    return n


#hàm dịch vòng phải n bit
def rightshift(s, n):
    s = hex_to_bin(s)
    if n == 0:
        return bin_to_hex(s)
    else:
        for i in range(0, n):               #thực hiện n lần dịch phải 1 bit
            k = ''
            k += s[-1]                      #dịch bit cuối cùng lên đầu tiên
            k += s[:len(s) - 1]             #thêm các bit còn lại
            s = k
        return bin_to_hex(s)

#Dịch trái n bit, bên phải thêm bit '0'
def leftshift(s, n):  
    s = hex_to_bin(s)
    if n == 0:
        return bin_to_hex(s)
    else:
        for i in range(0, n):             #dich trai 1 bits, thuc hien n lan
            k = ''
                  #lay tu bit[1] den het + bit '0'
            k += '0'
            k += s[:len(s) - 1]
            s = k
        return bin_to_hex(s)
#phép xor 2 số hexa: 
def xor_hex(a, b):          
    a = hex_to_bin(a)       #chuyển về dạng nhị phân
    b = hex_to_bin(b)
    c = ''
    for i in range(len(a)):
        if a[i] == b[i]:    #xor từng bit của a với bit tương ứng của b
            c += '0'
        else: c += '1'
    c = bin_to_hex(c)       #chuyển lại về dạng hexa
    return c

#phép cộng modulo 2^64
def add(a, b):
    val = int(a, 16) + int(b, 16)
    while val > int(math.pow(2, 64)):
        val = val - int(math.pow(2, 64))        #đưa về giá trị trong modulo 2^64
    val = hex(val).replace('0x', '') 
    s = ''
    while 1:
        if len(s) + len(val) == 16:
            s += val
            break                               #padding các bit '0' để số đầu ra
        s += '0'                                #tương ứng là 64bit (16 số hexa)
    s = s.upper()
    return s

#phép and
def and2(a, b):
    a = hex_to_bin(a)               #chuyển a, b về dạng nhị phân
    b = hex_to_bin(b)
    c = ''
    for i in range(len(a)):
        if a[i] == '1' and b[i] == '1': 
            c += '1'                #thực hiện phép and: trả về 1 nếu cả hai là bit '1'
        else: c += '0'              # còn lại trả về 0
    c = bin_to_hex(c)
    return c

#phép not
def not1(s):
    s = hex_to_bin(s)
    c = ''
    for i in range(len(s)):
        if s[i] == '0':             #đảo ngược giá trị bit: '1' chuyển thành '0'; '0' thành '1'
            c +='1'
        else: c+= '0'
    c = bin_to_hex(c)
    return c

#
def sum0(s):                        #hàm tính sum0_512:
    ROTR28 = rightshift(s, 28)      # ROTR28 ^ ROTR34 ^ ROTR39
    ROTR34 = rightshift(s, 34)  
    ROTR39 = rightshift(s, 39)
    val = xor_hex(ROTR28, xor_hex(ROTR34, ROTR39))
    return val

def sum1(s):                        #hàm tính sum1_512:
    ROTR14 = rightshift(s, 14)      #  ROTR14 ^ ROTR18 ^ ROTR41
    ROTR18 = rightshift(s, 18)
    ROTR41 = rightshift(s, 41)
    val = xor_hex(ROTR14, xor_hex(ROTR18, ROTR41))
    return val

def s0(s):                          #hàm tính sigma0_512:
    ROTR1 = rightshift(s, 1)        #ROTR1 ^ ROTR8 ^ SHR7
    ROTR8 = rightshift(s, 8)
    SHR7 = leftshift(s, 7)
    val = xor_hex(ROTR1, xor_hex(ROTR8, SHR7))
    return val


def s1(s):                          #hàm tính sigma1_512:
    ROTR19 = rightshift(s, 19)      #ROTR19 ^ ROTR61 ^ SHR6
    ROTR61 = rightshift(s, 61)
    SHR6 = leftshift(s, 6)
    val = xor_hex(ROTR19, xor_hex(ROTR61, SHR6))
    return val

def Maj(a, b, c):
    x = and2(a, b)
    y = and2(a, c)                  # (a & b) ^ (a&c) ^ (b&c)
    z = and2(b, c)
    val = xor_hex(x, xor_hex(y, z))
    return val

    
def Ch(e, f, g):
    x = and2(e, f)                  #(e & f) ^ ((~e) & g)
    y = and2(not1(e), g)
    val = xor_hex(x, y)
    return val


K = ['428a2f98d728ae22', '7137449123ef65cd', 'b5c0fbcfec4d3b2f', 'e9b5dba58189dbbc',
     '3956c25bf348b538', '59f111f1b605d019', '923f82a4af194f9b', 'ab1c5ed5da6d8118',
     'd807aa98a3030242', '12835b0145706fbe', '243185be4ee4b28c', '550c7dc3d5ffb4e2',
     '72be5d74f27b896f', '80deb1fe3b1696b1', '9bdc06a725c71235', 'c19bf174cf692694',
     'e49b69c19ef14ad2', 'efbe4786384f25e3', '0fc19dc68b8cd5b5', '240ca1cc77ac9c65',
     '2de92c6f592b0275', '4a7484aa6ea6e483', '5cb0a9dcbd41fbd4', '76f988da831153b5',
     '983e5152ee66dfab', 'a831c66d2db43210', 'b00327c898fb213f', 'bf597fc7beef0ee4',
     'c6e00bf33da88fc2', 'd5a79147930aa725', '06ca6351e003826f', '142929670a0e6e70',
     '27b70a8546d22ffc', '2e1b21385c26c926', '4d2c6dfc5ac42aed', '53380d139d95b3df',
     '650a73548baf63de', '766a0abb3c77b2a8', '81c2c92e47edaee6', '92722c851482353b',
     'a2bfe8a14cf10364', 'a81a664bbc423001', 'c24b8b70d0f89791', 'c76c51a30654be30',
     'd192e819d6ef5218', 'd69906245565a910', 'f40e35855771202a', '106aa07032bbd1b8',
     '19a4c116b8d2d0c8', '1e376c085141ab53', '2748774cdf8eeb99', '34b0bcb5e19b48a8',
     '391c0cb3c5c95a63', '4ed8aa4ae3418acb', '5b9cca4f7763e373', '682e6ff3d6b2b8a3',
     '748f82ee5defb2fc', '78a5636f43172f60', '84c87814a1f0ab72', '8cc702081a6439ec',
     '90befffa23631e28', 'a4506cebde82bde9', 'bef9a3f7b2c67915', 'c67178f2e372532b',
     'ca273eceea26619c', 'd186b8c721c0c207', 'eada7dd6cde0eb1e', 'f57d4f7fee6ed178',
     '06f067aa72176fba', '0a637dc5a2c898a6', '113f9804bef90dae', '1b710b35131c471b',
     '28db77f523047d84', '32caab7b40c72493', '3c9ebe0a15c9bebc', '431d67c49c100d4c',
     '4cc5d4becb3e42b6', '597f299cfc657e2a', '5fcb6fab3ad6faec', '6c44198c4a475817']

#tạo bộ message Wt
def create(s):
    
    w = []
    for i in range(0, len(s)):  
        m = []
        for t in range(0, 16):      #trong 16 bước đầu, giá trị của w bằng
            m.append(s[i][t])       #giá trị các khối tương ứng trong message
        for t in range(16, 80):  
            m.append(add(s1(m[t-2]), add(m[t-7], add(s0(m[t-15]), m[t-16]))))
                    #64 bước còn lại: tính qua công thức
                    #s1(w[t-2]) + w[t-7] + s0(t-15) + w[t-16]
                    #phép cộng trong trường GF(2^64)
        w.append(m)
    return w


def SHA_512(s):
    s = text_to_hex(s)              #chuyển s từ kí tự ASCII về hexa
    M = divide(s)                   #chia M thành các khối 1024bit, padding bit                              #lưu giá trị độ dài message vào cuối
    M = div(M)
    w = create(M)                   #ánh xạ khối 1024bit thành 80 khối 64bit
    H = ['6A09E667F3BCC908',
         'BB67AE8584CAA73B',
         '3C6EF372FE94F82B',
         'A54FF53A5F1D36F1',
         '510E527FADE682D1',
         '9B05688C2B3E6C1F',
         '1F83D9ABFB41BD6B',
         '5BE0CD19137E2179']
    for i in range(0, len(M)):
        #khởi tạo các biến làm việc
        a = H[0]
        b = H[1]
        c = H[2]
        d = H[3]
        e = H[4]
        f = H[5]
        g = H[6]
        h = H[7]
        #thực hiện tính toán băm chính
        for t in range(0, len(K)):
            T1 = add(h, add(Ch(e, f, g), add(sum1(e), add(w[i][t], K[t].upper()))))
            T2 = add(sum0(a), Maj(a, b, c))
            h = g
            g = f                           #Tính toán các giá trị mới của thanh ghi
            f = e                           #qua từng vòng lặp
            e = add(d, T1)
            d = c
            c = b
            b = a
            a = add(T1, T2)
        H[0] = add(H[0],a)
        H[1] = add(H[1],b)                  #H[i] = H[i-1] + a,b,c...
        H[2] = add(H[2],c)
        H[3] = add(H[3],d)
        H[4] = add(H[4],e)
        H[5] = add(H[5],f)
        H[6] = add(H[6],g)
        H[7] = add(H[7],h)
    digest = ''
    for i in range(len(H)):
        digest = digest + H[i] +' '
    return digest

with open('input.txt', 'r', encoding = 'UTF-8') as text,open('output.txt', 'w', encoding = 'UTF-8') as md:
    message = text.read()
    digest = SHA_512(message)
    md.write(digest)
    #print(digest)