import json
from typing import Optional, Sequence, Union

from pydantic import BaseModel, field_validator
from pytket._tket.circuit import Circuit


class CircuitStruct(BaseModel):
    circuit_json: str

    @field_validator("circuit_json")
    @classmethod
    def validate_circuit_json(cls, raw: str):
        Circuit.from_dict(json.loads(raw))
        return raw

    def get_circuit(self) -> Circuit:
        """Get a pytket Circuit object."""
        return Circuit.from_dict(json.loads(self.circuit_json))

    @staticmethod
    def from_circuit(circuit: Circuit) -> "CircuitStruct":
        """Serialise a pytket Circuit."""
        return CircuitStruct(circuit_json=json.dumps(circuit.to_dict()))


class DefaultCompilationPassArgs(BaseModel):
    optimisation_level: int = 2


class ProcessCircuitsArgs(BaseModel):
    circuits: Sequence[CircuitStruct]
    n_shots: Union[None, int, Sequence[Optional[int]]] = None
    valid_check: bool = True
