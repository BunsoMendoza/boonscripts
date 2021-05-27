from pathlib import Path
result = list(Path(".").rglob("file", '*'))
print(result)