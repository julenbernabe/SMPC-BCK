# mult-0--0
ldsi s0, 4 # 0
ldsi s1, 7 # 1
ldsi s2, 9 # 2
triple s4, s5, s6 # 3
subs s7, s0, s4 # 4
subs s8, s1, s5 # 5
startopen 2, s7, s8 # 6
stopopen 2, c0, c1 # 7
mulm s9, s5, c0 # 8
mulm s10, s4, c1 # 9
mulc c2, c0, c1 # 10
adds s11, s6, s9 # 11
adds s12, s11, s10 # 12
addm s3, s12, c2 # 13
triple s14, s15, s16 # 14
subs s17, s3, s14 # 15
subs s18, s2, s15 # 16
startopen 2, s17, s18 # 17
stopopen 2, c3, c4 # 18
mulm s19, s15, c3 # 19
mulm s20, s14, c4 # 20
mulc c5, c3, c4 # 21
adds s21, s16, s19 # 22
adds s22, s21, s20 # 23
addm s13, s22, c5 # 24
private_output s13, 0, 0 # 25
