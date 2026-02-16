import os
import random
import subprocess
from datetime import datetime
import time

# Configuration
REPO_PATH = "C:\\Users\\pimen\\Documents\\gitActivate"
MIN_COMMITS = 90
MAX_COMMITS = 100
AUTO_PUSH = True  # Set to True for automatic push, False to ask

# File to modify for commits
COMMIT_FILE = "md.md"

def run_git_command(command):
    """Execute a git command in the repository"""
    try:
        result = subprocess.run(
            command,
            cwd=REPO_PATH,
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        print(f"Error output: {e.stderr}")
        return None

def generate_commit_message():
    """Generate a unique commit message"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    messages = [
        f"Update documentation - {timestamp}",
        f"Code improvements - {timestamp}",
        f"Bug fixes and enhancements - {timestamp}",
        f"Feature updates - {timestamp}",
        f"Refactoring - {timestamp}",
        f"Performance improvements - {timestamp}",
        f"Maintenance update - {timestamp}"
    ]
    return random.choice(messages)

def modify_file():
    """Modify the tracking file to create a change"""
    file_path = os.path.join(REPO_PATH, COMMIT_FILE)
    
    # Create file if it doesn't exist
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write("# Auto-generated commits log\n\n")
    
    # Append a timestamp entry
    with open(file_path, 'a') as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"- Commit at {timestamp}\n")

def make_commit():
    """Create a single commit"""
    try:
        # Modify the file
        modify_file()
        
        # Stage the changes
        run_git_command(f"git add {COMMIT_FILE}")
        
        # Create commit
        commit_msg = generate_commit_message()
        run_git_command(f'git commit -m "{commit_msg}"')
        
        print(f"✓ Created commit: {commit_msg}")
        return True
    except Exception as e:
        print(f"✗ Failed to create commit: {e}")
        return False

def auto_commit():
    """Main function to create multiple commits"""
    print("=" * 50)
    print("Auto Commit Script Started")
    print("=" * 50)
    print(f"Repository: {REPO_PATH}")
    print(f"Target file: {COMMIT_FILE}")
    
    # Verify repository exists
    if not os.path.exists(REPO_PATH):
        print(f"Error: Repository path does not exist: {REPO_PATH}")
        return
    
    # Check if it's a git repository
    if not os.path.exists(os.path.join(REPO_PATH, ".git")):
        print("Error: Not a git repository. Run 'git init' first.")
        return
    
    # Generate random number of commits
    num_commits = random.randint(MIN_COMMITS, MAX_COMMITS)
    print(f"\nGenerating {num_commits} commits...")
    print("-" * 50)
    
    success_count = 0
    for i in range(num_commits):
        if make_commit():
            success_count += 1
        
        # Small delay between commits (optional)
        if i < num_commits - 1:
            time.sleep(0.5)
    
    print("-" * 50)
    print(f"\nCompleted: {success_count}/{num_commits} commits created")
    
    # Push to remote
    print("\n" + "=" * 50)
    if AUTO_PUSH:
        print("Pushing to remote...")
        result = run_git_command("git push")
        if result is not None:
            print("✓ Successfully pushed to remote")
        else:
            print("✗ Failed to push to remote")
    else:
        push = input("Do you want to push commits to remote? (y/n): ").lower()
        if push == 'y':
            print("Pushing to remote...")
            result = run_git_command("git push")
            if result is not None:
                print("✓ Successfully pushed to remote")
            else:
                print("✗ Failed to push to remote")
    
    print("=" * 50)
    print("Auto Commit Script Finished")
    print("=" * 50)

if __name__ == "__main__":
    auto_commit()

#push and commit automatically