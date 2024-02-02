"""Test that instantiated backend can compile and simulate if applicable."""

import json

import pytest
from pytket._tket.circuit import Circuit

from quantinuum_schemas import (
    CompilationRequest,
    CompilationRequestData,
    QulacsCompilationRequest,
    SimulationRequest,
    SimulationRequestData,
)
from quantinuum_schemas.aer import AerCompilationRequest, AerSimulationRequest
from quantinuum_schemas.backend import compile_circuit, simulate_circuits
from quantinuum_schemas.qulacs import QulacsSimulationRequest


def get_circ() -> Circuit:
    """Build a test circuit."""
    circ = Circuit(2, 2)
    circ.Rx(0.2, 0).CX(0, 1).Rz(-0.7, 1).measure_all()
    return circ


compilation_requests: list[CompilationRequestData] = [
    AerCompilationRequest(circuit=get_circ()),
    QulacsCompilationRequest(circuit=get_circ()),
]


@pytest.mark.parametrize("data", compilation_requests)
def test_compile(data: CompilationRequestData):
    """Compile a circuit."""

    req_json = data.model_dump_json()
    req = CompilationRequest(**json.loads(req_json))
    circuit = compile_circuit(req)

    assert len(circuit.bits) == 2
    assert len(circuit.qubits) == 2
    assert circuit != get_circ()


simulation_requests: list[SimulationRequestData] = [
    AerSimulationRequest(circuits=[]),
    QulacsSimulationRequest(circuits=[]),
]


@pytest.mark.parametrize(
    "compilation_data,simulation_data", zip(compilation_requests, simulation_requests)
)
def test_simulate(
    compilation_data: CompilationRequestData, simulation_data: SimulationRequestData
):
    """Simulate a circuit."""
    compilation_req_json = compilation_data.model_dump_json()
    simulation_req_json = simulation_data.model_dump_json()
    compilation_req = CompilationRequest(**json.loads(compilation_req_json))
    simulation_req = SimulationRequest(**json.loads(simulation_req_json))

    output_circuit = compile_circuit(compilation_req)
    simulation_req.root.circuits.append(output_circuit)  # pylint: disable=no-member
    result = simulate_circuits(simulation_req)

    assert len(result) == 1
