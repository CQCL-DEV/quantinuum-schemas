"""Configuration for Qulacs compilation and simulation."""
from typing import Optional

from pydantic import BaseModel
from pytket.circuit import OpType
from pytket.passes import (
    DecomposeBoxes,
    FlattenRegisters,
    FullPeepholeOptimise,
    SequencePass,
    SynthesiseTket,
)
from pytket.passes.auto_rebase import auto_rebase_pass

_TWO_QUBIT_GATES = {OpType.CX, OpType.CZ, OpType.SWAP}
_ONE_QUBIT_GATES = {
    OpType.X,
    OpType.Y,
    OpType.Z,
    OpType.H,
    OpType.S,
    OpType.Sdg,
    OpType.T,
    OpType.Tdg,
}
_ONE_QUBIT_ROTATIONS = {OpType.Rx, OpType.Ry, OpType.Rz}
_MEASURE_GATES = {OpType.Measure}
_IBM_GATES = {OpType.U1, OpType.U2, OpType.U3}
_1Q_GATES = _ONE_QUBIT_ROTATIONS | _ONE_QUBIT_GATES | _MEASURE_GATES | _IBM_GATES
_ALL_GATES = _1Q_GATES | _TWO_QUBIT_GATES
_rebase_pass = auto_rebase_pass(_ALL_GATES)

QULACS_PASS_LEVEL_0 = SequencePass([DecomposeBoxes(), FlattenRegisters(), _rebase_pass])
QULACS_PASS_LEVEL_1 = SequencePass(
    [DecomposeBoxes(), FlattenRegisters(), SynthesiseTket(), _rebase_pass]
)
QULACS_PASS_LEVEL_2 = SequencePass(
    [DecomposeBoxes(), FlattenRegisters(), FullPeepholeOptimise(), _rebase_pass]
)


class QulacsSimulateRequest(BaseModel):
    """Data required to instantiate a Qulacs backend and then process_circuits.

    This DTO should be kept in sync with the constructor of the Backend defined in pytket-qulacs.
    """

    # Attributes required to instantiate the backend.
    result_type: str = "state_vector"

    # Additional kwarg to process_circuits.
    seed: Optional[int] = None
