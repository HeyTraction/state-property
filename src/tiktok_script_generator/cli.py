"""Command line interface for TikTok script generation."""

import argparse
from typing import List

from .brand_voice import BrandVoice
from .generator import generate_script


def parse_args(args: List[str] | None = None) -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Generate TikTok scripts from bullet points")
    parser.add_argument("points", nargs="+", help="Bullet points for the script")
    parser.add_argument("--voice", choices=[v.value for v in BrandVoice], default=BrandVoice.CASUAL.value, help="Brand voice style")
    return parser.parse_args(args)


def main(argv: List[str] | None = None) -> None:
    """Entry point for the CLI."""
    args = parse_args(argv)
    voice = BrandVoice(args.voice)
    script = generate_script(args.points, voice)
    print(script)


if __name__ == "__main__":  # pragma: no cover - manual execution
    main()

