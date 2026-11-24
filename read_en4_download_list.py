#!/usr/bin/env python3
"""Unduh dan tampilkan isi daftar unduhan EN4 dari Met Office."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

URL = "https://www.metoffice.gov.uk/hadobs/en4/EN.4.2.2.analyses.g10.download-list.txt"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Baca daftar unduhan EN4 dari situs Met Office."
    )
    parser.add_argument(
        "--save",
        metavar="FILE",
        help="simpan salinan teks yang diunduh ke file lokal",
    )
    args = parser.parse_args()

    request = Request(URL, headers={"User-Agent": "Monitoring-Aceh-Waters/1.0"})
    try:
        with urlopen(request, timeout=30) as response:
            raw_text = response.read().decode("utf-8-sig", errors="replace")
    except (HTTPError, URLError, TimeoutError, OSError) as exc:
        print(f"Gagal membaca {URL}: {exc}", file=sys.stderr)
        return 1

    if args.save:
        try:
            Path(args.save).write_text(raw_text, encoding="utf-8")
        except OSError as exc:
            print(f"Gagal menyimpan file {args.save}: {exc}", file=sys.stderr)
            return 1
        print(f"Daftar berhasil disimpan ke {args.save}")

    # Tampilkan isi file sebagaimana diterima dari server.
    print(raw_text, end="" if raw_text.endswith("\n") else "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
