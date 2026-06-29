"""Generate the focused UTM values PowerPoint deck.

This reuses the same Markdown-to-PowerPoint generation code as the FY27 deck,
with a different source file, output file, and footer label.
"""

from pathlib import Path

import generate_fy27_deck as deck


deck.SOURCE = Path("UTM Values Training Deck.md")
deck.OUTPUT = Path("UTM Values Training Deck.pptx")
deck.FOOTER_TITLE = "UTM Values Training"


if __name__ == "__main__":
    deck.build_deck()
