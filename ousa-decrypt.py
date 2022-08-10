from ctypes import c_uint8, c_uint32
 
i = 0
newarray = bytearray()
 
with open("ciphered.zip", "rb") as obf, open("out.zip", "wb") as out:
    obf_array = bytearray(obf.read())
    while i < len(obf_array):
        newarray.append(obf_array[i] ^ c_uint8(~(c_uint32(0x161A >> i%32)).value).value)
        i += 1
    out.write(newarray)
