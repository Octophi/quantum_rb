def buildCirc(qc, circuitArray, perm):
    for gate in circuitArray:
        print(gate)
        addGate(qc, gate, perm)


def addGate(qc, gate, perm):
    genKeys = ["x", "z", "h", "s", "cx", "cz"]
    
    gateSpec = gate.split()
    gateIndex = genKeys.index(gateSpec[0])
    
    if gateIndex == 0:
        addX(qc,gateSpec[1:],perm)
    elif gateIndex ==1:
        addZ(qc,gateSpec[1:],perm)
    elif gateIndex ==2:
        addH(qc,gateSpec[1:],perm)
    elif gateIndex ==3:
        addS(qc,gateSpec[1:],perm)
    elif gateIndex ==4:
        addCX(qc,gateSpec[1:],perm)
    elif gateIndex ==5:
        addCZ(qc,gateSpec[1:],perm)
    
def addX(qc,gateNums,perm):
    for num in gateNums:
        qub = perm[int(num)]
        qc.x(qr[qub])
        
def addZ(qc,gateNums,perm):
    for num in gateNums:
        qub = perm[int(num)]
        qc.z(qr[qub])

def addH(qc,gateNums,perm):
    for num in gateNums:
        qub = perm[int(num)]
        qc.h(qr[qub])
        
def addS(qc,gateNums,perm):
    for num in gateNums:
        qub = perm[int(num)]
        qc.s(qr[qub])
        
def addCX(qc,gateNums,perm):
    qub1 = perm[int(gateNums[0])]
    qub2 = perm[int(gateNums[1])]
    qc.cx(qr[qub1], qr[qub2])
    
def addCZ(qc,gateNums,perm):
    qub1 = perm[int(gateNums[0])]
    qub2 = perm[int(gateNums[1])]
    qc.cz(qr[qub1], qr[qub2])
