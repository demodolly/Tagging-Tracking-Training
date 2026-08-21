# Tagging-Tracking-Training
This is a repository with Powerpoints, Excel and MD files that will help me prepare my Tagging and Tracking Training Documention

## Tagging & Tracking Overview — FY27 (primary training deck)

- Editable PowerPoint: `Tagging & Tracking Overview - FY27.pptx`
- Editable source outline: `Tagging & Tracking Overview - FY27.md`
- Update script (preserves Cisco template): `update_fy27_overview_deck.py`
- Editorial review notes: `Tagging & Tracking Overview - FY27 - Editorial Guide.md`

To apply narrative fixes from the Markdown outline to the template deck:

```bash
python3 update_fy27_overview_deck.py
```

The script backs up the original deck to `Tagging & Tracking Overview - FY27.backup.pptx` on first run.

## Tagging & Tracking Overview — FY27 Semi Final (primary stakeholder deck)

- Editable PowerPoint: `Tagging & Tracking Overview - FY27 - Semi Final.pptx`
- Purpose & Outcome review: `Tagging & Tracking Overview - FY27 - Semi Final - Purpose Outcome Review.md`
- Update script (preserves Cisco template): `update_semi_final_deck.py`

To re-apply Purpose/Outcome alignment patches:

```bash
python3 update_semi_final_deck.py
```

Backup: `Tagging & Tracking Overview - FY27 - Semi Final.backup.pptx`

## FY27 training deck (repository-backed reference deck)

- Editable PowerPoint: `FY27 Tagging and Tracking Training Deck.pptx`
- Editable source outline: `FY27 Tagging and Tracking Training Deck.md`
- Generator script: `generate_fy27_deck.py`

To update the deck, edit the Markdown source and regenerate the PowerPoint:

```bash
python3 generate_fy27_deck.py
```

The generator requires `python-pptx` in the local Python environment.

## UTM values training deck

- Editable PowerPoint: `UTM Values Training Deck.pptx`
- Editable source outline: `UTM Values Training Deck.md`
- Generator script: `generate_utm_values_deck.py`

To update the focused UTM values deck, edit the Markdown source and regenerate the PowerPoint:

```bash
python3 generate_utm_values_deck.py
```
