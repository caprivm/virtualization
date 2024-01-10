from application.settings.celery_settings import app


@app.task(queue="default")
def send_notification_email(message: str, recipient_list: list, subject: str) -> None:
    """
    Function to send an email notification to the user.

    :param message: Message to be sent.
    :type message: str
    :param recipient_list: List of recipients.
    :type recipient_list: list
    :param subject: Subject of the email.
    :type subject: str
    :raises Exception: Exception raised if the email cannot be sent.
    """
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email="foo@bar.com",
            recipient_list=recipient_list,
            fail_silently=False,
        )
    except Exception:
        raise Exception("The email cannot be sent.")


def send_mail(
    subject: str,
    message: str,
    from_email: str,
    recipient_list: list,
    fail_silently: bool = False,
) -> int:
    """
    Function to send an email notification to the user.

    :param subject: Subject of the email.
    :type subject: str
    :param message: Message to be sent.
    :type message: str
    :param from_email: Sender of the email.
    :type from_email: str
    :param recipient_list: List of recipients.
    :type recipient_list: list
    :param fail_silently: Flag to raise an exception if the email cannot be sent, defaults to False
    :type fail_silently: bool, optional
    :return: Number of emails sent.
    :rtype: int
    """
    pass
