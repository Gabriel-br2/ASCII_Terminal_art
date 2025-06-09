import cv2
from colors import ANSI_COLORS_RGB

class render:
    """
    A class to convert images into colored ASCII art with additional information.
    """
    def __init__(self, ascii_char="#", output_width=50, image_file="test.jpg",
                 margin_right_for_list=8, list_start_line=4, info_list=None):
        """
        Initializes the ImageToAsciiConverter class with default settings.

        Args:
            ascii_char (str): The ASCII character to use in the conversion.
            output_width (int): The desired width of the ASCII output.
            image_file (str): The path to the image file.
            margin_right_for_list (int): Right margin for the information list.
            list_start_line (int): The starting line of the information list in the ASCII output.
            info_list (list): A list of tuples containing information to be displayed.
        """
        self.RESET = "\033[0m"

        self.ASCII_CHAR = ascii_char
        self.OUTPUT_WIDTH = output_width
        self.IMAGE_FILE = image_file
        self.MARGIN_RIGHT_FOR_LIST = margin_right_for_list
        self.LIST_START_LINE = list_start_line
        self.INFO_LIST = info_list if info_list is not None else []

    def _find_nearest_ansi_color(self, r, g, b):
        """
        Recebe uma cor RGB e retorna o código ANSI mais próximo baseado na menor distância euclidiana.
        """
        min_dist = float('inf')
        nearest_code = self.RESET  # valor padrão

        for value in ANSI_COLORS_RGB.values():
            ansi_code, (cr,cg,cb) = value["ansi"], value["rgb"]
            
            dist = (r - cr)**2 + (g - cg)**2 + (b - cb)**2
            if dist < min_dist:
                min_dist = dist
                nearest_code = ansi_code

        return nearest_code

    def _get_ansi_color_and_char(self, b, g, r):
        """
        Mapeia uma cor RGB para o código ANSI mais próximo.
        Se o pixel for muito escuro, retorna espaço em branco.
        """
        brightness = (int(r) * 299 + int(g) * 587 + int(b) * 114) / 1000

        if brightness < 30:
            return "", " "

        color_code = self._find_nearest_ansi_color(r, g, b)
        return color_code, self.ASCII_CHAR

    def convert_image_to_colored_ascii(self):
        """
        Converts the image configured in the class into ASCII art where the character is colored,
        black (background) is represented by a space, and adds an information list to the right.
        """
        img = cv2.imread(self.IMAGE_FILE)
        if img is None:
            print(f"Error: Could not load the image from {self.IMAGE_FILE}")
            return

        try:
            aspect_ratio = img.shape[0] / img.shape[1]
            self.output_height = int(self.OUTPUT_WIDTH * aspect_ratio * 0.55)

            img_resized = cv2.resize(img, (self.OUTPUT_WIDTH, self.output_height), interpolation=cv2.INTER_AREA)
            
            # The list goes up to (self.output_height - 5) lines to have a bottom margin
            self.list_end_line_dynamic = self.output_height - 5 
            
            ascii_output = []
            for r in range(self.output_height):
                row_chars = []
                
                # ASCII Art part of the image
                for c in range(self.OUTPUT_WIDTH):
                    b, g, r_pixel = img_resized[r, c]
                    color_code, char_to_print = self._get_ansi_color_and_char(b, g, r_pixel)
                    row_chars.append(f"{color_code}{char_to_print}{self.RESET}")
                
                # Add margin for the list
                row_chars.append(" " * self.MARGIN_RIGHT_FOR_LIST)

                # Add list information if the line is within the range
                if self.LIST_START_LINE <= r < self.list_end_line_dynamic:
                    info_index = r - self.LIST_START_LINE
                    if info_index < len(self.INFO_LIST):
                        info_name, info_name_color, info_value, info_value_color = self.INFO_LIST[info_index]
                        info_string = f"{ANSI_COLORS_RGB[info_name_color]['ansi']}{info_name}:{self.RESET} {ANSI_COLORS_RGB[info_value_color]['ansi']}{info_value}{self.RESET}"
                        row_chars.append(info_string)
                
                ascii_output.append("".join(row_chars))

            for line in ascii_output:
                print(line)
            print(self.RESET) # Reset all colors at the end

        except FileNotFoundError:
            print(f"Error: The file '{self.IMAGE_FILE}' was not found. Please check the path: {self.IMAGE_FILE}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def debug_msg(self):
        print(f"\nASCII art generated for '{self.IMAGE_FILE}' with a width of {self.OUTPUT_WIDTH} characters, using '{self.ASCII_CHAR}'.")
        print(f"ASCII art height: {self.output_height} lines.")
        print(f"Information list displayed from line {self.LIST_START_LINE + 1} to line {self.list_end_line_dynamic} (indices {self.LIST_START_LINE} to {self.list_end_line_dynamic -1}).")


if __name__ == "__main__":
    info_project_list = [
        ("Project Name", "RED", "Digital Twin", "WHITE"),
        ("Status", "RED", "In Progress", "BLUE"), 
        ("Project ID", "RED", "DT-2025-001", "ORANGE"),
    ]

    converter = render(
        ascii_char="#",
        output_width=50,
        image_file="teste.png",
        margin_right_for_list=10,
        list_start_line=2,
        info_list=info_project_list
    )

    converter.convert_image_to_colored_ascii()
    converter.debug_msg()