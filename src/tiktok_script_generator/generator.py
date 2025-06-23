"""Simple TikTok script generator."""

from typing import Iterable

from .brand_voice import BrandVoice, apply_voice
from .hooks import apply_hooks, Hook


def generate_script(points: Iterable[str], voice: BrandVoice, hooks: Iterable[Hook] | None = None) -> str:
    """Generate a TikTok script from bullet points and a brand voice."""
    script = " ".join(points)
    script = apply_voice(script, voice)
    return apply_hooks(script, hooks or [])

