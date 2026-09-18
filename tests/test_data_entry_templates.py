#!/usr/bin/env python3
"""Guard the data-entry/ CSV templates (headers are the import contract).

Usage:
    python3 tests/test_data_entry_templates.py
"""

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENTRY = ROOT / "data-entry"

EXPECTED = {
    "1-kategori.csv": ["id", "Nama"],
    "2-penceramah.csv": ["id", "Nama", "Penerangan"],
    "3-masjids.csv": ["id", "Nama", "Mukim", "Negeri", "Alamat", "Latitud",
                      "Longitud", "Kenalan", "Laman web"],
    "4-acara.csv": ["id", "Tajuk", "Masjid", "Tarikh", "Mula", "Tamat",
                    "Penceramah", "Kategori", "Lokasi", "Penerangan", "Status",
                    "Jenis ulangan", "Hari ulangan", "Mula ulangan",
                    "Tamat ulangan", "Pengecualian"],
}


def read_header(name):
    path = ENTRY / name
    assert path.is_file(), f"{name} missing from data-entry/"
    with open(path, "r", encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.reader(fh))
    assert rows, f"{name} is empty"
    return rows[0]


def test_templates_present_and_headers_exact():
    for name, header in EXPECTED.items():
        assert read_header(name) == header, f"{name} header drifted: {read_header(name)!r}"


def test_config_wires_all_templates():
    import json
    config = json.loads((ENTRY / "config.json").read_text(encoding="utf-8"))
    sources = config.get("sources", {})
    wired = {s.get("file") for s in sources.values() if isinstance(s, dict)}
    for name in EXPECTED:
        assert name in wired, f"{name} not wired in config.json"


def test_headers_covered_by_config_columns():
    import json
    config = json.loads((ENTRY / "config.json").read_text(encoding="utf-8"))
    sources = config.get("sources", {})
    by_file = {s["file"]: s for s in sources.values() if isinstance(s, dict)}
    for name, header in EXPECTED.items():
        src = by_file.get(name)
        assert src is not None, f"{name} not wired in config.json"
        mapped = set(src.get("columns", {}))
        assert set(header) == mapped, f"{name}: header/config columns mismatch"


def main():
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    failed = 0
    for test in tests:
        try:
            test()
            print(f"PASS {test.__name__}")
        except AssertionError as exc:
            failed += 1
            print(f"FAIL {test.__name__}: {exc}")
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
