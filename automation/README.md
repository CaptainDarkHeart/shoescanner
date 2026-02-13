# Shoe Scanner Automation

Fully automated shoe deal hunting with email notifications. Set it and forget it!

## Overview

This automation script:
- ✅ Runs the shoescanner skill automatically
- 📧 Emails you when new deals are found
- 🕐 Works with cron/Task Scheduler for weekly runs
- 📝 Logs all activity
- 🎯 Only emails when there are actual new deals (configurable)

## Quick Setup

### 1. Install Python Dependencies

The script uses only Python standard library - no extra dependencies needed!

```bash
# Verify Python 3.6+ is installed
python3 --version
```

### 2. Configure Email Settings

Copy the example config and fill in your details:

```bash
cd automation
cp automation_config.json.example automation_config.json
nano automation_config.json  # or use your preferred editor
```

**For Gmail users:**
1. Enable 2-factor authentication on your Google account
2. Generate an App Password: https://myaccount.google.com/apppasswords
3. Use the App Password (not your regular password) in the config

**Example Gmail config:**
```json
{
  "email": {
    "enabled": true,
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "smtp_user": "youremail@gmail.com",
    "smtp_password": "your-16-char-app-password",
    "from_address": "youremail@gmail.com",
    "to_address": "youremail@gmail.com",
    "subject": "🔥 New Shoe Deals Found!"
  }
}
```

**For Outlook/Hotmail users:**
```json
{
  "email": {
    "smtp_server": "smtp-mail.outlook.com",
    "smtp_port": 587,
    "smtp_user": "youremail@outlook.com",
    "smtp_password": "your-password",
    ...
  }
}
```

### 3. Test the Script

Run it manually first to make sure everything works:

```bash
python3 shoescanner_automation.py
```

You should see output like:
```
============================================================
Starting Shoe Scanner Automation
============================================================
Running shoescanner skill...
Skill execution completed
Found 2 new deal(s)
New deals detected, sending email notification...
Sending email to youremail@gmail.com...
Email sent successfully
Automation run complete
============================================================
```

### 4. Schedule It

#### On macOS/Linux (using cron)

Edit your crontab:
```bash
crontab -e
```

Add a line to run weekly (every Sunday at 9 AM):
```bash
0 9 * * 0 /usr/bin/python3 /Users/dantaylor/Claude/shoescanner/automation/shoescanner_automation.py
```

Or run it daily:
```bash
0 9 * * * /usr/bin/python3 /Users/dantaylor/Claude/shoescanner/automation/shoescanner_automation.py
```

**Tip:** Find your Python path with `which python3`

#### On Windows (using Task Scheduler)

1. Open Task Scheduler
2. Create Basic Task
3. Name: "Shoe Scanner Weekly"
4. Trigger: Weekly (choose day/time)
5. Action: Start a program
   - Program: `C:\Python\python.exe` (or your Python path)
   - Arguments: `C:\path\to\shoescanner\automation\shoescanner_automation.py`
6. Finish and test it

## Configuration Options

### Email Settings

| Setting | Description | Example |
|---------|-------------|---------|
| `enabled` | Enable/disable email | `true` |
| `smtp_server` | SMTP server address | `smtp.gmail.com` |
| `smtp_port` | SMTP port (usually 587) | `587` |
| `smtp_user` | Email username | `you@gmail.com` |
| `smtp_password` | Email password/app password | `abcd efgh ijkl mnop` |
| `from_address` | From email address | `you@gmail.com` |
| `to_address` | Recipient email address | `you@gmail.com` |
| `subject` | Email subject line | `New Shoe Deals!` |

### Behavior Settings

| Setting | Description | Default |
|---------|-------------|---------|
| `only_email_on_deals` | Only email when deals found | `true` |

If `only_email_on_deals` is `false`, you'll get an email every run (even with no deals) as a status update.

### Logging Settings

| Setting | Description | Default |
|---------|-------------|---------|
| `logging.enabled` | Enable logging | `true` |
| `logging.log_file` | Log file path | `~/.claude/skills/shoescanner/automation.log` |

## Environment Variables

You can also configure via environment variables (useful for security):

```bash
export SMTP_SERVER="smtp.gmail.com"
export SMTP_PORT="587"
export SMTP_USER="your-email@gmail.com"
export SMTP_PASSWORD="your-app-password"
export EMAIL_FROM="your-email@gmail.com"
export EMAIL_TO="your-email@gmail.com"
```

Then run without a config file - it will use environment variables.

## Email Format

You'll receive a beautiful HTML email with:
- 📊 Summary of deals found
- 💰 Price for each deal
- 🔗 Direct purchase links
- 🏪 Retailer information
- 📋 Your search criteria

Example:

```
🔥 New Shoe Deals Found!
Found 2 new deals for New Balance in size UK 12.5

#1. New Balance 9060 - Black/Grey
💰 £89.99
🏪 Retailer: End Clothing
📏 Size: UK 12.5 available
[View Deal →]

#2. New Balance 2002R - Navy/Silver
💰 £95.00
🏪 Retailer: Size?
📏 Size: UK 12.5 available
[View Deal →]
```

## Monitoring

### Check Logs

```bash
tail -f ~/.claude/skills/shoescanner/automation.log
```

### View Last Run

```bash
cat ~/.claude/skills/shoescanner/automation_state.json
```

This shows when the script last ran and what deals it has seen.

## Troubleshooting

### "Claude CLI not found"

The script needs the `claude` command to be available. Make sure:
1. Claude Code CLI is installed
2. `claude` is in your PATH
3. Try running `claude --version` manually

### "Skill execution failed"

1. Make sure the skill is configured: run `/shoescanner` manually first
2. Check that `~/.claude/skills/shoescanner/settings.json` exists
3. Verify `configured: true` in settings

### "Failed to send email"

**For Gmail:**
- Enable 2-factor authentication
- Use an App Password, not your regular password
- Allow "Less secure app access" (if not using 2FA)

**For Outlook:**
- Use your regular password
- May need to enable SMTP in account settings

**Test SMTP manually:**
```python
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('your-email@gmail.com', 'your-app-password')
server.quit()
```

### "Permission denied"

Make the script executable:
```bash
chmod +x shoescanner_automation.py
```

## Advanced Usage

### Multiple Email Recipients

Edit the config to send to multiple addresses:

```json
"to_address": "you@gmail.com, friend@example.com, deals@family.com"
```

### Custom Email Template

Edit the `format_email_body()` method in `shoescanner_automation.py` to customize the HTML.

### Webhook Integration

Instead of email, you can modify the script to:
- Post to Slack/Discord webhook
- Send push notification (Pushover, Pushbullet)
- Update a Google Sheet
- Trigger IFTTT/Zapier workflow

Example Slack webhook:
```python
import requests

def send_to_slack(deals):
    webhook_url = "https://hooks.slack.com/services/YOUR/WEBHOOK/URL"
    message = {"text": f"Found {len(deals)} new shoe deals!"}
    requests.post(webhook_url, json=message)
```

### Different Schedules

**Daily at 9 AM:**
```bash
0 9 * * * /usr/bin/python3 /path/to/shoescanner_automation.py
```

**Twice a week (Monday and Thursday at 8 AM):**
```bash
0 8 * * 1,4 /usr/bin/python3 /path/to/shoescanner_automation.py
```

**Every 6 hours:**
```bash
0 */6 * * * /usr/bin/python3 /path/to/shoescanner_automation.py
```

## Files

- `shoescanner_automation.py` - Main automation script
- `automation_config.json` - Your configuration (create from .example)
- `automation_config.json.example` - Example configuration
- `README.md` - This file
- `~/.claude/skills/shoescanner/automation.log` - Activity log
- `~/.claude/skills/shoescanner/automation_state.json` - Last run state

## Security Notes

⚠️ **Important Security Tips:**

1. **Never commit `automation_config.json` to git** - it contains passwords
2. Use App Passwords for Gmail (more secure than regular password)
3. Consider using environment variables instead of config file
4. Keep the automation log file readable only by you: `chmod 600 automation.log`
5. Rotate your SMTP passwords periodically

## Support

- [Main README](../README.md)
- [Quick Start Guide](../QUICKSTART.md)
- [GitHub Issues](https://github.com/CaptainDarkHeart/shoescanner/issues)

Happy automated deal hunting! 🎉
