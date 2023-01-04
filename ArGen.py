import os
import openai

print("Artikel Generator using OpenAI")
print()

#Ubah YOUR_OPENAI_API dengan OpenAI API
openai.api_key = "YOUR_OPENAI_API"

ask=input("Masukkan Topik Artikel : ")
print()
print("Generate Artikel...")
print()
response = openai.Completion.create(
   model="text-davinci-003",
   prompt= "Buatkan artikel seo friendly tentang "+ ask,
   temperature=0.9,
   max_tokens=2000,
   top_p=1,
   frequency_penalty=0,
   presence_penalty=0.6,
   stop=[" Human:", " AI:"]
 )
text = response['choices'][0]['text']

file = open("Artikel.txt",'w')
file.write(text)
file.close()

print("Artikel berhasil diketik, silahkan cek file Artikel.txt")
