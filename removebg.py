from rembg import remove
from PIL import Image


class RemoveBackGround:

    def __init__(self, input_path:str, output_path:str) -> None:
        self.input_path = input_path
        self.output_path = output_path

    def remove_bg(self):
        input = Image.open(self.input_path)
        rgb_im = input.convert('RGB')
        rgb_im = remove(input)
        rgb_im.save(self.output_path)


