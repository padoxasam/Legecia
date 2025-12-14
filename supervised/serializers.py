from rest_framework import serializers
from .models import SupervisedPack

class SupervisedPackSerializer(serializers.ModelSerializer):
    class Meta:
        model=SupervisedPack
        fields='__all__'
        read_only_fields=['created_at','supervision_status']
    def validate(self,data):
        request=self.context['request']
        user=request.user
        if self.instance is None:
            if user.active_role != 'USER':
                raise serializers.ValidationError(
                    'Only USER role can create supervision requests.')
            pack = data.get('pack')

            if pack.pack_delivery != 'Guardian':
                raise serializers.ValidationError('Package is not marked for Guardian delivery.')
            if pack.owner_id != user.id:
                raise serializers.ValidationError('You do not own this package.')
            data['user'] = user
            data['supervision_status'] = 'Draft'

        else:
            if user.active_role != 'GUARDIAN':
                raise serializers.ValidationError('Only Guardian can Update Supervision')
        return data
    
    