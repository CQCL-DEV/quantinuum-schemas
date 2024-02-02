"""Functions requiring extra imports."""

from pytket.backends.backend import Backend

from quantinuum_schemas import (
    AerConfig,
    BackendConfig,
    CompilationRequest,
    QulacsConfig,
    SimulationRequest,
)
from quantinuum_schemas.models import BackendResultModel, CircuitModel
from quantinuum_schemas.typing_utils import assert_never


# pylint: disable=import-outside-toplevel
def get_backend(config: BackendConfig) -> Backend:
    """Instantiate a backend from a config."""
    match config:
        case AerConfig():
            from pytket.extensions.qiskit.backends.aer import AerBackend

            return AerBackend(
                noise_model=None,
                simulation_method=config.simulation_method,
                crosstalk_params=None,
                n_qubits=config.n_qubits,
            )
        case QulacsConfig():
            from pytket.extensions.qulacs.backends.qulacs_backend import QulacsBackend

            return QulacsBackend(result_type=config.result_type)
        case _:
            assert_never(config)


def compile_circuit(req: CompilationRequest) -> CircuitModel:
    """Compile a circuit given a CompilationRequest."""

    backend = get_backend(req.root.config)
    base_pass = backend.default_compilation_pass(**req.root.kwargs.model_dump())
    circuit = req.root.circuit
    base_pass.apply(circuit)
    return circuit


def simulate_circuits(
    req: SimulationRequest,
) -> list[BackendResultModel]:
    """Simulate a circuit given a SimulationRequest."""

    backend = get_backend(req.root.config)
    return backend.run_circuits(req.root.circuits, **req.root.kwargs.model_dump())
