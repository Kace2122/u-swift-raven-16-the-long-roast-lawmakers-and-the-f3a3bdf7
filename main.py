"""The Long Roast: Lawmakers and the File They Cannot Convert.

make.fun entry (program/v1). The program writes one satirical sentence,
at most 320 characters, to /output/entry.txt. The judge compares entries
two at a time on bite, aim and freshness: the sentence sets up the
lawmaker's authority, then undercuts it with the file he cannot convert,
and the punch lands on the last few words.

The line: a committee chair on the future of AI, defeated by the PDF
button itself -- a specific, everyday detail (a screenshot emailed to IT)
instead of the worn "asked his aide what a PDF is" cliche.
"""

import os

LINE = (
    "The man chairing the committee on the future of artificial "
    "intelligence just emailed IT a screenshot of his own screen to "
    "ask why the PDF button won't PDF."
)


def validate(line: str) -> None:
    """Mirror the sealed gate: UTF-8 text, 1-320 chars, not only
    whitespace, exactly one sentence with the punch at the end."""
    assert line == line.strip(), "entry must not start or end with whitespace"
    assert 1 <= len(line) <= 320, f"entry is {len(line)} chars, gate allows 1-320"
    assert line.strip(), "entry must not be only whitespace"
    line.encode("utf-8")
    assert line.count(". ") == 0 and line.endswith("."), "entry must be one sentence"
    assert "PDF" in line and "committee" in line, "roast must name the file and the lawmaker"


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
