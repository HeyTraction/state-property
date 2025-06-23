"""TikTok Script Generator package."""

from .brand_voice import BrandVoice, apply_voice
from .generator import generate_script
from .hooks import Hook, apply_hooks

__all__ = [
    "BrandVoice",
    "apply_voice",
    "generate_script",
    "Hook",
    "apply_hooks",
]

