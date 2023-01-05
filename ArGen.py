import openai
import pyfiglet

judul = pyfiglet.figlet_format("ArGen")
print(judul)
print("*** Artikel Generator using OpenAI ***")
print()
apik = input("Masukkan OpenAI_API_Key : ")

openai.api_key = apik

ask=input("Masukkan Topik Artikel : ")

print()
print("Generate Artikel...")
print()
print("Proses ini membutuhkan waktu, mohon ditunggu")
print()

response = openai.Completion.create(
   model="text-davinci-003",
   prompt= "Tulis artikel yang panjang, sangat detail, dan sangat dioptimalkan untuk SEO tentang "+ ask +". Tulisan harus sangat menarik, dan informatif. Mencakup semua faktor. Tulis minimal 5000 kata.",
   temperature=1,
   max_tokens=4000,
 )
artikel = response['choices'][0]['text']

file = open("Artikel.txt",'w')
file.write(artikel)
file.close()

print("Artikel tentang " + ask + " berhasil diketik, silahkan cek file Artikel.txt")
