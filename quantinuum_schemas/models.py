"""Models for interacting with pytket."""

import json
from typing import Annotated, Sequence, Union

from pydantic import BaseModel, GetPydanticSchema, PlainSerializer, PlainValidator
from pydantic_core.core_schema import no_info_plain_validator_function as get_schema
from pytket._tket.circuit import Circuit
from pytket.backends.backendresult import BackendResult


def validate_circuit(raw: str) -> Circuit:
    """Use pytket to validate a circuit."""
    if isinstance(raw, Circuit):
        return raw
    return Circuit.from_dict(json.loads(raw))


def serialise_circuit(circuit: Circuit) -> str:
    """Use pytket to serialise a circuit."""
    return json.dumps(circuit.to_dict())


def validate_result(raw: str) -> BackendResult:
    """Use pytket to validate backend result."""
    if isinstance(raw, BackendResult):
        return raw
    return BackendResult.from_dict(json.loads(raw))


def serialise_result(result: BackendResult) -> str:
    """Use pytket to serialise backend result."""
    return json.dumps(result.to_dict())


circuit_schema = GetPydanticSchema(lambda _x, _y: get_schema(validate_circuit))
circuit_validator = PlainValidator(validate_circuit)
circuit_serializer = PlainSerializer(serialise_circuit, return_type=str)
CircuitModel = Annotated[Circuit, circuit_schema, circuit_serializer]

result_schema = GetPydanticSchema(lambda _x, _y: get_schema(validate_result))
result_validator = PlainValidator(validate_result)
result_serializer = PlainSerializer(serialise_result, return_type=str)
BackendResultModel = Annotated[BackendResult, result_schema, result_serializer]


class DefaultCompilationPassArgs(BaseModel):
    """Arguments that make sense for all default_compilation_pass functions."""

    optimisation_level: int = 2


class ProcessCircuitsArgs(BaseModel):
    """Arguments that make sense for all process_circuits functions."""

    n_shots: Union[None, int, Sequence[int]] = None
    valid_check: bool = True
