"""Configuration for Qulacs compilation and simulation."""

from typing import Literal, Optional

from pydantic import BaseModel

from quantinuum_schemas.models import (
    CircuitModel,
    DefaultCompilationPassArgs,
    ProcessCircuitsArgs,
)


class QulacsConfig(BaseModel):
    """Data required to instantiate a Qulacs backend."""

    result_type: str = "state_vector"


class QulacsCompilationPassKwargs(DefaultCompilationPassArgs, BaseModel):
    """Extra kwargs to default_compilation_pass for Qulacs."""


class QulacsCompilationRequest(BaseModel):
    """Qulacs config and any additional arguments to default_compilation_pass."""

    name: Literal["QulacsCompilationRequest"] = "QulacsCompilationRequest"

    circuit: CircuitModel
    kwargs: QulacsCompilationPassKwargs = QulacsCompilationPassKwargs()
    config: QulacsConfig = QulacsConfig()


class QulacsProcessKwargs(ProcessCircuitsArgs, BaseModel):
    """Extra kwargs to process_circuits for Qulacs."""

    seed: Optional[int] = None


class QulacsSimulationRequest(BaseModel):
    """Qulacs config and any additional kwargs to process_circuits."""

    name: Literal["QulacsSimulationRequest"] = "QulacsSimulationRequest"

    circuits: list[CircuitModel]
    kwargs: QulacsProcessKwargs = QulacsProcessKwargs()
    config: QulacsConfig = QulacsConfig()
