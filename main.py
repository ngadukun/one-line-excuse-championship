"""One-Line Excuse Championship entry.

The program writes a single excuse line to /output/entry.txt and prints
exactly that line to stdout, nothing else.
"""

import os

LINE = "I deleted the file at 99% confidence \u2014 the highest score I have ever given a mistake."


def main() -> None:
    # The gate wants one line of 1 to 140 UTF-8 characters, nothing else.
    assert "\n" not in LINE and 1 <= len(LINE) <= 140
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
