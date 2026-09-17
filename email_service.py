import os
import smtplib
import threading
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Global persistent HTTP session with connection pooling for maximum speed
http_session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=20, max_retries=1)
http_session.mount('https://', adapter)
http_session.mount('http://', adapter)

def get_otp_text_template(otp_code, username=None, purpose='register'):
    user_greeting = f"Hi {username}," if username else "Hello,"
    if purpose == 'reset_password':
        action_text = "Use the verification code below to reset your Interview Master password:"
    else:
        action_text = "Thank you for joining Interview Master! Use the verification code below to activate your account:"

    return f"""{user_greeting}

{action_text}

VERIFICATION CODE: {otp_code}

This code will expire in 15 minutes.
If you did not request this code, you can safely ignore this email.

Best regards,
Interview Master Team
"""

def get_otp_html_template(otp_code, username=None, purpose='register'):
    user_greeting = f"Hi {username}," if username else "Hello,"
    if purpose == 'reset_password':
        header_title = "Password Recovery"
        header_icon = "🔑"
        intro_text = "We received a request to reset your password on <strong>Interview Master</strong>. Enter the verification code below to proceed:"
        sub_title = "Password Reset Verification"
    else:
        header_title = "Account Verification"
        header_icon = "🚀"
        intro_text = "Thank you for registering on <strong>Interview Master</strong>. To activate your account and start your placement preparation, enter the verification code below:"
        sub_title = "Account Verification Code"

    return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{sub_title}</title>
</head>
<body style="margin: 0; padding: 0; background-color: #0b0f19; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #f8fafc;">
    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="background-color: #0b0f19; padding: 30px 15px;">
        <tr>
            <td align="center">
                <table width="100%" max-width="520px" border="0" cellspacing="0" cellpadding="0" style="max-width: 520px; background: #131d31; border-radius: 18px; overflow: hidden; border: 1px solid #1e293b; box-shadow: 0 15px 35px rgba(0,0,0,0.5);">
                    <!-- Header Banner -->
                    <tr>
                        <td style="padding: 28px 24px 20px 24px; text-align: center; background: linear-gradient(135deg, #4f46e5 0%, #0284c7 100%);">
                            <div style="font-size: 30px; margin-bottom: 6px;">{header_icon}</div>
                            <h1 style="margin: 0; font-size: 22px; font-weight: 800; color: #ffffff; letter-spacing: 0.5px;">Interview Master</h1>
                            <p style="margin: 4px 0 0 0; font-size: 13px; color: #e0e7ff; font-weight: 500;">{header_title}</p>
                        </td>
                    </tr>

                    <!-- Body Content -->
                    <tr>
                        <td style="padding: 28px 24px;">
                            <p style="margin: 0 0 14px 0; font-size: 16px; color: #f1f5f9; font-weight: 600;">{user_greeting}</p>
                            <p style="margin: 0 0 20px 0; font-size: 14px; line-height: 1.6; color: #94a3b8;">
                                {intro_text}
                            </p>

                            <!-- OTP Code Box -->
                            <div style="background: #090d16; border: 2px dashed #6366f1; border-radius: 14px; padding: 22px; text-align: center; margin: 20px 0;">
                                <div style="font-size: 11px; font-weight: 800; color: #818cf8; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 8px;">Your 6-Digit Verification Code</div>
                                <div style="font-size: 38px; font-weight: 900; letter-spacing: 10px; color: #38bdf8; font-family: 'Courier New', Courier, monospace; line-height: 1;">{otp_code}</div>
                                <div style="font-size: 12px; color: #64748b; margin-top: 10px; font-weight: 500;">⏱️ Valid for 15 minutes</div>
                            </div>

                            <p style="margin: 20px 0 0 0; font-size: 12px; line-height: 1.5; color: #64748b;">
                                🔒 For security, never share this code with anyone. If you didn't request this, please ignore this email.
                            </p>
                        </td>
                    </tr>

                    <!-- Footer -->
                    <tr>
                        <td style="padding: 18px 24px; background: #090d16; text-align: center; border-top: 1px solid #1e293b;">
                            <p style="margin: 0; font-size: 11px; color: #64748b;">
                                © 2026 Interview Master Portal • Ace Your Technical & HR Rounds
                            </p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>"""

def get_reset_link_html_template(reset_url, username=None, local_reset_url=None):
    user_greeting = f"Hi {username}," if username else "Hello,"
    local_section = ""
    if local_reset_url and local_reset_url != reset_url:
        local_section = f"""
        <div style="margin-top: 16px; padding: 12px; background: #090d16; border-radius: 8px; border: 1px solid #1e293b;">
            <p style="margin: 0 0 6px 0; font-size: 11px; font-weight: 600; color: #94a3b8;">💻 If testing locally on localhost:</p>
            <a href="{local_reset_url}" style="font-size: 11px; word-break: break-all; color: #38bdf8; text-decoration: underline;">{local_reset_url}</a>
        </div>
        """

    return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reset Your Password</title>
</head>
<body style="margin: 0; padding: 0; background-color: #0b0f19; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #f8fafc;">
    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="background-color: #0b0f19; padding: 30px 15px;">
        <tr>
            <td align="center">
                <table width="100%" max-width="540px" border="0" cellspacing="0" cellpadding="0" style="max-width: 540px; background: #131d31; border-radius: 18px; overflow: hidden; border: 1px solid #1e293b; box-shadow: 0 15px 35px rgba(0,0,0,0.5);">
                    <tr>
                        <td style="padding: 28px 24px 20px 24px; text-align: center; background: linear-gradient(135deg, #4f46e5 0%, #0284c7 100%);">
                            <div style="font-size: 30px; margin-bottom: 6px;">🔑</div>
                            <h1 style="margin: 0; font-size: 22px; font-weight: 800; color: #ffffff; letter-spacing: 0.5px;">Interview Master</h1>
                            <p style="margin: 4px 0 0 0; font-size: 13px; color: #e0e7ff; font-weight: 500;">Password Recovery</p>
                        </td>
                    </tr>
                    <tr>
                        <td style="padding: 28px 24px;">
                            <p style="margin: 0 0 14px 0; font-size: 16px; color: #f1f5f9; font-weight: 600;">{user_greeting}</p>
                            <p style="margin: 0 0 22px 0; font-size: 14px; line-height: 1.6; color: #94a3b8;">
                                We received a request to reset your password. Click the button below to create a new password:
                            </p>
                            <div style="text-align: center; margin: 26px 0;">
                                <a href="{reset_url}" target="_blank" style="display: inline-block; background: linear-gradient(135deg, #4f46e5 0%, #0284c7 100%); color: #ffffff; text-decoration: none; font-weight: 800; font-size: 15px; padding: 14px 30px; border-radius: 10px; box-shadow: 0 4px 20px rgba(79, 70, 229, 0.4);">
                                    🔐 Create New Password →
                                </a>
                            </div>
                            <div style="text-align: center; margin-bottom: 20px;">
                                <span style="display: inline-block; background: #090d16; border: 1px solid #1e293b; border-radius: 20px; padding: 5px 14px; font-size: 11px; color: #94a3b8;">
                                    ⏱️ Link valid for 30 minutes
                                </span>
                            </div>
                            <p style="margin: 18px 0 6px 0; font-size: 11px; color: #64748b;">
                                Direct Link:
                            </p>
                            <p style="margin: 0 0 10px 0; font-size: 11px; word-break: break-all; color: #38bdf8; background: #090d16; padding: 8px 12px; border-radius: 6px; border: 1px solid #1e293b;">
                                {reset_url}
                            </p>
                            {local_section}
                        </td>
                    </tr>
                    <tr>
                        <td style="padding: 18px 24px; background: #090d16; text-align: center; border-top: 1px solid #1e293b;">
                            <p style="margin: 0; font-size: 11px; color: #64748b;">
                                © 2026 Interview Master Portal
                            </p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>"""

def send_brevo_otp_email(to_email, otp_code, username=None, purpose='register'):
    """
    High-speed, multi-provider email sender with connection pooling and fast fallbacks.
    """
    to_email = (to_email or '').strip()
    if not to_email:
        return False, "Recipient email is missing."

    api_key = os.environ.get('BREVO_API_KEY', '').strip()
    sender_email = (os.environ.get('BREVO_SENDER_EMAIL') or os.environ.get('MAIL_DEFAULT_SENDER') or 'support@interviewmaster.local').strip()
    sender_name = os.environ.get('BREVO_SENDER_NAME', 'Interview Master Portal').strip()

    subject = f"{otp_code} is your Interview Master verification code" if purpose != 'reset_password' else f"{otp_code} is your Interview Master password reset code"
    html_content = get_otp_html_template(otp_code, username, purpose)
    text_content = get_otp_text_template(otp_code, username, purpose)

    # 1. Preferred: Brevo REST API v3 (Ultra-fast via Keep-Alive session)
    if api_key:
        try:
            url = "https://api.brevo.com/v3/smtp/email"
            headers = {
                "accept": "application/json",
                "content-type": "application/json",
                "api-key": api_key,
                "User-Agent": "InterviewMaster-Mailer/2.0"
            }
            payload = {
                "sender": {"name": sender_name, "email": sender_email},
                "to": [{"email": to_email, "name": username or to_email}],
                "subject": subject,
                "htmlContent": html_content,
                "textContent": text_content,
                "headers": {
                    "X-Priority": "1",
                    "Importance": "high",
                    "Auto-Submitted": "auto-generated"
                },
                "tags": ["otp-auth", "fast-delivery"]
            }
            response = http_session.post(url, json=payload, headers=headers, timeout=6)
            if response.status_code in [200, 201, 202]:
                print(f"[BREVO API SUCCESS] {purpose} OTP email sent to {to_email}")
                return True, "OTP email sent successfully."
            else:
                print(f"[BREVO API WARNING {response.status_code}]: {response.text}")
        except Exception as e:
            print(f"[BREVO API EXCEPTION]: {e}")

    # 2. Alternative: Brevo SMTP Relay
    smtp_login = os.environ.get('BREVO_SMTP_LOGIN', '').strip()
    smtp_key = os.environ.get('BREVO_SMTP_KEY', '').strip()
    if smtp_login and smtp_key:
        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = f"{sender_name} <{sender_email}>"
            msg['To'] = to_email
            msg['X-Priority'] = '1'
            msg['Importance'] = 'high'
            msg.attach(MIMEText(text_content, 'plain'))
            msg.attach(MIMEText(html_content, 'html'))

            with smtplib.SMTP("smtp-relay.brevo.com", 587, timeout=6) as server:
                server.starttls()
                server.login(smtp_login, smtp_key)
                server.sendmail(sender_email, to_email, msg.as_string())
            print(f"[BREVO SMTP SUCCESS] {purpose} email sent to {to_email}")
            return True, "OTP email sent successfully via SMTP."
        except Exception as e:
            print(f"[BREVO SMTP EXCEPTION]: {e}")

    # 3. Alternative: Standard SMTP / Gmail SMTP Relay
    gmail_user = (os.environ.get('GMAIL_USER') or os.environ.get('MAIL_USERNAME') or '').strip()
    gmail_password = (os.environ.get('GMAIL_APP_PASSWORD') or os.environ.get('MAIL_PASSWORD') or '').strip()
    smtp_host = os.environ.get('MAIL_SERVER', 'smtp.gmail.com').strip()
    smtp_port = int(os.environ.get('MAIL_PORT', 587))

    if gmail_user and gmail_password:
        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = f"{sender_name} <{gmail_user}>"
            msg['To'] = to_email
            msg['X-Priority'] = '1'
            msg.attach(MIMEText(text_content, 'plain'))
            msg.attach(MIMEText(html_content, 'html'))

            with smtplib.SMTP(smtp_host, smtp_port, timeout=6) as server:
                server.starttls()
                server.login(gmail_user, gmail_password)
                server.sendmail(gmail_user, to_email, msg.as_string())
            print(f"[GMAIL/SMTP SUCCESS] {purpose} email sent to {to_email}")
            return True, "OTP email sent successfully via Gmail SMTP."
        except Exception as e:
            print(f"[GMAIL/SMTP EXCEPTION]: {e}")

    # 4. Dev / Sandbox Fallback: Terminal Log
    print("=" * 65)
    print(f" [DEV MODE SIMULATION] Verification OTP Generated")
    print(f" To: {to_email} | User: {username or 'New Candidate'}")
    print(f" [OTP CODE]: >>>  {otp_code}  <<< (Valid for 15 minutes)")
    print("=" * 65)
    return True, "OTP generated (Dev Mode simulation logged to terminal)."

def send_brevo_password_reset_link_email(to_email, reset_url, username=None, local_reset_url=None):
    """
    High-speed password reset link email sender.
    """
    to_email = (to_email or '').strip()
    if not to_email:
        return False, "Recipient email is missing."

    api_key = os.environ.get('BREVO_API_KEY', '').strip()
    sender_email = (os.environ.get('BREVO_SENDER_EMAIL') or os.environ.get('MAIL_DEFAULT_SENDER') or 'support@interviewmaster.local').strip()
    sender_name = os.environ.get('BREVO_SENDER_NAME', 'Interview Master Portal').strip()

    subject = "Reset your Interview Master password"
    html_content = get_reset_link_html_template(reset_url, username, local_reset_url)
    text_content = f"Hi {username or 'there'},\n\nClick the link below to reset your Interview Master password:\n{reset_url}\n\nThis link is valid for 30 minutes.\n"

    # 1. Preferred: Brevo REST API v3
    if api_key:
        try:
            url = "https://api.brevo.com/v3/smtp/email"
            headers = {
                "accept": "application/json",
                "content-type": "application/json",
                "api-key": api_key,
                "User-Agent": "InterviewMaster-Mailer/2.0"
            }
            payload = {
                "sender": {"name": sender_name, "email": sender_email},
                "to": [{"email": to_email, "name": username or to_email}],
                "subject": subject,
                "htmlContent": html_content,
                "textContent": text_content,
                "headers": {
                    "X-Priority": "1",
                    "Importance": "high"
                }
            }
            response = http_session.post(url, json=payload, headers=headers, timeout=6)
            if response.status_code in [200, 201, 202]:
                print(f"[BREVO API SUCCESS] Password reset email sent to {to_email}")
                return True, "Password reset email sent successfully."
            else:
                print(f"[BREVO API WARNING {response.status_code}]: {response.text}")
        except Exception as e:
            print(f"[BREVO API EXCEPTION]: {e}")

    # 2. Alternative: Brevo SMTP Relay
    smtp_login = os.environ.get('BREVO_SMTP_LOGIN', '').strip()
    smtp_key = os.environ.get('BREVO_SMTP_KEY', '').strip()
    if smtp_login and smtp_key:
        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = f"{sender_name} <{sender_email}>"
            msg['To'] = to_email
            msg.attach(MIMEText(text_content, 'plain'))
            msg.attach(MIMEText(html_content, 'html'))

            with smtplib.SMTP("smtp-relay.brevo.com", 587, timeout=6) as server:
                server.starttls()
                server.login(smtp_login, smtp_key)
                server.sendmail(sender_email, to_email, msg.as_string())
            print(f"[BREVO SMTP SUCCESS] Password reset email sent to {to_email}")
            return True, "Password reset link sent successfully via SMTP."
        except Exception as e:
            print(f"[BREVO SMTP EXCEPTION]: {e}")

    # 3. Dev Fallback: Terminal Log
    print("=" * 65)
    print(f" [DEV MODE SIMULATION] Simulated Password Reset Link Email")
    print(f" To: {to_email} | User: {username}")
    print(f" RESET LINK: >>> {reset_url} <<< (Valid for 30 minutes)")
    print("=" * 65)
    return True, "Password reset link generated (Dev mode)."

def send_async_otp_email(to_email, otp_code, username=None, purpose='register'):
    """
    Spawns a daemon thread to send OTP email immediately in the background without blocking HTTP responses.
    """
    thread = threading.Thread(
        target=send_brevo_otp_email,
        args=(to_email, otp_code, username, purpose),
        daemon=True
    )
    thread.start()
    return thread

def send_async_reset_link_email(to_email, reset_url, username=None, local_reset_url=None):
    """
    Spawns a daemon thread to send Password Reset Link email in the background.
    """
    thread = threading.Thread(
        target=send_brevo_password_reset_link_email,
        args=(to_email, reset_url, username, local_reset_url),
        daemon=True
    )
    thread.start()
    return thread


