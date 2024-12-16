from rest_framework import serializers
from bson import ObjectId
from .models import Task

class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value) if value else None

    def to_internal_value(self, data):
        if ObjectId.is_valid(data):
            return ObjectId(data)
        raise serializers.ValidationError("Invalid ObjectId format.")
    
class TaskSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        if '_id' not in validated_data or not validated_data['_id']: 
            validated_data['_id'] = ObjectId() 
        return super().create(validated_data)