import pyttsx3
import PyPDF2
# *User Input
bookName = input("Enter PDF Book name: ")
bookName+=".pdf"
audioBookName = input("Enter Audio Book name: ")
audioBookName+=".mp3"
# *open PDF
book = open(bookName,'rb')

# *PDF reader 
pdfReader = PyPDF2.PdfReader(book)


# *Number of pages
pages = len(pdfReader.pages)
print(pages)

# *All pages text
allText =""

for pageNum in range(pages):
    page = pdfReader.pages[pageNum]
    text = page.extract_text()
    print(text,'\n')

    allText+=text+" "

# *Initialization Pyttxs3

speaker = pyttsx3.init()

# *Generate Output
speaker.save_to_file(allText, audioBookName)

# *Run the speaker 
speaker.runAndWait()

book.close()

print(f'Audio File Created successfully {audioBookName}')