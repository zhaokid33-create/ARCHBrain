# 2026-04-13 Hermes Discord Gateway 接入记录

tags: [系统配置, Hermes, Discord]
updated: 2026-04-14
sources: [claude-code session]

## 最终状态
Discord gateway 已成功连接。

## 配置信息
- `DISCORD_BOT_TOKEN` — 已写入 `C:\Users\kid\.hermes\.env`
- `DISCORD_ALLOWED_USERS=1493287347591053455`
- `DISCORD_PROXY=http://127.0.0.1:1080` — 国内网络需要代理

## 启动命令
```powershell
cd E:\codex\hermes; python -m gateway.run
```
注意：`hermes gateway` 在 Windows 上静默退出，不可用。

## 修复的 Bug

### gateway/status.py — os.kill WinError 87
Windows + Python 3.14 上 `os.kill(pid, 0)` 抛 `OSError: [WinError 87]`。
修复：两处 `except (ProcessLookupError, PermissionError)` 改为 `except OSError`
- 第 307 行：`acquire_scoped_lock()` 里的锁检查
- 第 410 行：`get_running_pid()` 里的 PID 存活检查

## 遗留警告（不影响功能）
- `UnicodeEncodeError: gbk` — 设置 `PYTHONIOENCODING=utf-8` 解决
- `Opus/PyNaCl not found` — 语音功能缺依赖，文字聊天不受影响
- `slash command limit reached (100)` — Discord 斜杠命令上限，不影响主功能
