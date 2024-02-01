"""Functions requiring extra imports."""
from pytket.backends.backend import Backend

from quantinuum_schemas import AerConfig, BackendConfig, QulacsConfig
from quantinuum_schemas.typing_utils import assert_never


# pylint: disable=import-outside-toplevel
def get_backend(config: BackendConfig) -> Backend:
    """Instantiate a backend from a config.

    In due course we may include the equivalent of default_compilation_pass into this repo.
    """
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
