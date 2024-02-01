"""Configuration for Qulacs compilation and simulation."""
from typing import Literal, Optional

from pydantic import BaseModel

from quantinuum_schemas.models import (
    CircuitStruct,
    DefaultCompilationPassArgs,
    ProcessCircuitsArgs,
)


class QulacsConfig(BaseModel):
    """Data required to instantiate a Qulacs backend."""

    result_type: str = "state_vector"


class QulacsCompilationPassKwargs(BaseModel):
    """Extra kwargs to default_compilation_pass for Qulacs."""


class QulacsCompilationRequest(BaseModel):
    """Qulacs config and any additional arguments to default_compilation_pass."""

    name: Literal["QulacsCompilationRequest"] = "QulacsCompilationRequest"

    config: QulacsConfig
    circuit: CircuitStruct
    args: DefaultCompilationPassArgs = DefaultCompilationPassArgs()
    kwargs: QulacsCompilationPassKwargs = QulacsCompilationPassKwargs()


class QulacsProcessKwargs(BaseModel):
    """Extra kwargs to process_circuits for Qulacs."""

    seed: Optional[int] = None


class QulacsSimulationRequest(BaseModel):
    """Qulacs config and any additional kwargs to process_circuits."""

    name: Literal["QulacsSimulationRequest"] = "QulacsSimulationRequest"

    config: QulacsConfig
    args: ProcessCircuitsArgs
    kwargs: QulacsProcessKwargs = QulacsProcessKwargs()
