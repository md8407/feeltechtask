from attr import fields
from rest_framework import serializers
from .models import User,Inquiry    


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id',"first_name","last_name"]
    
class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = ['id','first_name','last_name','email','contact','subject']

