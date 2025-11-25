from django.db import models

# Create your models here.
class Milestone(models.Model):
    milestone_id=models.AutoField(primary_key=True)
    milestone_name=models.CharField(max_length=100)
    ben_id=models.IntegerField()
    ben_full_name=models.CharField(max_length=100) ##
    upload_date=models.DateTimeField(auto_now_add=True)
    verified_documents=models.BooleanField(default=False)
    match_pack=models.BooleanField(default=False)
    family_name=models.CharField(max_length=100)
    file_format=models.CharField(max_length=60,null=True,blank=True)
    remarks=models.TextField(null=True,blank=True)
    user_reference_files=models.TextField(null=True,blank=True)
    beneficiary_files=models.TextField(null=True,blank=True)
    class Meta:
        db_table='milestone_upload'
    def __str__(self):
        return f'Milestone Name:{self.milestone_name} Designated to: {self.ben_full_name} '