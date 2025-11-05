import subprocess
from pathlib import Path

def run_git_command(*args):
    result = subprocess.run(["git", *args], capture_output=True, text=True)
    return result.stdout.strip().splitlines()

def file_exists_in_remote(filename):
    """Check if file exists in the remote repository"""
    result = subprocess.run(
        ["git", "ls-tree", "-r", "origin/main", "--name-only"],
        capture_output=True,
        text=True
    )
    remote_files = result.stdout.strip().splitlines()
    return filename in remote_files

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

            # Check if file is truly new (not in remote)
            if f in untracked or not file_exists_in_remote(f):
                action = "solve"
            else:
                action = "update"

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