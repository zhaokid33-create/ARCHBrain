$action = New-ScheduledTaskAction -Execute "python.exe" -Argument "E:\codex\brain\compile_architecture.py"
$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Friday -At "18:00"
Register-ScheduledTask -TaskName "Architecture Weekly Compile" -Action $action -Trigger $trigger -Force
Write-Host "任务创建成功"
