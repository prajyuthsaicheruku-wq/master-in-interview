import os
import smtplib
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def get_otp_html_template(otp_code, username=None):
    user_greeting = f"Hi {username}," if username else "Hello,"
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Email Verification Code</title>
    </head>
    <body style="margin: 0; padding: 0; background-color: #0f172a; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; color: #f8fafc;">
        <table width="100%" border="0" cellspacing="0" cellpadding="0" style="background-color: #0f172a; padding: 40px 20px;">
            <tr>
                <td align="center">
                    <table width="100%" max-width="520px" border="0" cellspacing="0" cellpadding="0" style="max-width: 520px; background: #1e293b; border-radius: 16px; overflow: hidden; border: 1px solid #334155; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
                        <!-- Header Banner -->
                        <tr>
                            <td style="padding: 32px 30px 20px 30px; text-align: center; background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 50%, #0284c7 100%);">
                                <div style="font-size: 32px; margin-bottom: 8px;">🚀</div>
                                <h1 style="margin: 0; font-size: 22px; font-weight: 800; color: #ffffff; letter-spacing: 0.5px;">Interview Master</h1>
                                <p style="margin: 4px 0 0 0; font-size: 13px; color: #e2e8f0; font-weight: 500;">Account Verification</p>
                            </td>
                        </tr>

                        <!-- Body Content -->
                        <tr>
                            <td style="padding: 32px 30px;">
                                <p style="margin: 0 0 16px 0; font-size: 16px; color: #f1f5f9; font-weight: 600;">{user_greeting}</p>
                                <p style="margin: 0 0 24px 0; font-size: 14px; line-height: 1.6; color: #94a3b8;">
                                    Thank you for registering on <strong>Interview Master</strong>. To activate your account and access all interview preparation features, please enter the verification code below:
                                </p>

                                <!-- OTP Code Box -->
                                <div style="background: #0f172a; border: 2px dashed #6366f1; border-radius: 12px; padding: 20px; text-align: center; margin: 24px 0;">
                                    <div style="font-size: 12px; font-weight: 700; color: #818cf8; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 8px;">Your 6-Digit OTP</div>
                                    <div style="font-size: 36px; font-weight: 900; letter-spacing: 8px; color: #38bdf8; font-family: monospace;">{otp_code}</div>
                                    <div style="font-size: 12px; color: #64748b; margin-top: 8px;">⏱️ Valid for 10 minutes</div>
                                </div>

                                <p style="margin: 20px 0 0 0; font-size: 13px; line-height: 1.5; color: #64748b;">
                                    If you did not request this code, please safely ignore this email. Do not share this OTP with anyone.
                                </p>
                            </td>
                        </tr>

                        <!-- Footer -->
                        <tr>
                            <td style="padding: 20px 30px; background: #0f172a; text-align: center; border-top: 1px solid #334155;">
                                <p style="margin: 0; font-size: 12px; color: #64748b;">
                                    © 2026 Interview Master Portal. All rights reserved.
                                </p>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
    </body>
    </html>
    """

def send_brevo_otp_email(to_email, otp_code, username=None):
    """
    Sends OTP email using Brevo (Sendinblue) API v3 or SMTP fallback.
    If Brevo credentials are not configured, prints OTP to terminal for dev mode.
    """
    api_key = os.environ.get('BREVO_API_KEY', '').strip()
    sender_email = os.environ.get('BREVO_SENDER_EMAIL', 'support@interviewmaster.local').strip()
    sender_name = os.environ.get('BREVO_SENDER_NAME', 'Interview Master Portal').strip()

    subject = f"{otp_code} is your Interview Master verification code"
    html_content = get_otp_html_template(otp_code, username)

    # 1. Preferred: Brevo REST API v3
    if api_key:
        try:
            url = "https://api.brevo.com/v3/smtp/email"
            headers = {
                "accept": "application/json",
                "content-type": "application/json",
                "api-key": api_key
            }
            payload = {
                "sender": {"name": sender_name, "email": sender_email},
                "to": [{"email": to_email, "name": username or to_email}],
                "subject": subject,
                "htmlContent": html_content
            }
            response = requests.post(url, json=payload, headers=headers, timeout=10)
            if response.status_code in [200, 201, 202]:
                print(f"[BREVO API SUCCESS] Verification email sent to {to_email}")
                return True, "OTP email sent successfully."
            else:
                print(f"[BREVO API ERROR {response.status_code}]: {response.text}")
                return False, f"Brevo API Error: {response.text}"
        except Exception as e:
            print(f"[BREVO API EXCEPTION]: {e}")
            return False, f"Email delivery failed: {e}"

    # 2. Alternative: Brevo SMTP Relay
    smtp_login = os.environ.get('BREVO_SMTP_LOGIN', '').strip()
    smtp_key = os.environ.get('BREVO_SMTP_KEY', '').strip()
    if smtp_login and smtp_key:
        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = f"{sender_name} <{sender_email}>"
            msg['To'] = to_email
            msg.attach(MIMEText(html_content, 'html'))

            with smtplib.SMTP("smtp-relay.brevo.com", 587, timeout=10) as server:
                server.starttls()
                server.login(smtp_login, smtp_key)
                server.sendmail(sender_email, to_email, msg.as_string())
            print(f"[BREVO SMTP SUCCESS] Verification email sent to {to_email}")
            return True, "OTP email sent successfully via SMTP."
        except Exception as e:
            print(f"[BREVO SMTP EXCEPTION]: {e}")
            return False, f"SMTP delivery failed: {e}"

    # 3. Dev Fallback: Terminal Log
    print("=" * 65)
    print(f" [BREVO DEV MODE] Simulated OTP Email")
    print(f" To: {to_email} | User: {username}")
    print(f" OTP CODE: >>> {otp_code} <<< (Valid for 10 minutes)")
    print(f" (Set BREVO_API_KEY and BREVO_SENDER_EMAIL in .env to send real emails)")
    print("=" * 65)
    return True, "OTP generated (Dev mode: check server console or configure Brevo)."
