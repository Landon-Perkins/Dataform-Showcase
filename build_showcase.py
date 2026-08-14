from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
SOURCE_ROOT = REPO_ROOT / "definitions"
TARGET_ROOT = REPO_ROOT / "showcase"

# Replace environment- and project-specific labels with generic placeholders.
REPLACEMENTS = [
    ("demo_project", "example_project"),
    ("demo-project", "example-project"),
    ("demo_sources", "example_sources"),
    ("demo_staging", "example_staging"),
    ("demo_reporting", "example_reporting"),
    ("stakeholder@example.com", "team@example.com"),
    ("<demo>", "<example>"),
]


def sanitize_content(text: str) -> str:
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
    return text


def is_included(path: Path) -> bool:
    parts = set(path.parts)
    return path.suffix == ".sqlx" and "tests" not in parts


TARGET_ROOT.mkdir(parents=True, exist_ok=True)
files = [p for p in SOURCE_ROOT.rglob("*.sqlx") if is_included(p)]
files.sort()

for source_file in files:
    rel = source_file.relative_to(SOURCE_ROOT)
    target_file = TARGET_ROOT / rel
    target_file.parent.mkdir(parents=True, exist_ok=True)
    content = source_file.read_text(encoding="utf-8")
    target_file.write_text(sanitize_content(content), encoding="utf-8")

index_lines = [
    "# SQLX Showcase",
    "",
    "This directory contains sanitized copies of the SQLX transformations from the main Dataform repository.",
    "",
    "## Files",
    "",
]
for source_file in files:
    rel = source_file.relative_to(SOURCE_ROOT).as_posix()
    index_lines.append(f"- [{rel}]({rel})")

(TARGET_ROOT / "README.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")

print(f"Copied {len(files)} SQLX files into {TARGET_ROOT}")
print("Sample files:")
for p in files[:10]:
    print(" -", p.relative_to(SOURCE_ROOT).as_posix())
