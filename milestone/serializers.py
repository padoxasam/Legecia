from rest_framework import serializers
from .models import Milestone
import os 

class MilestoneSerializer(serializers.Serializer):
    milestone_id=serializers.IntegerField(required=True)
    milestone_name=serializers.CharField(max_length=100)
    family_name=serializers.CharField(max_length=100)
    remarks=serializers.CharField(required=False,allow_blank=True)
    user_reference_file=serializers.FileField(required=True)
    beneficiary_file=serializers.FileField(required=True)
    user_allowed_formats=['pdf','doc','docs','txt',"rtf",
    "xls", "xlsx", "ppt", "pptx","csv","json","xml",
    "mp4", "mov", "avi", "mkv",
    "mp3", "wav"
    "zip"]
    
    bene_allowed_formats=[ "jpg", "jpeg","png","heic", "heif",
    "webp", "bmp","tiff", "tif","pdf",
    "mp4", "mov", "avi", "mkv", "wav"
]
    user_reference_file=serializers.FileField(required=False)
    beneficiary_file=serializers.FileField(required=False)
    class Meta:
        model=Milestone
        fields='__all__'
    def validate(self, data):
        user=self.context['request'].user
        role=user.active_role
        file_user=data.get('user_reference_file')
        file_bene=data.get('beneficiary_file')
        if role =='USER':
                
            if not file_user:
                raise serializers.ValidationError('User Must Upload a Reference Docuements !')
            
            forma=os.path.splitext(file_user.name)[1].lower().replace('.','')
            if forma not in self.user_allowed_formats:
                raise serializers.ValidationError(f"invalid file format for User\n Allowed Formats:{', '.join(self.user_allowed_formats)}")
        elif role =='BENEFICIARY':
            if not file_bene:
                raise serializers.ValidationError('Beneficiary Must Upload a Milestone file !')
            forma=os.path.splitext(file_bene.name)[1].lower().replace('.','')
            if forma not in self.bene_allowed_formats:
                raise serializers.ValidationError(f"invalid file format for Beneficiary\n Allowed Formats:{', '.join(self.bene_allowed_formats)}")
        else:
            raise serializers.ValidationError("Your Active Role Doesnt permit Milestone Uploads")
        return data