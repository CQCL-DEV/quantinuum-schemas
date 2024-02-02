"""Aggregate models exposed at the top level."""

from typing import Literal, Union

from pydantic import BaseModel, Field, RootModel
from pytket.passes import BasePass

from quantinuum_schemas.aer import (
    AerCompilationRequest,
    AerConfig,
    AerSimulationRequest,
)
from quantinuum_schemas.qulacs import (
    QulacsCompilationRequest,
    QulacsConfig,
    QulacsSimulationRequest,
)

CompilationRequestData = AerCompilationRequest | QulacsCompilationRequest
SimulationRequestData = AerSimulationRequest | QulacsSimulationRequest
BackendConfig = AerConfig | QulacsConfig


class CompilationRequest(RootModel):
    """Root model for compilation requests."""

    root: CompilationRequestData = Field(..., discriminator="name")


class SimulationRequest(RootModel):
    """Root model for simulation requests."""

    root: SimulationRequestData = Field(..., discriminator="name")
