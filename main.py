from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector

class QCircuit:
    
    def __init__(self) -> None:
        self.simulator = AerSimulator()
        self.qc = QuantumCircuit(1, 1)

    def half_plate(self):
        self.qc.h(0)
        self.qc.s(0)
        self.qc.h(0)

    def measure(self):
        self.qc.measure(0, 0)
    
    def simulate(self, shots:int):
        result = self.simulator.run(self.qc, shots=shots).result()
        return result.get_counts()

    def save_circuit(self, filename:str, dpi=200):
        circuit = self.qc.draw("mpl")
        circuit.savefig(filename, dpi=dpi)

interferometer = QCircuit()
interferometer.half_plate()
interferometer.half_plate()
interferometer.measure()
result_counts = interferometer.simulate(1000)
print(result_counts)

#interferometer.save_circuit("Mach-Zehnder Interferometer.png", 200)
