from django import forms
from django.contrib.auth.forms import PasswordResetForm


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'autocomplete': 'email'}),
    )


from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.template.loader import render_to_string


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'autocomplete': 'email'}),
    )

    def send_mail(self, subject_template_name, email_template_name, context, from_email, to_email, html_email_template_name=None):
        """
        Sends a django.core.mail.EmailMultiAlternatives to `to_email`.
        """
        subject = render_to_string(subject_template_name, context)
        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())
        email = render_to_string(email_template_name, context)
        send_mail(
            subject, email, from_email, [to_email],
            html_message=html_email_template_name is not None,
        )