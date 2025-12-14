from rest_framework import serializers
from .models import SupervisedPack

class SupervisedPackSerializer(serializers.ModelSerializer):
    class Meta:
        model=SupervisedPack
        fields='__all__'
        read_only_fields=['created_at','pack_name','gu_id','usr_id','ben_id','pck_id',]
    def validate(self,data):
        request=self.context['request']
        user=request.user
        if self.instance is None:
            if user.account_type !='USER':
                raise serializers.ValidationError('Only Users caj Create Supervised Packages !')
            pack=data.get('package')
            if pack.pack_delivery !='Guardian':
                raise serializers.ValidationError('Package is not Marked for Guardian Delivery ! ')
            if pack.owner_id != user.reg_id:
                raise serializers.ValidationError('You Do not Own This Package')
            data['supervision_status'] = 'Draft'
        else:
            if user.account_type !='GUARDIAN':
                raise serializers.ValidationError('Only Guardian can Update Supervision')
        return data
    
    