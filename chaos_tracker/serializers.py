from rest_framework import serializers
from .models import Employee, Interaction

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class InteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaction
        fields = '__all__'

    def create(self, validated_data):
        employee1 = validated_data.get('employee1')
        employee2 = validated_data.get('employee2')
        chaos_points = validated_data.get('chaos_points', 0)  # Default to 0 if missing

        # Ensure employee1 and employee2 are valid instances before updating
        if employee1 and employee2:
            employee1.chaos_level = max(0, employee1.chaos_level + chaos_points)
            employee2.chaos_level = max(0, employee2.chaos_level + chaos_points)

            # Save updated chaos levels
            employee1.save()
            employee2.save()

        return super().create(validated_data)
