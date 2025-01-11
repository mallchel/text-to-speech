from ebooklib import epub
from bs4 import BeautifulSoup
# import codecs


def extract_text_from_epub(file_path):
    book = epub.read_epub(file_path)
    text_content = []
    for item in book.get_items():
        if item.get_type() == 9:
            soup = BeautifulSoup(item.content, 'html.parser')
            text_content.append(soup.get_text())
    return '\n'.join(text_content)


# Path to your .epub file
epub_file_path = 'assets/sample1.epub'
text = extract_text_from_epub(epub_file_path)

# Save the extracted text to a file
# with codecs.open('sample1.text', 'w', encoding='utf-8') as f:
with open('assets/sample1.txt', 'w', encoding='utf-8') as f:
    f.write(text)

print("Text extracted and saved to 'assets/sample1.txt'")
