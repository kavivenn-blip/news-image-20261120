"""news-image-20261120 entry runner.

Copies the pre-rendered entry image into the output directory.

The image is a deterministic 1024x1024 PNG rendered from render.html
(a static, self-contained page: system fonts only, no network, no
JavaScript). It is screenshotted once at build time with a headless
browser and stored in this repository as entry.png; two independent
screenshot runs produced byte-identical files.

This runner uses only the Python standard library. It reads the
MAKEFUN_OUTPUT_DIR environment variable when set and falls back to
/output, matching the harness convention.
"""

import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        print(f"entry.png not found next to {__file__}", file=sys.stderr)
        return 1

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    destination = out_dir / "entry.png"
    shutil.copyfile(source, destination)

    size = destination.stat().st_size
    print(f"wrote {destination} ({size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
