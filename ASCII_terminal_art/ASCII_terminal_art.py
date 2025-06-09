import cv2

ANSI_COLORS_RGB = {
    "BLACK":         {"ansi": "\033[30m", "rgb": (0, 0, 0)},
    "RED":           {"ansi": "\033[31m", "rgb": (255, 0, 0)},
    "GREEN":         {"ansi": "\033[32m", "rgb": (0, 255, 0)},
    "YELLOW":        {"ansi": "\033[33m", "rgb": (255, 255, 0)},
    "BLUE":          {"ansi": "\033[34m", "rgb": (0, 0, 255)},
    "MAGENTA":       {"ansi": "\033[35m", "rgb": (255, 0, 255)},
    "CYAN":          {"ansi": "\033[36m", "rgb": (0, 255, 255)},
    "WHITE":         {"ansi": "\033[37m", "rgb": (192, 192, 192)},

    "BRIGHT_BLACK":  {"ansi": "\033[90m", "rgb": (105, 105, 105)},
    "BRIGHT_RED":    {"ansi": "\033[91m", "rgb": (255, 85, 85)},
    "BRIGHT_GREEN":  {"ansi": "\033[92m", "rgb": (85, 255, 85)},
    "BRIGHT_YELLOW": {"ansi": "\033[93m", "rgb": (255, 255, 85)},
    "BRIGHT_BLUE":   {"ansi": "\033[94m", "rgb": (85, 85, 255)},
    "BRIGHT_MAGENTA":{"ansi": "\033[95m", "rgb": (255, 85, 255)},
    "BRIGHT_CYAN":   {"ansi": "\033[96m", "rgb": (85, 255, 255)},
    "BRIGHT_WHITE":  {"ansi": "\033[97m", "rgb": (255, 255, 255)},

    "ORANGE":        {"ansi": "\033[38;5;208m", "rgb": (255, 165, 0)},
    "PINK":          {"ansi": "\033[38;5;213m", "rgb": (255, 192, 203)},
    "VIOLET":        {"ansi": "\033[38;5;177m", "rgb": (238, 130, 238)},
    "TURQUOISE":     {"ansi": "\033[38;5;80m", "rgb": (64, 224, 208)},
    "AQUA":          {"ansi": "\033[38;5;87m", "rgb": (0, 255, 255)},
    "SALMON":        {"ansi": "\033[38;5;216m", "rgb": (250, 128, 114)},
    "LIME":          {"ansi": "\033[38;5;154m", "rgb": (191, 255, 0)},
    "PEACH":         {"ansi": "\033[38;5;223m", "rgb": (255, 218, 185)},
    "BROWN":         {"ansi": "\033[38;5;94m", "rgb": (139, 69, 19)},
    "GOLD":          {"ansi": "\033[38;5;220m", "rgb": (255, 215, 0)},

    "DARK_RED":      {"ansi": "\033[38;5;88m", "rgb": (139, 0, 0)},
    "DARK_GREEN":    {"ansi": "\033[38;5;22m", "rgb": (0, 100, 0)},
    "DARK_BLUE":     {"ansi": "\033[38;5;18m", "rgb": (0, 0, 139)},
    "DARK_MAGENTA":  {"ansi": "\033[38;5;89m", "rgb": (139, 0, 139)},
    "DARK_CYAN":     {"ansi": "\033[38;5;30m", "rgb": (0, 139, 139)},
    "DARK_GRAY":     {"ansi": "\033[38;5;236m", "rgb": (64, 64, 64)},
    "LIGHT_GRAY":    {"ansi": "\033[38;5;250m", "rgb": (211, 211, 211)},
    "SLATE_GRAY":    {"ansi": "\033[38;5;66m", "rgb": (112, 128, 144)},
    "SKY_BLUE":      {"ansi": "\033[38;5;117m", "rgb": (135, 206, 235)},
    "LAVENDER":      {"ansi": "\033[38;5;183m", "rgb": (230, 230, 250)},

    "MINT":          {"ansi": "\033[38;5;121m", "rgb": (189, 252, 201)},
    "INDIGO":        {"ansi": "\033[38;5;54m", "rgb": (75, 0, 130)},
    "CORAL":         {"ansi": "\033[38;5;209m", "rgb": (255, 127, 80)},
    "IVORY":         {"ansi": "\033[38;5;230m", "rgb": (255, 255, 240)},
    "NAVY":          {"ansi": "\033[38;5;17m", "rgb": (0, 0, 128)},
    "TEAL":          {"ansi": "\033[38;5;37m", "rgb": (0, 128, 128)},
    "ROSE":          {"ansi": "\033[38;5;211m", "rgb": (255, 228, 225)},
    "SAND":          {"ansi": "\033[38;5;180m", "rgb": (244, 164, 96)},
    "CHARCOAL":      {"ansi": "\033[38;5;240m", "rgb": (54, 69, 79)},
    "BEIGE":         {"ansi": "\033[38;5;223m", "rgb": (245, 245, 220)},

    "OLIVE":         {"ansi": "\033[38;5;58m", "rgb": (128, 128, 0)},
    "MAROON":        {"ansi": "\033[38;5;52m", "rgb": (128, 0, 0)},
    "PLUM":          {"ansi": "\033[38;5;176m", "rgb": (221, 160, 221)},
    "FUCHSIA":       {"ansi": "\033[38;5;201m", "rgb": (255, 0, 255)},
    "PERIWINKLE":    {"ansi": "\033[38;5;147m", "rgb": (204, 204, 255)}
}


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
            ansi_code, (cr, cg, cb) = value["ansi"], value["rgb"]
            
            cr = float(cr)
            cg = float(cg)
            cb = float(cb)

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
        try:
            print(f"\nASCII art generated for '{self.IMAGE_FILE}' with a width of {self.OUTPUT_WIDTH} characters, using '{self.ASCII_CHAR}'.")
            print(f"ASCII art height: {self.output_height} lines.")
            print(f"Information list displayed from line {self.LIST_START_LINE + 1} to line {self.list_end_line_dynamic} (indices {self.LIST_START_LINE} to {self.list_end_line_dynamic -1}).")
        except:
            print("No image generated")

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
    #converter.debug_msg()