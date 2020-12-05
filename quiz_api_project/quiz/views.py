from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Quizzes, Question
from .serializers import QuizSerializer, RandomQuestionSerializer


# Create your views here.
class Quiz(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()


class RandomQuestion(APIView):
    def get(self, requeest, format=None, **kwargs):
        #here 'topic' is a key === Quiz.title
        question = Question.objects.filter(
            quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)
