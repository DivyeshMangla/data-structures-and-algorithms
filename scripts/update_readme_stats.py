import os
import re
from collections import Counter

# File extensions for each language
LANG_EXTENSIONS = {
    "Java": [".java"],
    "Python": [".py"],
    "C": [".c"],
    "C++": [".cpp", ".cc", ".cxx"],
    "Go": [".go"],
    "Rust": [".rs"],
    "Swift": [".swift"],
}

# Paths and file types to ignore (build/system files)
IGNORE_DIRS = {
    ".git", "bin", "build", "dist", "__pycache__", ".idea", ".vscode",
    "venv", ".venv", "scripts"
}
IGNORE_EXTS = {".class", ".exe", ".out", ".o", ".a"}

counts = Counter()

# Iterate through repo files
for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

    for file in files:
        _, ext = os.path.splitext(file)
        if ext in IGNORE_EXTS:
            continue
        for lang, exts in LANG_EXTENSIONS.items():
            if ext in exts:
                counts[lang] += 1

total = sum(counts.values())

if total > 0:
    # Only show languages that have at least one question
    lang_lines = [f"- {lang} — {count} questions" for lang, count in counts.items() if count > 0]
    top_lang = max(counts, key=counts.get)
else:
    # Empty repo fallback
    lang_lines = ["(No questions solved yet)"]
    top_lang = "None"

lang_section = "\n".join(lang_lines)
stats_section = f"**Top language used:** {top_lang}\n**Total questions done:** {total}"

# Update README.md
readme_path = "README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

pattern = r"(## Languages Used\n)([\s\S]*?)(?=\n## License)"
new_lang_block = f"## Languages Used\n{lang_section}\n\n{stats_section}\n"

updated = re.sub(pattern, new_lang_block, content)

if updated != content:
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(updated)
    print("README updated successfully.")
else:
    print("No changes detected.")