import openai


openai.api_key = 'API_KEY_OPENAI'

with open('Zadanie dla JJunior AI Developera - tresc artykulu.txt', 'r') as file:
    article_content = file.read()

# creating prompt based on specific requirements
prompt = """
Stwórz kod HTML na podstawie poniższego artykułu. Wymagania:
1. Użyj odpowiednich tagów HTML do strukturyzacji treści (np. <h1>, <h2>, <p>, <ul>, <ol>, <blockquote>).
2. Dodaj w odpowiednie miejsca grafiki jako <img src="image_placeholder.jpg" alt="dokładny prompt służący do wygenerowania grafiki">.
3. Dodaj podpisy pod grafikami używając <figure> i <figcaption>.
4. Brak kodu CSS ani JavaScript.
5. Kod powinien zawierać wyłącznie to, co jest między <body> i </body>. Nie dodawaj <html>, <head>, ani <body>.

Artykuł:
""" + article_content

def comp(PROMPT, MaxToken, outputs):
    
    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",
        # passing the user input 
        prompt=PROMPT,
        # generated output can have "max_tokens" number of tokens 
        max_tokens=MaxToken,
        # number of outputs generated in one call
        n=outputs
    )

    # writing the generated response to a file
    with open('artykul.html', 'w') as file:
        file.write(response.choices[0].text.strip())

comp(prompt, MaxToken=2500, outputs=1)


