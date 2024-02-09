from qiskit import *
from qiskit.visualization import plot_histogram
import qiskit.tools.jupyter
from qiskit.tools.monitor import job_monitor

circuit = QuantumCircuit(2, 2)

circuit.cx(0, 1) # 0 -> control qubit, 1 -> target qubit
circuit.measure([0, 1], [0, 1])

circuit.draw()

simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend = simulator).result()

plot_histogram(result.get_counts(circuit))

IBMQ.load_account()
provider = IBMQ.get_provider("ibm-q")
quantum_computer = provider.get_backend("ibm_osaka")

%qiskit_job_watcher
job = execute(circuit, backend = quantum_computer)
job_monitor(job)

quantum_result = job.result()
plot_histogram(quantum_result.get_counts(circuit))

%qiskit_disable_job_watcher
