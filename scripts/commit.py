import subprocess
from pathlib import Path

def run_git_command(*args):
    result = subprocess.run(["git", *args], capture_output=True, text=True)
    return result.stdout.strip().splitlines()

def main():
    subprocess.run(["git", "pull"])
    
    untracked = run_git_command("ls-files", "--others", "--exclude-standard")
    modified = run_git_command("ls-files", "--modified")
    staged = run_git_command("diff", "--name-only", "--cached")

    all_files = set(untracked + modified + staged)
    if not all_files:
        return

    if len(all_files) == 1:
        f = list(all_files)[0]
        path = Path(f)
        parts = path.parts
        if len(parts) >= 3:
            platform = parts[0]
            language = parts[1]
            problem_name = path.stem
            action = "solve" if f in untracked else "update"
            msg = f"{platform}: {action} {problem_name} in {language}"
        else:
            msg = "feat: update solution"
    else:
        msg = "feat: solved or updated multiple problems across languages"

    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", msg])
    subprocess.run(["git", "push"])

    print(msg)

if __name__ == "__main__":
    main()