#!/usr/bin/env python3
"""
reset_git_history.py

Replace the entire repo history with a single commit of the current working tree.

Default mode ("orphan"):
  - Creates an orphan commit and deletes all other local branches/tags.
  - Expires reflogs and runs aggressive GC.

Alternative mode ("hard"):
  - Deletes .git, runs `git init`, and commits everything as a fresh repo.

Optional:
  - --push to force-push the new single-commit history to a remote (default: origin)
  - --wipe-remote to delete all other remote branches/tags (DANGEROUS)

Examples:
  # Dry run only (shows what would happen)
  python reset_git_history.py

  # Do it locally (orphan mode), keep branch 'main'
  python reset_git_history.py --force

  # Do it and force-push to origin/main
  python reset_git_history.py --force --push

  # Nuke .git and re-init (hard mode), then push and wipe remote branches/tags
  python reset_git_history.py --force --mode hard --push --wipe-remote --branch main
"""

import argparse
import os
import shutil
import stat
import subprocess
import sys

def run(cmd, check=True, capture=False):
    if capture:
        return subprocess.check_output(cmd, text=True).strip()
    subprocess.run(cmd, check=check)

def git(*args, capture=False, check=True):
    return run(["git", *args], check=check, capture=capture)

def ensure_repo_or_cwd_root():
    try:
        inside = git("rev-parse", "--is-inside-work-tree", capture=True)
    except subprocess.CalledProcessError:
        inside = "false"
    if inside != "true":
        print("Not inside a Git repository. Proceeding in current directory (hard mode will still work).")

    # If in a repo, cd to top-level so branch/tag ops hit the root
    if inside == "true":
        toplevel = git("rev-parse", "--show-toplevel", capture=True)
        os.chdir(toplevel)

def get_remote_url(name):
    try:
        return git("remote", "get-url", name, capture=True)
    except subprocess.CalledProcessError:
        return None

def list_local_branches():
    out = git("for-each-ref", "--format=%(refname:short)", "refs/heads", capture=True)
    return [b for b in out.splitlines() if b.strip()] if out else []

def list_local_tags():
    out = git("tag", capture=True)
    return [t for t in out.splitlines() if t.strip()] if out else []

def list_remote_heads(remote):
    try:
        out = git("ls-remote", "--heads", remote, capture=True)
        names = []
        for line in out.splitlines():
            parts = line.split("\t")
            if len(parts) == 2 and parts[1].startswith("refs/heads/"):
                names.append(parts[1].split("refs/heads/")[1])
        return names
    except subprocess.CalledProcessError:
        return []

def list_remote_tags(remote):
    try:
        out = git("ls-remote", "--tags", remote, capture=True)
        names = []
        for line in out.splitlines():
            parts = line.split("\t")
            if len(parts) == 2 and parts[1].startswith("refs/tags/"):
                tagref = parts[1].split("refs/tags/")[1]
                # strip ^{} deref suffix
                tagref = tagref.replace("^{}", "")
                names.append(tagref)
        return sorted(set(names))
    except subprocess.CalledProcessError:
        return []

def orphan_reinit(target_branch, message):
    print(f"[orphan] Creating orphan commit on temporary branch...")
    git("checkout", "--orphan", "_reinit_tmp")

    # Reset index but keep working tree as-is
    try:
        git("rm", "-rf", "--cached", ".")
    except subprocess.CalledProcessError:
        pass  # fine if nothing is cached yet

    git("add", "-A")
    git("commit", "-m", message)

    # Delete all other local branches (except current)
    branches = [b for b in list_local_branches() if b != "_reinit_tmp"]
    for b in branches:
        print(f"[orphan] Deleting local branch: {b}")
        git("branch", "-D", b)

    # Delete all local tags
    for t in list_local_tags():
        print(f"[orphan] Deleting local tag: {t}")
        git("tag", "-d", t)

    print(f"[orphan] Renaming _reinit_tmp -> {target_branch}")
    git("branch", "-M", target_branch)

    print("[orphan] Expiring reflogs and running aggressive GC...")
    git("reflog", "expire", "--expire=now", "--all")
    git("gc", "--prune=now", "--aggressive")

def handle_readonly_remove(func, path, exc):
    # Windows may mark files as read-only in .git; clear and retry
    try:
        os.chmod(path, stat.S_IWRITE)
        func(path)
    except Exception:
        raise

def hard_reinit(target_branch, message, origin_url):
    print("[hard] Deleting .git directory and reinitializing...")
    if os.path.isdir(".git"):
        shutil.rmtree(".git", onerror=handle_readonly_remove)

    # Re-init and commit everything
    try:
        # If your Git supports -b, this sets the initial branch name directly
        run(["git", "init", "-b", target_branch])
    except subprocess.CalledProcessError:
        run(["git", "init"])
        # Create initial commit then rename branch
        run(["git", "add", "-A"])
        run(["git", "commit", "-m", message])
        run(["git", "branch", "-M", target_branch])
    else:
        run(["git", "add", "-A"])
        run(["git", "commit", "-m", message])

    if origin_url:
        print(f"[hard] Restoring remote 'origin' -> {origin_url}")
        run(["git", "remote", "add", "origin", origin_url])

def do_push(remote, branch, wipe_remote):
    print(f"[push] Force-pushing {branch} to {remote}...")
    run(["git", "push", "-f", remote, f"{branch}:{branch}"])

    if wipe_remote:
        print("[push] Wiping other remote branches/tags (DANGEROUS)...")
        remote_heads = [b for b in list_remote_heads(remote) if b != branch]
        for b in remote_heads:
            print(f"[push] Deleting remote branch: {b}")
            # Ignore failure (branch may be protected)
            run(["git", "push", remote, "--delete", b], check=False)

        remote_tags = list_remote_tags(remote)
        for t in remote_tags:
            print(f"[push] Deleting remote tag: {t}")
            run(["git", "push", remote, "--delete", t], check=False)

def main():
    ap = argparse.ArgumentParser(description="Reset Git history to a single commit of the current working tree.")
    ap.add_argument("--branch", default="main", help="Target branch name to keep (default: main)")
    ap.add_argument("--commit-message", default="Initial commit (history reset to current state)",
                    help="Commit message for the new single commit")
    ap.add_argument("--mode", choices=["orphan", "hard"], default="orphan",
                    help="orphan = rewrite in-place; hard = delete .git and re-init")
    ap.add_argument("--push", action="store_true", help="Force-push the result to the remote")
    ap.add_argument("--remote", default="origin", help="Remote name to push to (default: origin)")
    ap.add_argument("--wipe-remote", action="store_true",
                    help="Also delete ALL other remote branches/tags (implies very destructive)")
    ap.add_argument("--force", action="store_true",
                    help="Actually perform changes. Without this, the script only prints what it would do.")
    args = ap.parse_args()

    ensure_repo_or_cwd_root()
    origin_url = get_remote_url(args.remote)

    print("Planned actions:")
    print(f"  Mode           : {args.mode}")
    print(f"  Target branch  : {args.branch}")
    print(f"  Commit message : {args.commit_message!r}")
    print(f"  Remote         : {args.remote} ({origin_url or 'no remote'})")
    print(f"  Force-push     : {'yes' if args.push else 'no'}")
    print(f"  Wipe remote    : {'yes' if args.wipe_remote else 'no'}")
    if not args.force:
        print("\n-- DRY RUN -- Add --force to actually perform these actions.")
        return

    try:
        if args.mode == "orphan":
            orphan_reinit(args.branch, args.commit_message)
        else:
            hard_reinit(args.branch, args.commit_message, origin_url)

        if args.push:
            do_push(args.remote, args.branch, args.wipe_remote)

        print("\nDone.")
        if args.push:
            print(f"Remote {args.remote}/{args.branch} now points to a single commit.")
        else:
            print(f"Local branch '{args.branch}' now has a single commit. Use --push to update the remote.")
    except subprocess.CalledProcessError as e:
        print(f"\nERROR: Command failed: {' '.join(e.cmd)}")
        sys.exit(e.returncode)

if __name__ == "__main__":
    main()
