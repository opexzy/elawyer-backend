from django.db import models
from django.utils.translation import gettext as _
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.postgres.fields import ArrayField
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField
from simple_history.models import HistoricalRecords
from django_countries.fields import CountryField

GENDER_CHOICES = [
    ("male","Male"), ("female","Female")
]

SERVICE_INTEREST_CHOICES = [
    ("real_estate", "Real Etstate"), ("civil case", "Civil Case"), ("litigation", "Litigation"),
    ("human right", "Human Right"), ("employment agreement", "Employment Agreement"),
    ("business agreement","Business Agreement")
]

LEVEL_OF_EDUCATION_CHOICES = [
    ("phd","Doctor of Philosophy (Phd.)"), ("msc","Master of Science (MSc.)"), 
    ("ma","Master of Art (MA)"), ("mit","Master of Infomation Technology (MIT)"),
    ("pgd", "Post Graduate Diploma (PGD)"),("mbbs", "Bachelor of Medcine & Surgery (MBBS, BMBS"),
    ("bsc","Bachelor of Science (BSc)"), ("ba","Bachelor of Art (BA)"), ("hnd","Higher National Diploma (HND)"),
    ("nd","National Diploma (ND)"), ("high school","High School"), ("basic","Basic/Elementary School"),
    ("non", "No Formal Education"), ("","Would rather not specify")
]

HEARD_ABOUT_US_CHOICES = [
    ('facebook', 'Facebook'), ('twitter', 'Twitter'), ('instagram', 'Instagram'), ('linkedin', 'LinkedIn'),
    ('friend', 'Friend'), ('family', 'Family'), ('elawyerng staff', 'Elawyer-Ng Staff'), ('referral', 'Referral'),
    ('other', 'Other')
]

class Account(models.Model):
    """
        Account model for users that are not admin.
        It extends the base user model.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("User Id"), on_delete=models.CASCADE,
        related_name="account")
    gender = models.CharField(_("Gender"), choices=GENDER_CHOICES, max_length=6)
    phone_number = PhoneNumberField(_("Phone Number"), null=True, blank=True)
    birth_date = models.DateField(_("date of birth"), blank=True, null=True)
    country = CountryField(_("country"), blank=True, default='NG')
    state = models.CharField(_("State/Region"), null=True, blank=True, max_length=100)
    city = models.CharField(_("City/Town"), null=True, blank=True, max_length=100)
    address = models.CharField(_("address"), max_length=100, blank=True, null=True)
    service_interest = ArrayField(models.CharField(blank=True, max_length=255, choices=SERVICE_INTEREST_CHOICES), 
        blank=True, verbose_name=_("Service Interest"))
    occupation = models.CharField(_("Occupation"), max_length=255, null=True, blank=True)
    level_of_education = models.CharField(_("Highest Level of Education"), max_length=10, 
        choices=LEVEL_OF_EDUCATION_CHOICES)
    heard_about_us = models.CharField(_("How user heard about us"), max_length=100, choices=HEARD_ABOUT_US_CHOICES,
        blank=True, null=True, default='')
    email_verified = models.BooleanField(_("Is email verified"), default=False)
    audit = AuditlogHistoryField()
    history = HistoricalRecords()

    def __str__(self):
        return self.user.get_full_name()
        
    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name

    @property
    def email(self):
        return self.user.email

    @property
    def is_active(self):
        return self.user.is_active

    @property
    def age(self):
        if self.birth_date:
            return timezone.now().year - self.birth_date.year
        return None

    @property
    def date_joined(self):
        return self.user.date_joined
    
    def save(self, *args, **kwargs):
        """
            Overide the custom save method to perform
            some actions based on updated properties
        """
        if self.id:
            # Treat as update
            pass
        
        super().save(*args, **kwargs)

auditlog.register(Account) 
