f = open("key","rb")
c = f.read()
f.close()

def lfsr(R,mask):
    output = (R << 1) & 0xffffff
    
    i=(R&mask)&0xffffff
    lastbit=0
    while i!=0:
        lastbit^=(i&1)
        i=i>>1
        
    output^=lastbit
    return (output,lastbit)

l = []
for ch in c:
    tmp0 = 0
    for o1 in xrange(2):
        tmp1 = (tmp0<<1)^o1
        for o2 in xrange(2):
            tmp2 = (tmp1<<1)^o2
            for o3 in xrange(2):
                tmp3 = (tmp2<<1)^o3
                for o4 in xrange(2):
                    tmp4 = (tmp3<<1)^o4
                    for o5 in xrange(2):
                        tmp5= (tmp4<<1)^o5
                        for o6 in xrange(2):
                            tmp6 = (tmp5<<1)^o6
                            for o7 in xrange(2):
                                tmp7 = (tmp6<<1)^o7
                                for o8 in xrange(2):
                                    tmp8 = (tmp7<<1)^o8
                                    if tmp8 == ord(ch) :
                                        l.append(o1)
                                        l.append(o2)
                                        l.append(o3)
                                        l.append(o4)
                                        l.append(o5)
                                        l.append(o6)
                                        l.append(o7)
                                        l.append(o8)

mask = 0b1010011000100011100 
for r1 in ['0', '1']:
    for r2 in ['0', '1']:
        for r3 in ['0', '1']:
            for r4 in ['0', '1']:
                for r5 in ['0', '1']:
                    for r6 in ['0', '1']:
                        for r7 in ['0', '1']:
                            for r8 in ['0', '1']:
                                for r9 in ['0', '1']:
                                    for r10 in ['0', '1']:
                                        for r11 in ['0', '1']:
                                            for r12 in ['0', '1']:
                                                for r13 in ['0', '1']:
                                                    for r14 in ['0', '1']:
                                                        for r15 in ['0', '1']:
                                                            for r16 in ['0', '1']:
                                                                for r17 in ['0', '1']:
                                                                    for r18 in ['0', '1']:
                                                                        for r19 in ['0', '1']:
                                                                            string = '0b'+r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r13+r14+r15+r16+r17+r18+r19
                                                                            R = int(string, 2)
                                                                            flag = 0
                                                                            for o in l:
                                                                                (R, out) = lfsr(R, mask)
                                                                                if o != out:
                                                                                    flag = 0
                                                                                else:
                                                                                    flag += 1
                                                                            if flag == len(l):
                                                                                print 'flag{' + string[2:] + '}'
