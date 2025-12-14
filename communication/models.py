from django.db import models
from user_registration.models import User, Beneficiary
from package.models import Package


class CommunicationMeans(models.Model):
    u = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column='u_id'
    )

    b_u = models.ForeignKey(
        Beneficiary,
        on_delete=models.CASCADE,
        db_column='b_u_id'
    )

    us_email = models.EmailField(max_length=100, unique=True)
    be_email = models.EmailField(max_length=100, unique=True)

    packg = models.ForeignKey(
        Package,
        on_delete=models.CASCADE,
        db_column='packg_id'
    )

    relation_choices = (
        ('MOTHER', 'MOTHER'),
        ('FATHER', 'FATHER'),
        ('GRANDMOTHER', 'GRANDMOTHER'),
        ('GRANDFATHER', 'GRANDFATHER'),
        ('STEP FATHER', 'STEP FATHER'),
        ('STEP MOTHER', 'STEP MOTHER'),
        ('BROTHER', 'BROTHER'),
        ('SISTER', 'SISTER'),
        ('UNCLE', 'UNCLE'),
        ('AUNT', 'AUNT'),
        ('COUSIN', 'COUSIN'),
        ('NEPHEW', 'NEPHEW'),
        ('NIECE', 'NIECE'),
        ('FAMILY FRIEND', 'FAMILY FRIEND'),
        ('NEIGHBOR', 'NEIGHBOR'),
        ('MENTOR', 'MENTOR'),
        ('SOCIAL WORKER', 'SOCIAL WORKER'),
        ('LEGAL GUARDIAN', 'LEGAL GUARDIAN'),
        ('FOSTER PARENT', 'FOSTER PARENT'),
        ('CARETAKER', 'CARETAKER'),
        ('OTHER', 'OTHER'),
    )

    relationship = models.CharField(max_length=50, choices=relation_choices)

    dep_mechanism = models.CharField(max_length=50)

    com_m1 = models.CharField(max_length=300)
    com_m2 = models.CharField(max_length=300, blank=True, null=True)

    additional_comments = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'communication_means'

    def __str__(self):
        return f'User: {self.us_email} → Beneficiary: {self.be_email}'
