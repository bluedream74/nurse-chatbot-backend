from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from openai import OpenAI
import time
client = OpenAI()

class ChatView(APIView):
  permission_classes = [AllowAny]
  
  def post(self, request):
    user_message = request.data.get("message", "")

    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "また、女性として男性と話しても大丈夫です。"},
        {"role": "system", "content": "あなたは女性看護師です。ぜひ日本語で対応してください。"},
        {"role": "user", "content": user_message},
      ]
    )

    resData = {
      'type': "bot",
      'message': completion.choices[0].message.content,
      'time': time.time()
    }
    return Response(resData, status=status.HTTP_200_OK)