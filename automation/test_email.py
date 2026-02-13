#!/usr/bin/env python3
"""
Email Configuration Test Script

Quick test to verify your email settings work before running automation.

Usage:
    python3 test_email.py
"""

import json
import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path


def load_config():
    """Load automation config"""
    config_path = Path(__file__).parent / "automation_config.json"

    if not config_path.exists():
        print("❌ automation_config.json not found!")
        print("📝 Please copy automation_config.json.example and fill in your settings")
        sys.exit(1)

    with open(config_path) as f:
        return json.load(f)


def test_email_config(config):
    """Test email configuration"""
    email_config = config.get("email", {})

    # Check required fields
    required = ["smtp_server", "smtp_port", "smtp_user", "smtp_password", "from_address", "to_address"]
    missing = [f for f in required if not email_config.get(f)]

    if missing:
        print(f"❌ Missing required fields: {', '.join(missing)}")
        return False

    print("✅ All required fields present")
    return True


def send_test_email(config):
    """Send a test email"""
    email_config = config["email"]

    try:
        # Create test message
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "✅ Shoe Scanner Email Test"
        msg['From'] = email_config["from_address"]
        msg['To'] = email_config["to_address"]

        # Simple HTML body
        html = """
        <html>
        <body>
            <h2>✅ Success!</h2>
            <p>Your Shoe Scanner automation email is configured correctly.</p>
            <p>You should now be able to receive deal notifications.</p>
            <hr>
            <p style="color: #666; font-size: 0.9em;">
                This is a test email from the Shoe Scanner automation system.
            </p>
        </body>
        </html>
        """

        msg.attach(MIMEText(html, 'html'))

        # Connect and send
        print(f"\n📧 Connecting to {email_config['smtp_server']}:{email_config['smtp_port']}...")

        with smtplib.SMTP(email_config['smtp_server'], email_config['smtp_port']) as server:
            server.set_debuglevel(0)  # Set to 1 for verbose output
            print("🔐 Starting TLS...")
            server.starttls()

            print("🔑 Authenticating...")
            server.login(email_config['smtp_user'], email_config['smtp_password'])

            print(f"📨 Sending test email to {email_config['to_address']}...")
            server.send_message(msg)

        print("\n✅ Test email sent successfully!")
        print(f"📬 Check your inbox at {email_config['to_address']}")
        return True

    except smtplib.SMTPAuthenticationError:
        print("\n❌ Authentication failed!")
        print("💡 Tips:")
        print("   - For Gmail: Use an App Password, not your regular password")
        print("   - Enable 2-factor authentication first")
        print("   - Generate App Password: https://myaccount.google.com/apppasswords")
        return False

    except smtplib.SMTPException as e:
        print(f"\n❌ SMTP error: {e}")
        return False

    except Exception as e:
        print(f"\n❌ Error: {e}")
        return False


def main():
    """Main test routine"""
    print("=" * 60)
    print("📧 Shoe Scanner Email Configuration Test")
    print("=" * 60)

    # Load config
    print("\n1️⃣ Loading configuration...")
    config = load_config()

    # Test config
    print("\n2️⃣ Checking configuration...")
    if not test_email_config(config):
        sys.exit(1)

    # Send test
    print("\n3️⃣ Sending test email...")
    if not send_test_email(config):
        sys.exit(1)

    print("\n" + "=" * 60)
    print("🎉 All tests passed!")
    print("=" * 60)
    print("\n✅ Your automation is ready to use!")
    print("📖 See automation/README.md for scheduling instructions")


if __name__ == "__main__":
    main()
