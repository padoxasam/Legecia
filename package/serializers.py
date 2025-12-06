from rest_framework import serializers
from django.utils import timezone
from .models import Package

class PackageSeriializer(serializers.ModelSerializer):
    owner=serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Package
        fields = [ 'pack_id','owner','ownership','uploaded_on','pack_name',
                  'last_modification','pack_status','tags','pack_delivery',
                  'pack_type','total_files','has_expiry','expiry_at','unlocked','description'
                  
        ]
        read_only_fields= ['pack_id','total_files','unlocked']
    def validate(self, attrs): # llexpiry
        has_expiry=data.get('has_expiry',getattr(self.instance,'has_expiry',False))
        expiry=data.get("expiry_at",getattr(self.instance,'expiry_at',None))
        if has_expiry and not expiry:
            raise serializers.ValidationError('Expiry Date is Required ! ')
        return data 
    def create(self,validated_data):
        if 'uploaded_on' not in validated_data:
            validated_data['uploaded_on']=timezone.now().date()
        if 'last_modification' not in validated_data:
            validated_data['last_modification']=timezone.now().date()
        return super().create(validated_data)
    def update(self,instance,validated_data):
        fields_trigger_last_modification=['pack_name','tags','description','pack_delivery']
        if fields_trigger_last_modification.intersection(set(validated_data.keys())):
            validated_data['last_modification']=timezone.now().date()
        return super().update(instance,validated_data)    