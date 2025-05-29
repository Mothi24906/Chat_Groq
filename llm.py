from groq import Groq

client=Groq(api_key='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')

stream=client.chat.completions.create(

  messages=[
    {  #system's role 
      'role':"system",
      'content':"You are an helpful assitant"

    },
    {
      #user's role
      'role':"user",
      'content':"How to become a pro in solving dsa problems"


    }
  ],

  #defining model and version
  model="llama-3.3-70b-versatile",

  #defining additional paramters
  temperature=0.5,

  max_completion_tokens=1024,

  top_p=1,

  stop=None,

  stream=True,







)

for chunk in stream:
  print(chunk.choices[0].delta.content, end="")