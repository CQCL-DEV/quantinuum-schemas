"""Configuration for Qulacs compilation and simulation."""
from typing import Literal, Optional

from pydantic import BaseModel

from quantinuum_schemas.models import (
    CircuitStruct,
    DefaultCompilationPassArgs,
    ProcessCircuitsArgs,
)


class AerConfig(BaseModel):
    """Data required to instantiate a Aer backend.

    Draft: does not include noise_model or crosstalk_params."""

    # noise_model: Optional[NoiseModel] = None
    simulation_method: str = "automatic"
    # crosstalk_params: Optional[CrosstalkParams] = None
    n_qubits: int = 40


class AerCompilationPassKwargs(BaseModel):
    """Extra kwargs to default_compilation_pass for Aer."""

    placement_options: Optional[dict] = None


class AerCompilationRequest(BaseModel):
    """Aer config and any additional arguments to default_compilation_pass."""

    name: Literal["AerCompilationRequest"] = "AerCompilationRequest"

    config: AerConfig
    circuit: CircuitStruct
    args: DefaultCompilationPassArgs = DefaultCompilationPassArgs()
    kwargs: AerCompilationPassKwargs = AerCompilationPassKwargs()


class AerProcessKwargs(BaseModel):
    """Extra kwargs to process_circuits for Aer."""

    seed: Optional[int] = None


class AerSimulationRequest(BaseModel):
    """Aer config and any additional kwargs to process_circuits."""

    name: Literal["AerSimulationRequest"] = "AerSimulationRequest"

    config: AerConfig
    args: ProcessCircuitsArgs
    kwargs: AerProcessKwargs
