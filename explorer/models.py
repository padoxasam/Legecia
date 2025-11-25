from django.db import models
from package.models import Package
from user_registration.models import User
class PackageExplorer(models.Model):
    pack=models.ForeignKey(Package,on_delete=models.CASCADE)
    ownership=models.ForeignKey(User,on_delete=models.CASCADE)
    family_nickname=models.CharField(max_length=100)
    is_public=models.BooleanField(default=True)
    posted_at=models.DateField()
    remarks=models.TextField(null=True,blank=True)

    class Meta:
        db_table='pack_explorar'
        oredering=['-posted_at']

    def __str__(self):
        return f'Public Package:{self.pack_name} by:{self.ownership}'