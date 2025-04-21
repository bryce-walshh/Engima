import machine as m

e = m.Enigma()

# setting rotor position and encrypting
e.set_rotor_position('AAA')

encrypted = e.encipher('this is a test')

print(encrypted)

# reseting rotor position and decrypting
machine2 = m.Enigma()
decrypted = machine2.decipher(encrypted)
print(decrypted)