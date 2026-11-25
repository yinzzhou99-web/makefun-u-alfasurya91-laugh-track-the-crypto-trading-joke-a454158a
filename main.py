"""Laugh Track: one crypto-trading joke to /output/entry.txt.

Stdlib only, no network, deterministic: identical bytes on every run.
The gate wants 1-200 UTF-8 characters; the joke below is 73.
"""
import os

JOKE = "I bought the dip, then the dip's dip, and now I own the entire staircase."


def main() -> None:
    if not 1 <= len(JOKE) <= 200:
        raise ValueError("joke must be 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    fd = os.open("/output/entry.txt", os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    try:
        os.write(fd, JOKE.encode("utf-8"))
    finally:
        os.close(fd)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
