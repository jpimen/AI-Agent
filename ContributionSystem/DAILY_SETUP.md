# Daily Auto Commit Setup - Quick Guide

## ✅ Changes Made
- **AUTO_PUSH = True** - Script now pushes automatically without asking
- Created batch file for easy scheduling
- Created PowerShell script for automatic Task Scheduler setup

## 🚀 Setup Daily Automation (2 Minutes)

### Option 1: Automatic Setup (Recommended)

**Run this in PowerShell as Administrator:**
```powershell
cd C:\dev\autogenerate\gitActivate\ContributionSystem
.\setup_daily_task.ps1
```

This will automatically create a scheduled task that runs every day at 9 AM.

### Option 2: Manual Setup

1. **Open Task Scheduler:**
   - Press `Win + R`, type `taskschd.msc`, press Enter

2. **Create Basic Task:**
   - Click "Create Basic Task" on the right
   - Name: `GitAutoCommit`
   - Description: `Daily git commits`

3. **Set Trigger:**
   - Choose "Daily"
   - Set your preferred time (e.g., 9:00 AM)
   - Click Next

4. **Set Action:**
   - Choose "Start a program"
   - Program/script: `C:\Users\pimen\Documents\run_auto_commit.bat`
   - Click Next and Finish

## ⚙️ Configuration

Edit `auto_commit.py` to customize:

```python
REPO_PATH = "C:\Users\pimen\Documents/gitActivate"  # Your repo path
MIN_COMMITS = 10    # Minimum commits per run
MAX_COMMITS = 20    # Maximum commits per run
AUTO_PUSH = True    # Automatic push (True/False)
```

## 🧪 Test It Now

Run manually to test:
```powershell
cd C:\Users\pimen\Documents
python auto_commit.py
```

Or run the scheduled task immediately:
```powershell
Start-ScheduledTask -TaskName "GitAutoCommit"
```

## 📋 Important Notes

✅ Make sure you have:
- Git remote configured: `git remote -v`
- Git credentials saved or SSH keys set up
- Python in system PATH

✅ To change the daily time:
- Edit line 5 in `setup_daily_task.ps1`: `$Time = "09:00AM"`
- Run the setup script again

## 🔍 Verify Setup

Check if task is scheduled:
```powershell
Get-ScheduledTask -TaskName "GitAutoCommit"
```

View task history:
- Open Task Scheduler → Task Scheduler Library → Find "GitAutoCommit" → History tab

## 🛑 Remove Automation

If you want to stop daily automation:
```powershell
Unregister-ScheduledTask -TaskName "GitAutoCommit" -Confirm:$false
```

## 📝 What Happens Daily

1. Script runs at scheduled time
2. Generates 10-20 commits
3. Automatically pushes to remote
4. Logs completion
5. Exits

**No user interaction needed!**
