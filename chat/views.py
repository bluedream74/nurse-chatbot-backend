from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from openai import OpenAI
import time
import random
client = OpenAI()

emoji_str = ["❣️", "❤️", "🤐", "💗", '💜', "😍", "🥰", "🧑", "💉", "🛀", '🏨']

class ChatView(APIView):
  permission_classes = [AllowAny]
  
  def post(self, request):
    user_message = request.data.get("message", "")

    completion = client.chat.completions.create(
      model="ft:gpt-3.5-turbo-0125:a::9OOtFQ3D",
      messages=[
        {"role": "user", "content": user_message},
      ]
    )

    randomIndex = random.randint(0, 11)
    print(randomIndex)
    resData = {
      'type': "bot",
      'message': completion.choices[0].message.content + emoji_str[randomIndex],
      'time': time.time()
    }
    return Response(resData, status=status.HTTP_200_OK)