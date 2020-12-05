from rest_framework import serializers
from .models import Quizzes, Question

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quizzes
        fields = [
            'title',
        ]

class RandomQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        # here answer field doesn't exist.
        # but djangp still manages to show response 
        fields = [
            'title',
            'answer'
        ]
