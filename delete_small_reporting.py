from pathlib import Path

root = Path(r"\Code\DEMO files\Dataform Demo\definitions\reporting\power_bi")
deleted = []
for path in root.iterdir():
    if path.is_file():
        try:
            with path.open("r", encoding="utf-8") as handle:
                line_count = sum(1 for _ in handle)
        except Exception:
            continue
        if line_count <= 100:
            path.unlink()
            deleted.append(path.name)

print(f"deleted {len(deleted)} files")
for name in deleted:
    print(name)
