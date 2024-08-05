import typing
from collections.abc import Callable, Sequence
from typing import Any, TypeVar, dataclass_transform, overload

from cappa.arg import Arg
from cappa.command import Command
from cappa.help import HelpFormatable
from cappa.invoke import Dep
from cappa.output import Output
from rich.theme import Theme

_T = TypeVar("_T")

def __getattr__(name: str) -> Any: ...  # pyright: ignore[reportIncompleteStub]
def invoke(
    obj: type | Command[Any],
    *,
    deps: Sequence[Callable[..., Any]]
    | typing.Mapping[Callable[..., Any], Dep[Any] | typing.Any]
    | None = None,
    argv: list[str] | None = None,
    backend: Callable[..., Any] | None = None,
    color: bool = True,
    version: str | Arg[Any] | None = None,
    help: bool | Arg[Any] = True,  # noqa: A002
    completion: bool | Arg[Any] = True,
    theme: Theme | None = None,
    output: Output | None = None,
    help_formatter: HelpFormatable | None = None,
): ...
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
