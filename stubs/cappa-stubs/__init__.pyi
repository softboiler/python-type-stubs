from typing import Any

from cappa.base import command as command
from cappa.base import invoke as invoke

def __getattr__(name: str) -> Any: ...  # pyright: ignore[reportIncompleteStub]

