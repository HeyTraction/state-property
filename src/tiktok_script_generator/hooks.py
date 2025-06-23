"""Hook utilities for post-processing generated scripts."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable


@dataclass
class Hook:
    """Represents a callable hook that modifies a script."""

    func: Callable[[str], str]

    def __call__(self, script: str) -> str:  # pragma: no cover - trivial
        return self.func(script)


def apply_hooks(script: str, hooks: Iterable[Hook]) -> str:
    """Apply hooks sequentially to the script."""
    for hook in hooks:
        script = hook(script)
    return script

