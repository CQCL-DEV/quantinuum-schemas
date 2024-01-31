"""Configuration for Qulacs compilation and simulation."""
from typing import Optional

from pydantic import BaseModel


class AerSimulateRequest(BaseModel):
    """Data required to instantiate a Aer backend and then process_circuits.

    Currently this model is just a draft for basic simulations.
    In future, this DTO should be kept in sync with the constructor of AerBackend.
    """

    # Attributes required to instantiate the backend.
    simulation_method: str = "automatic"
    n_qubits: int = 40

    # Additional kwarg to process_circuits.
    seed: Optional[int] = None
