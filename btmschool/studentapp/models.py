from django.db import models

adm_class = (
    ('10th', '10th'),
    ('9th', '9th'),
    ('8th', '8th'),
    ('7th', '7th'),
    ('6th', '6th'),

)
nation = (
    ('in', 'India'),
    ('pk', 'Pakistan'),
    ('sl', 'Srilanka'),
    ('ch', 'Chain'),
    ('us', 'Us')

)
state = (
    ('OD', 'Odisha'),
    ('AP', 'Andhrapradesh'),
    ('TS', 'Telengana'),
    ('CG', 'Chhattisgarh'),
    ('KA', 'Karnataka'),
    ('KL', 'Kerala'),
    ('BR', 'Bihar'),
    ('GA', 'Goa')
)
religion = (
    ('hindu', 'Hindu'),
    ('musilim', 'musilim'),
    ('sikh', 'sikh'),
    ('christian', 'christian')
)
gender = (
    ('m', 'male'),
    ('f', 'female')
)
caste = (
    ('obc', 'OBC'),
    ('sc', 'SC'),
    ('st', 'ST'),
    ('general', 'General'),
)
blood_group = (
    ('O+', 'O+'),
    ('O-', 'O-'),
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-')
)


class registerModel(models.Model):
    name = models.CharField(max_length=35)
    ad_class = models.CharField(choices=adm_class, max_length=5)
    DOB = models.DateField()
    place_birth = models.CharField(max_length=50)
    nation = models.CharField(choices=nation, max_length=10)
    state = models.CharField(choices=state, max_length=20)
    religion = models.CharField(choices=religion, max_length=12)
    gender = models.CharField(choices=gender, max_length=8)
    caste = models.CharField(choices=caste, max_length=10, null=True)
    permanent_address = models.CharField(max_length=70, null=True)
    pin_code = models.PositiveSmallIntegerField(null=True)
    blood_group = models.CharField(choices=blood_group, max_length=5, null=True)
    identification_mark = models.CharField(max_length=65, null=True)
    other_info = models.TextField(max_length=150, null=True)


# Counting visitor
"""class User(models.Model):
    user = models.TextField(default=None)

    def __str__(self):
        return self.user"""
