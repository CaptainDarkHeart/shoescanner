#!/usr/bin/env python3
"""
Shoe Scanner Automation Script

Runs the shoescanner skill and emails results when deals are found.
Designed to run via cron/scheduled tasks for automated deal hunting.

Usage:
    python shoescanner_automation.py

Configuration via environment variables or config file.
"""

import os
import sys
import json
import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional


class ShoeScannerAutomation:
    """Automates shoe scanning and email notifications"""

    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize automation with configuration.

        Args:
            config_path: Path to config file (defaults to automation_config.json)
        """
        self.config_path = config_path or self._get_default_config_path()
        self.config = self._load_config()
        self.skill_settings = self._load_skill_settings()
        self.seen_deals_path = self._expand_path(
            self.skill_settings.get("seenDealsFile", "~/.claude/skills/shoescanner/seen-deals.json")
        )

    def _get_default_config_path(self) -> str:
        """Get default config path"""
        script_dir = Path(__file__).parent
        return str(script_dir / "automation_config.json")

    def _expand_path(self, path: str) -> str:
        """Expand ~ and environment variables in path"""
        return os.path.expanduser(os.path.expandvars(path))

    def _load_config(self) -> Dict:
        """Load automation configuration"""
        if not os.path.exists(self.config_path):
            return self._create_default_config()

        with open(self.config_path, 'r') as f:
            return json.load(f)

    def _create_default_config(self) -> Dict:
        """Create default configuration"""
        default_config = {
            "email": {
                "enabled": True,
                "smtp_server": os.getenv("SMTP_SERVER", "smtp.gmail.com"),
                "smtp_port": int(os.getenv("SMTP_PORT", "587")),
                "smtp_user": os.getenv("SMTP_USER", ""),
                "smtp_password": os.getenv("SMTP_PASSWORD", ""),
                "from_address": os.getenv("EMAIL_FROM", ""),
                "to_address": os.getenv("EMAIL_TO", ""),
                "subject": "🔥 New Shoe Deals Found!"
            },
            "claude": {
                "command": "claude",
                "skill": "shoescanner"
            },
            "logging": {
                "enabled": True,
                "log_file": "~/.claude/skills/shoescanner/automation.log"
            },
            "only_email_on_deals": True
        }

        # Save default config
        os.makedirs(os.path.dirname(self.config_path), exist_ok=True)
        with open(self.config_path, 'w') as f:
            json.dump(default_config, f, indent=2)

        print(f"Created default config at {self.config_path}")
        print("Please edit this file with your email settings.")

        return default_config

    def _load_skill_settings(self) -> Dict:
        """Load skill settings"""
        settings_path = self._expand_path("~/.claude/skills/shoescanner/settings.json")

        if not os.path.exists(settings_path):
            raise FileNotFoundError(
                f"Skill settings not found at {settings_path}. "
                "Please run /shoescanner at least once to configure it."
            )

        with open(settings_path, 'r') as f:
            return json.load(f)

    def _load_seen_deals(self) -> List[Dict]:
        """Load previously seen deals"""
        if not os.path.exists(self.seen_deals_path):
            return []

        with open(self.seen_deals_path, 'r') as f:
            return json.load(f)

    def _log(self, message: str):
        """Log message to file and console"""
        timestamp = datetime.now().isoformat()
        log_message = f"[{timestamp}] {message}"

        print(log_message)

        if self.config.get("logging", {}).get("enabled", True):
            log_file = self._expand_path(
                self.config.get("logging", {}).get("log_file", "automation.log")
            )
            os.makedirs(os.path.dirname(log_file), exist_ok=True)

            with open(log_file, 'a') as f:
                f.write(log_message + '\n')

    def run_skill(self) -> Optional[str]:
        """
        Run the shoescanner skill using Claude CLI.

        Returns:
            Output from the skill execution, or None if failed
        """
        self._log("Running shoescanner skill...")

        try:
            # Run claude with the skill command
            # Note: This assumes 'claude' CLI is available and configured
            result = subprocess.run(
                ["claude", "code", "--skill", self.config["claude"]["skill"]],
                capture_output=True,
                text=True,
                timeout=300  # 5 minute timeout
            )

            if result.returncode != 0:
                self._log(f"Skill execution failed: {result.stderr}")
                return None

            self._log("Skill execution completed")
            return result.stdout

        except subprocess.TimeoutExpired:
            self._log("Skill execution timed out")
            return None
        except FileNotFoundError:
            self._log("Claude CLI not found. Is it installed and in PATH?")
            return None
        except Exception as e:
            self._log(f"Error running skill: {e}")
            return None

    def get_new_deals(self) -> List[Dict]:
        """
        Get deals that were added since last run.

        Returns:
            List of new deals found in this run
        """
        # Load current seen deals
        current_deals = self._load_seen_deals()

        # Load previous state (if exists)
        state_file = self._expand_path("~/.claude/skills/shoescanner/automation_state.json")

        if os.path.exists(state_file):
            with open(state_file, 'r') as f:
                state = json.load(f)
                previous_deal_urls = set(state.get("seen_urls", []))
        else:
            previous_deal_urls = set()

        # Find new deals
        new_deals = [
            deal for deal in current_deals
            if deal.get("url") not in previous_deal_urls
        ]

        # Update state
        current_urls = [deal.get("url") for deal in current_deals if deal.get("url")]
        with open(state_file, 'w') as f:
            json.dump({
                "seen_urls": current_urls,
                "last_run": datetime.now().isoformat()
            }, f, indent=2)

        return new_deals

    def format_email_body(self, deals: List[Dict]) -> str:
        """
        Format deals into HTML email body.

        Args:
            deals: List of deal dictionaries

        Returns:
            HTML formatted email body
        """
        if not deals:
            return "<p>No new deals found in this scan.</p>"

        # Get user preferences for context
        brand = self.skill_settings.get("manufacturer", "shoes")
        size = self.skill_settings.get("size", "your size")
        max_price = self.skill_settings.get("maxPrice", "")
        currency = self.skill_settings.get("currency", "")

        html = f"""
        <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
                .header {{ background-color: #4CAF50; color: white; padding: 20px; text-align: center; }}
                .deal {{ border: 1px solid #ddd; margin: 20px 0; padding: 15px; border-radius: 5px; }}
                .deal h3 {{ margin-top: 0; color: #4CAF50; }}
                .price {{ font-size: 1.5em; font-weight: bold; color: #e74c3c; }}
                .link {{ display: inline-block; margin-top: 10px; padding: 10px 20px; background-color: #4CAF50; color: white; text-decoration: none; border-radius: 3px; }}
                .footer {{ margin-top: 30px; padding-top: 20px; border-top: 1px solid #ddd; font-size: 0.9em; color: #666; }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>🔥 New Shoe Deals Found!</h1>
                <p>Found {len(deals)} new deal{"s" if len(deals) != 1 else ""} for {brand} in size {size}</p>
            </div>
        """

        for i, deal in enumerate(deals, 1):
            model = deal.get("model", "Unknown Model")
            colorway = deal.get("colorway", "")
            price = deal.get("price", "Price not available")
            url = deal.get("url", "#")
            retailer = deal.get("retailer", "Retailer")
            found_date = deal.get("found", "")

            title = f"{model} - {colorway}" if colorway else model

            html += f"""
            <div class="deal">
                <h3>#{i}. {title}</h3>
                <p class="price">{price}</p>
                <p><strong>Retailer:</strong> {retailer}</p>
                <p><strong>Size:</strong> {size} available</p>
                <a href="{url}" class="link" target="_blank">View Deal →</a>
            </div>
            """

        html += f"""
            <div class="footer">
                <p><strong>Your Search Criteria:</strong></p>
                <ul>
                    <li>Brand: {brand}</li>
                    <li>Size: {size}</li>
                    <li>Max Price: {currency}{max_price}</li>
                </ul>
                <p style="font-size: 0.8em; color: #999;">
                    This is an automated email from Shoe Scanner.
                    <br>Last scan: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                </p>
            </div>
        </body>
        </html>
        """

        return html

    def send_email(self, deals: List[Dict]) -> bool:
        """
        Send email notification about deals.

        Args:
            deals: List of deals to include in email

        Returns:
            True if email sent successfully, False otherwise
        """
        email_config = self.config.get("email", {})

        if not email_config.get("enabled", True):
            self._log("Email notifications disabled")
            return False

        # Validate email configuration
        required_fields = ["smtp_server", "smtp_user", "smtp_password", "from_address", "to_address"]
        missing = [f for f in required_fields if not email_config.get(f)]

        if missing:
            self._log(f"Missing email configuration: {', '.join(missing)}")
            self._log("Please update automation_config.json with your email settings")
            return False

        try:
            # Create message
            msg = MIMEMultipart('alternative')
            msg['Subject'] = email_config.get("subject", "New Shoe Deals Found!")
            msg['From'] = email_config["from_address"]
            msg['To'] = email_config["to_address"]

            # Add HTML body
            html_body = self.format_email_body(deals)
            msg.attach(MIMEText(html_body, 'html'))

            # Send email
            self._log(f"Sending email to {email_config['to_address']}...")

            with smtplib.SMTP(email_config["smtp_server"], email_config["smtp_port"]) as server:
                server.starttls()
                server.login(email_config["smtp_user"], email_config["smtp_password"])
                server.send_message(msg)

            self._log("Email sent successfully")
            return True

        except Exception as e:
            self._log(f"Failed to send email: {e}")
            return False

    def run(self):
        """Main automation routine"""
        self._log("=" * 60)
        self._log("Starting Shoe Scanner Automation")
        self._log("=" * 60)

        # Run the skill
        output = self.run_skill()

        if output is None:
            self._log("Skill execution failed, aborting")
            return

        # Check for new deals
        new_deals = self.get_new_deals()

        self._log(f"Found {len(new_deals)} new deal(s)")

        # Send email if needed
        if new_deals:
            self._log("New deals detected, sending email notification...")
            self.send_email(new_deals)
        else:
            # Send email even with no deals if configured
            if not self.config.get("only_email_on_deals", True):
                self._log("No new deals, but sending status email anyway...")
                self.send_email([])
            else:
                self._log("No new deals found, skipping email")

        self._log("Automation run complete")
        self._log("=" * 60)


def main():
    """Entry point for automation script"""
    try:
        automation = ShoeScannerAutomation()
        automation.run()
    except Exception as e:
        print(f"Fatal error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
