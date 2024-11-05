import re
def clean_html(input_file, output_file="cleaned_output.txt"):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    cleaned_text = re.sub(r'<[^>]+>', '', content)
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(cleaned_text)

    print(f"Очищений текст записано у файл {output_file}")
