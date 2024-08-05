from typing import Any

from cappa.base import command as command

def __getattr__(name: str) -> Any: ...  # pyright: ignore[reportIncompleteStub]

