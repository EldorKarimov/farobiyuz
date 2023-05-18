from rest_framework import serializers

from farobiy.models import Teachers, Courses, Skils, Category, MessageFromUser

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skils
        fields = ('name', 'slug')

class TeacherSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Teachers
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    skils = SkillSerializer(many=True)
    category = CategorySerializer()
    teacher = TeacherSerializer(many=True)
    class Meta:
        model = Courses
        fields = '__all__'

class MessageFromUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageFromUser
        fields = '__all__'