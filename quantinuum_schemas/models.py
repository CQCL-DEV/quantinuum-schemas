import json
from typing import Optional, Sequence, Union

from pydantic import BaseModel
from pytket._tket.circuit import Circuit


class CircuitStruct(BaseModel):
    circuit_str: str

    # Add custom validators here.
    def get_circuit(self) -> Circuit:
        """Get a pytket Circuit object."""
        return Circuit.from_dict(json.loads(self.circuit_str))

    @staticmethod
    def from_circuit(circuit: Circuit) -> "CircuitStruct":
        """Serialise a pytket Circuit."""
        return CircuitStruct(circuit_str=json.dumps(circuit.to_dict()))


class DefaultCompilationPassArgs(BaseModel):
    optimisation_level: int = 2


class ProcessCircuitsArgs(BaseModel):
    circuits: Sequence[CircuitStruct]
    n_shots: Union[None, int, Sequence[Optional[int]]] = None
    valid_check: bool = True
