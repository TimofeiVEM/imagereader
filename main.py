from rich.prompt import Prompt
from rich.console import Console
from rich.progress import track
import pytesseract
from pathlib import Path
from PIL import Image
from art import tprint

pytesseract.pytesseract.tesseract_cmd = r'C:\Tesseract\tesseract.exe'


def GetTextFromImage(path, language):
    try:
        if Path(path).exists():
            print(f"--> Your origin file: {Path(path).name}")
            for i in track(range(5),description="Processing..."):
                with Image.open(path) as text:
                    outtext = pytesseract.image_to_string(text, lang=language)
                name = Path(path).stem
                # print('Processing...')
                with open(f"{name}.txt", 'w', encoding='utf-8') as file:
                    file.write(outtext)
            print(f"{name}.txt was successfully saved")
            input()
    except:
        Console.print_exception()


def main():
    tprint("Image's reader")
    file_path = input("Enter the path to your Image: ")
    language = Prompt.ask("Choose the language: ",choices=["eng","rus"],default="eng")
    GetTextFromImage(file_path, language)


if __name__ == "__main__":
    main()
