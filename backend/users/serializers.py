from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username','full_name','email','password','phone']

    def create(self, validated):
        user = User.objects.create_user(
            username=validated['username'],
            email=validated['email'],
            password=validated['password'],
            full_name=validated.get('full_name',''),
            phone=validated.get('phone',''),
        )
        # asigna automáticamente al grupo “Manager Negocio”
        from django.contrib.auth.models import Group
        group, _ = Group.objects.get_or_create(name='Manager Negocio')
        user.groups.add(group)
        return user
