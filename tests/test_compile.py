import json

import pytest
from pytket._tket.circuit import Circuit
from sympy import symbols

from quantinuum_schemas import (
    CompilationRequest,
    QulacsCompilationRequest,
    QulacsConfig,
)
from quantinuum_schemas.models import CircuitStruct

test_circuit = Circuit(2)
a, b = symbols("a b")
test_circuit.Rx(0.5 + a, 0).Rx(-0.5 + b, 1).CZ(0, 1).Rx(0.5 + b, 0).Rx(-0.5 + a, 1)
test_circuit.measure_all()


@pytest.mark.parametrize("")
def test_compile():
    config = QulacsConfig()
    qulacs_req = QulacsCompilationRequest(
        config=config, circuit=CircuitStruct.from_circuit(test_circuit)
    )
    req_str = qulacs_req.model_dump_json()
    out_req = (CompilationRequest(**json.loads(req_str))).root
    assert out_req == qulacs_req
