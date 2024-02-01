"""Generael helper functions for Python typing."""
from typing import NoReturn


def assert_never(never: NoReturn) -> NoReturn:
    """Used to enforce exhaustiveness in a match statement.

    https://github.com/microsoft/pyright/issues/2569"""
    assert False, f"Unhandled type: f{never}"
