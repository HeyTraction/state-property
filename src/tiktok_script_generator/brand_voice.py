"""Utilities for representing and applying brand voice styles."""

from enum import Enum

class BrandVoice(Enum):
    """Enumeration of possible brand voices."""

    CASUAL = "casual"
    ENTHUSIASTIC = "enthusiastic"
    PROFESSIONAL = "professional"


def apply_voice(text: str, voice: BrandVoice) -> str:
    """Apply the chosen brand voice to the text.

    Parameters
    ----------
    text:
        The text to transform.
    voice:
        The desired brand voice.

    Returns
    -------
    str
        Modified text in the given voice.
    """

    if voice is BrandVoice.CASUAL:
        return f"Hey! {text}"
    if voice is BrandVoice.ENTHUSIASTIC:
        return f"!!! {text} !!!"
    if voice is BrandVoice.PROFESSIONAL:
        return f"{text}."
    return text

