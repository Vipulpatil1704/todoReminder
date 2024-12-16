from rest_framework import serializers
from bson import ObjectId
from .models import Task

class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        # Convert ObjectId to string when sending data to the client
        return str(value) if value else None

    def to_internal_value(self, data):
        # Convert string back to ObjectId when receiving data from the client
        if ObjectId.is_valid(data):
            return ObjectId(data)
        raise serializers.ValidationError("Invalid ObjectId format.")
    
class TaskSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        # Automatically generate an _id if it isn't provided (for test environments)
        if '_id' not in validated_data or not validated_data['_id']:  # Check if _id is empty or not provided
            validated_data['_id'] = ObjectId()  # Generate a new ObjectId
        return super().create(validated_data)