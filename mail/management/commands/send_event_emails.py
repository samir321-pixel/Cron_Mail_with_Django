from django.core.management.base import BaseCommand
from datetime import date
import logging

logger = logging.getLogger('event_emails')
from mail.management.commands.utlis import send_event_email
from mail.models import Event, EmailTemplate, EmailLog


class Command(BaseCommand):
    help = 'Send event emails'

    def handle(self, *args, **options):
        today = date.today()
        events = Event.objects.filter(event_date=today)

        if not events:
            logger.info("No events are scheduled for the current period.")
            return

        for event in events:
            try:
                employee = event.employee
                email_template = EmailTemplate.objects.get(event_type=event.event_type)
                email_content = email_template.template.format(employee_name=employee.name)
                send_event_email(employee.email, 'Event Notification', event.event_type)
                EmailLog.objects.create(
                    event=event,
                    status='Success',
                )
            except Exception as e:
                EmailLog.objects.create(
                    event=event,
                    status='Error',
                    error_message=str(e),
                )
                logger.error(f"Failed to send email for {event.event_type} event to {employee.email}: {e}")
