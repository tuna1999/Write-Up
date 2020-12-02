
from z3 import *

inp = [BitVec('inp_%d'%i,8) for i in range(16)]

s = Solver()

s.add((inp[11] ^ (inp[9] ^ inp[5] ^ inp[1] ^ inp[0] ^ inp[10] ^ inp[6] ^ inp[3] ^ inp[2] ^ inp[15] ^ inp[14])) == 117)
s.add((inp[11] ^ (inp[9] ^ inp[8] ^ inp[5] ^ inp[4] ^ inp[1] ^ inp[0] ^ inp[12] ^ inp[13] ^ inp[15] ^ inp[14])) == 49 )
s.add((inp[8] ^ (inp[5] ^ inp[4] ^ inp[6] ^ inp[3] ^ inp[7] ^ inp[12] ^ inp[13] ^ inp[15] ^ inp[14])) == 82 )
s.add((inp[11] ^ (inp[9] ^ inp[8] ^ inp[5] ^ inp[1] ^ inp[0] ^ inp[10] ^ inp[13] ^ inp[15] ^ inp[14])) == 102)
s.add((inp[11] ^ (inp[9] ^ inp[5] ^ inp[4] ^ inp[1] ^ inp[3] ^ inp[2] ^ inp[15] ^ inp[12])) == 115 )
s.add((inp[8] ^ (inp[4] ^ inp[0] ^ inp[6] ^ inp[3] ^ inp[2] ^ inp[12] ^ inp[15] ^ inp[14])) == 56 )
s.add((inp[14] ^ inp[13] ^ inp[12] ^ inp[11] ^ inp[8] ^ inp[4] ^ inp[0] ^ inp[10] ^ inp[2] == 50 ))
s.add((inp[4] ^ (inp[10] ^ inp[6] ^ inp[3] ^ inp[2] ^ inp[13] ^ inp[12] ^ inp[11])) == 110 )
s.add((inp[9] ^ inp[8] ^ inp[0] ^ inp[2] ^ inp[7] ^ inp[13] ^ inp[15] ^ inp[14] == 7 ))
s.add((inp[14] ^ (inp[12] ^ inp[11] ^ inp[4] ^ inp[0] ^ inp[10] ^ inp[6] ^ inp[2])) == 7 )
s.add((inp[8] ^ inp[4] ^ inp[1] ^ inp[0] ^ inp[7] ^ inp[13] ^ inp[11] == 16 ))
s.add((inp[9] ^ (inp[8] ^ inp[0] ^ inp[7] ^ inp[13] ^ inp[12] ^ inp[11])) == 29 )
s.add((inp[9] ^ inp[0] ^ inp[10] ^ inp[6] ^ inp[7] ^ inp[13] ^ inp[11] == 7 ))
s.add((inp[9] ^ (inp[5] ^ inp[4] ^ inp[3] ^ inp[15] ^ inp[12])) == 25 )
s.add((inp[9] ^ inp[1] ^ inp[2] ^ inp[12] ^ inp[15] ^ inp[14] == 78 ))
s.add((inp[14] ^ (inp[5] ^ inp[1] ^ inp[3] ^ inp[7])) == 48 )

print(s.check())

while s.check() == sat:
	m = s.model()
	ss = ""
	for d in inp:
		ss += chr(m[d].as_long())
	print("input:",ss)
	s.add(Or([inp[ii] != m[inp[ii]] for ii in range(16)]))


