from rest_framework import serializers
from .models import Quizzes, Question, Answer


class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quizzes
        fields = [
            'title',
        ]

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:

        model = Answer
        fields = [
            'id',
            'answer_text',
            'is_right',
        ]

class RandomQuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)

    # here answer field doesn't exist.
    # but djangp still manages to show response
    # now answer links to AnswerSerializer fields
    class Meta:

        model = Question
        fields = [
            'title','answer',
        ]


class QuestionSerializer(serializers.ModelSerializer):

    quiz = QuizSerializer(read_only=True)
    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:

        model = Question
        fields = [
            'quiz','title','answer', 'difficulty'
        ]
        # fields = '__all__'
