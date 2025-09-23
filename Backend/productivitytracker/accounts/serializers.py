from rest_framework import serializers
from .models import Profile

class Profile_Serializer(serializers.ModelSerializers):
    class Meta:
        model = Profile
        fields = ['id','username','email','role','password']
        extra_kwargs = {'password' : {'write_only' : True}}

        def create(self, validated_data):
            profile = Profile(
                username=validated_data['username'],
                email=validated_data['email'],
                role=validated_data['role']
            )

            profile.set_password(validated_data['password'])
            profile.save()
            return profile
        

        