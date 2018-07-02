from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, QISKitError
import qiskit
import importlib
importlib.reload(qiskit)

def buildCirc(qc, qr, circuitArray, perm):
    for gate in circuitArray:
        print(gate)
        addGate(qc, qr, gate, perm)


def addGate(qc, qr, gate, perm):
    gateSet = {
        "x": addX,
        "z": addZ,
        "h": addH,
        "s": addS,
        "cx": addCX,
        "cz": addCZ,
    }
    
    # convert gate string to gate array
    gateSpec = gate.split()
    
    # get appropriate function to add desired generators
    addGens = gateSet.get(gateSpec[0], lambda:"Invalid gate")
    addGens(qc, qr, gateSpec[1:],perm)
    
def addX(qc, qr, gateNums,perm):
    for num in gateNums:
        qub = perm[int(num)]
        qc.x(qr[qub])
        
def addZ(qc, qr, gateNums,perm):
    for num in gateNums:
        qub = perm[int(num)]
        qc.z(qr[qub])

def addH(qc, qr, gateNums,perm):
    for num in gateNums:
        qub = perm[int(num)]
        qc.h(qr[qub])
        
def addS(qc, qr, gateNums,perm):
    for num in gateNums:
        qub = perm[int(num)]
        qc.s(qr[qub])
        
def addCX(qc, qr, gateNums,perm):
    qub1 = perm[int(gateNums[0])]
    qub2 = perm[int(gateNums[1])]
    qc.cx(qr[qub1], qr[qub2])
    
def addCZ(qc, qr, gateNums,perm):
    qub1 = perm[int(gateNums[0])]
    qub2 = perm[int(gateNums[1])]
    qc.cz(qr[qub1], qr[qub2])

