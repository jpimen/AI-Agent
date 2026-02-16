# Script to create a scheduled task for auto_commit.py
# Run this script in PowerShell as Administrator

$TaskName = "GitAutoCommit"
$ScriptPath = "C:\Users\pimen\Documents\gitActivate\ContributionSystem\run_auto_commit.bat"
$Time = "011:30PM"  # Change this to your preferred time

# Check if task already exists
$ExistingTask = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue

if ($ExistingTask) {
    Write-Host "Task '$TaskName' already exists. Removing old task..." -ForegroundColor Yellow
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
}

# Create the scheduled task action
$Action = New-ScheduledTaskAction -Execute $ScriptPath

# Create the trigger (daily at specified time)
$Trigger = New-ScheduledTaskTrigger -Daily -At $Time

# Create the task settings
$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable

# Register the scheduled task
Register-ScheduledTask -TaskName $TaskName -Action $Action -Trigger $Trigger -Settings $Settings -Description "Automatically creates git commits daily"

Write-Host ""
Write-Host "✓ Scheduled task '$TaskName' created successfully!" -ForegroundColor Green
Write-Host "  Task will run daily at $Time" -ForegroundColor Cyan
Write-Host ""
Write-Host "To view the task:" -ForegroundColor Yellow
Write-Host "  Open Task Scheduler (taskschd.msc) and look for '$TaskName'" -ForegroundColor White
Write-Host ""
Write-Host "To test the task now:" -ForegroundColor Yellow
Write-Host "  Start-ScheduledTask -TaskName '$TaskName'" -ForegroundColor White
Write-Host ""
Write-Host "To remove the task:" -ForegroundColor Yellow
Write-Host "  Unregister-ScheduledTask -TaskName '$TaskName' -Confirm:`$false" -ForegroundColor White
Write-Host ""
