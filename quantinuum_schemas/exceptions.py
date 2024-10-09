"""Custom exceptions."""


class OptionalDependencyError(Exception):
    """Exception for import error"""

    def __init__(  # type: ignore
        self,
        *args,
        msg="An optional dependency is required for this action",
        **kwargs,
    ) -> None:
        super().__init__(*args, msg, **kwargs)
