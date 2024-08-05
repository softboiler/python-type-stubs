from collections.abc import Callable
from typing import Any, TypeVar, dataclass_transform, overload

from cappa.help import HelpFormatable

def __getattr__(name: str) -> Any: ...  # pyright: ignore[reportIncompleteStub]

_T = TypeVar("_T")

@dataclass_transform()
@overload
def command(
    _cls: None = None,
    *,
    name: str | None = None,
    help: str | None = None,  # noqa: A002
    description: str | None = None,
    invoke: Callable[..., Any] | str | None = None,
    hidden: bool = False,
    default_short: bool = False,
    default_long: bool = False,
    deprecated: bool = False,
    help_formatter: HelpFormatable = ...,
) -> Callable[[type[_T]], type[_T]]: ...
@overload
def command(
    _cls: type[_T],
    *,
    name: str | None = None,
    help: str | None = None,  # noqa: A002
    description: str | None = None,
    invoke: Callable[..., Any] | str | None = None,
    hidden: bool = False,
    default_short: bool = False,
    default_long: bool = False,
    deprecated: bool = False,
    help_formatter: HelpFormatable = ...,
) -> type[_T]: ...
def command(
    _cls: type[_T] | None = None,
    *,
    name: str | None = None,
    help: str | None = None,  # noqa: A002
    description: str | None = None,
    invoke: Callable[..., Any] | str | None = None,
    hidden: bool = False,
    default_short: bool = False,
    default_long: bool = False,
    deprecated: bool = False,
    help_formatter: HelpFormatable = ...,
) -> type[_T] | Callable[[type[_T]], type[_T]]: ...
