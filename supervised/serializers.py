from rest_framework import serializers
from .models import SupervisedPack

class SupervisedPackSerializer(serializers.ModelSerializer):
    class Meta:
        model=SupervisedPack
        fields='__all__'
        read_only_fields=['created_at']
    def validate(self,data):
        request=self.context['request']
        user=request.user
        if self.instance is None:
            if user.account_type !='USER':
                raise seriliazer.validationaError('Only Users caj Create Supervised Packages !')
        if self.instance :
            if user.account_type != 'USER':
                raise serializers.ValidationError('Only Guardians Can Update Supervised Packages ! ')
        return data
    
    