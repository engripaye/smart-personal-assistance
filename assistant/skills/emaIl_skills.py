from .base import Skill
from ..core.config import settings
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import re


class EmailSkill(Skill):
    """Send a simple plaintext email via SMTP."""
def run(self, text: str, **kwargs) -> str:
# Extract recipient & subject/body heuristically
to = kwargs.get('to')
if not to:
    m = re.search(r"to (\S+@\S+)", text)
to = m.group(1) if m else None
subject_match = re.search(r"subject (.+?)(?: body |$)", text, re.I)
subject = subject_match.group(1).strip() if subject_match else "Hello from Smart Assistant"
body_match = re.search(r"body (.+)$", text, re.I)
body = body_match.group(1).strip() if body_match else text
if not to:
    return "I couldn't find the recipient's email. Say: send email to alice@example.com subject ... body ..."


msg = MIMEText(body, 'plain', 'utf-8')
msg['From'] = formataddr(('Assistant', settings.email_user))
msg['To'] = to
msg['Subject'] = subject


with smtplib.SMTP(settings.email_smtp, settings.email_port) as server:
    if settings.email_use_tls:
    server.starttls()
server.login(settings.email_user, settings.email_password)
server.send_message(msg)
return f"Email sent to {to} with subject '{