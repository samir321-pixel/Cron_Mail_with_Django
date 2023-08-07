import smtplib
import logging
from django.core.mail import send_mail
from django.conf import settings

logger = logging.getLogger('event_emails')
from mail.models import Employee, EmailTemplate


def send_event_email(employee_email, subject, event_type, max_retries=3):
    try:
        employee = Employee.objects.get(email=employee_email)
        event_template = EmailTemplate.objects.get(event_type=event_type)
        email_content = event_template.template.format(employee_name=employee.name)

        for retry in range(max_retries + 1):
            try:
                send_mail(subject, email_content, settings.DEFAULT_FROM_EMAIL, [employee_email])
                logger.info(f"Email sent successfully for {event_type} event to {employee_email}")
                break
            except Exception as e:
                if retry < max_retries:
                    logger.warning(f"Failed to send email for {event_type} event to {employee_email}, retrying...")
                else:
                    logger.error(
                        f"Failed to send email for {event_type} event to {employee_email} after {max_retries} retries: {e}")
                    logger.error(f"Error details: {e}")
                    break

    except Employee.DoesNotExist:
        logger.error(f"Employee with email {employee_email} does not exist")
    except EmailTemplate.DoesNotExist:
        logger.error(f"Email template for {event_type} event does not exist")
    except Exception as e:
        logger.error(f"Failed to send email for {event_type} event to {employee_email}: {e}")
