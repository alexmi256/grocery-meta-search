# Development environment

How the interpreter and dependencies are pinned, and why. Read this
before changing the Python version or the OCR stack.

## The interpreter is capped at Python 3.12

The pipeline's OCR stack is the binding constraint. `rapidocr-
onnxruntime` (the OCR engine wrapper used by every OCR store) declares
`requires-python = "<3.13,>=3.6"` — and it has done so for **every**
release up to and including the current 1.4.4. There is no version of
`rapidocr-onnxruntime` that installs on 3.13 or newer.

So although the rest of the stack would happily run on a newer
interpreter — `onnxruntime` (its transitive dependency) already ships
`cp314` wheels, and `pymupdf`/`numpy` are fine — a single
`pip install -r requirements.txt` cannot resolve on 3.13+.

| Python | Status | Reason |
|---|---|---|
| 3.11 | supported | floor in `pyproject.toml` |
| **3.12** | **pinned — highest usable** | `rapidocr-onnxruntime <3.13` |
| 3.13+ | blocked | `rapidocr-onnxruntime` has no compatible release |

The system interpreter on this machine is 3.14, which is why the project
uses **pyenv** to provide a 3.12 interpreter rather than the system one.

## Pinned version

`pyenv` + `.python-version` pin the project to **3.12.15**, the latest
3.12 patch release. The pin lives in the repo so every checkout, and
`pyenv` itself when you `cd` into the directory, selects it
automatically.

The pin names an exact patch, so the interpreter must be installed
first (step 2 below). If it is not, `pyenv` prints a warning and falls
back to the system interpreter — the unsupported 3.14 here — and the
dependency install then fails. Run `pyenv install 3.12.15` before
anything else.

`pyproject.toml` records the same ceiling in metadata:

```toml
requires-python = ">=3.11,<3.13"
```

This governs installation of *the project itself* (`pip install .` /
`-e .`), where a 3.13+ interpreter is rejected with a clear message.
It does **not** apply to the documented `pip install -r
requirements-dev.txt` flow: `pip` never reads the local
`pyproject.toml` when installing from a requirements file, so on 3.13+
that path still fails — inside the `rapidocr-onnxruntime` resolution,
the very error the metadata is meant to avoid. Treat the metadata as
the declared contract for a packaged install; the practical guard for
contributors is the `.python-version` pin plus the `pyenv install`
step below.

## One-time setup

```bash
# 1. pyenv itself (already installed on this machine)
#    Ensure pyenv is initialised for your shell — see "Shell setup" below.

# 2. Install the pinned interpreter (compiles from source, ~a few minutes)
pyenv install 3.12.15

# 3. From the repo root, pyenv reads .python-version and selects 3.12.15
cd /path/to/grocery-meta-search
python --version   # -> Python 3.12.15

# 4. Create the virtualenv and install runtime + dev tools
python -m venv .venv
.venv/bin/pip install -r requirements-dev.txt
```

`.venv/` is git-ignored; `.python-version` is tracked by git (not
ignored).

## Shell setup

`pyenv` needs its shims on `PATH` so that `python` resolves through it.
Add the following to `~/.bashrc` (or the equivalent for your shell) once:

```bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init - bash)"
```

With that in place, `python` inside the repo reports 3.12.15 via the
committed `.python-version`, and any other directory is unaffected.

## Running the gates

The three gates in `AGENTS.md` run against the `.venv` interpreter:

```bash
.venv/bin/ruff check src tests
.venv/bin/mypy src
.venv/bin/python -m pytest tests/ -q
```

Keep `ruff`'s `target-version` and `mypy`'s `python_version` at `py311`:
the interpreter is 3.12, but 3.11 remains the supported floor, so the
linters must not assume 3.12-only syntax.

## When to revisit this pin

Re-check the cap whenever the OCR stack moves — a new
`rapidocr-onnxruntime` release, a switch to the unified `rapidocr`
package, or a direct `onnxruntime` integration. If a release drops the
`<3.13` marker and ships 3.13+ wheels:

1. Install the new interpreter (`pyenv install 3.13.x`).
2. Bump `.python-version` and the `requires-python` ceiling.
3. Re-run all three gates on a clean venv, plus the two slow OCR
   fixture tests (`tests/test_pa_chalkboard.py`,
   `tests/test_frutta_red_grid.py`) that iterate against a new
   `onnxruntime`.
4. Update this file, `README.md` and `requirements.txt`.

## System packages

Two things are *not* pip packages:

- **Tesseract 5** — a system binary the OCR pipeline needs on `PATH`
  (RapidOCR handles detection, Tesseract the recognition).
- **Build toolchain** — building CPython from source needs `gcc`,
  `make`, and the `-dev` headers for OpenSSL, zlib, bz2, readline,
  sqlite3, libffi, lzma, ncurses and (optional) tk/gdbm. All present on
  this machine.
