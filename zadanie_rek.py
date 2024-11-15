import openai

openai.api_key = '<API_KEY>'

# file paths
input_file_path = "Zadanie dla JJunior AI Developera - tresc artykulu.txt"
output_file_path = "artykul.html"

def read_input_file(file_path):
    # reading given .txt file on which AI response will be based
    try:
        with open(file_path, 'r') as file:
            return file.read()
        
    except FileNotFoundError:
        print("File not found")
        return None

# function saving html content to a file
def save_file(file_path, html_content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)


# function returning AI response based on given prompt
def generate_AI_response(article_content, max_token, temp):

    # creating prompt based on specific requirements
    prompt = """
    Stwórz kod HTML na podstawie poniższego artykułu. Wymagania:
    1. Użyj odpowiednich tagów HTML do strukturyzacji treści.
    2. Dodaj w odpowiednie miejsca grafiki jako <img src="image_placeholder.jpg" alt="dokładny prompt służący do wygenerowania grafiki">.
    3. Dodaj podpisy pod grafikami używając <figure> i <figcaption>.
    4. Brak kodu CSS ani JavaScript.
    5. Nie dodawaj <html>, <head>, ani <body>, ani innych nie wymaganych oznaczeń, że jest to kod html.
    6. Kod powinien zawierać wyłącznie to, co jest między <body> i </body>.

    Artykuł:
    """ + article_content

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Jesteś ekspertem w generowaniu strukturalnego kodu HTML."},
            {"role": "user", "content": prompt}
        ],
        temperature=temp,
        max_tokens=max_token,
    )

    return response.choices[0].message.content


if __name__ == "__main__":

    input_file_content = read_input_file(input_file_path)
    output_file_content = generate_AI_response(input_file_content, max_token=3000, temp=0.3)
    save_file(output_file_path, output_file_content)



