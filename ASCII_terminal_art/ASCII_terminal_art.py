import cv2

class ASCII_terminal_art:
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
        self.ASCII_CHAR = ascii_char
        self.OUTPUT_WIDTH = output_width
        self.IMAGE_FILE = image_file
        self.MARGIN_RIGHT_FOR_LIST = margin_right_for_list
        self.LIST_START_LINE = list_start_line
        self.INFO_LIST = info_list if info_list is not None else []

        # ANSI color codes
        self.RESET = "\033[0m"
        self.FG_RED = "\033[31m"
        self.FG_BLUE = "\033[34m"
        self.FG_ORANGE = "\033[33m"
        self.FG_DARK_GRAY = "\033[90m"
        self.FG_LIGHT_GRAY = "\033[37m"
        self.FG_WHITE = "\033[97m"
        self.FG_GREEN = "\033[32m" 

    def _get_ansi_color_and_char(self, b, g, r):
        """
        Maps an RGB color to an ANSI foreground color code and the character to use.
        If the pixel is very dark (considered black/background), it returns a blank space.
        """
        brightness = (int(r) * 299 + int(g) * 587 + int(b) * 114) / 1000

        if brightness < 30: # Threshold to consider "black" (background)
            return "", " "  # Empty color code and a blank space

        if r > 150 and g < 100 and b < 100:
            return self.FG_RED, self.ASCII_CHAR
        if r > 200 and g > 100 and b < 50:
            return self.FG_ORANGE, self.ASCII_CHAR
        if b > 100 and g < 100 and r < 100:
            return self.FG_BLUE, self.ASCII_CHAR
        if g > 100 and r < 100 and b < 100: # Example of adding green color
            return self.FG_GREEN, self.ASCII_CHAR

        if brightness < 150:
            return self.FG_DARK_GRAY, self.ASCII_CHAR
        elif brightness < 200:
            return self.FG_LIGHT_GRAY, self.ASCII_CHAR
        else:
            return self.FG_LIGHT_GRAY, self.ASCII_CHAR

    def convert_image_to_colored_ascii(self):
        """
        Converts the image configured in the class into ASCII art where the character is colored,
        black (background) is represented by a space, and adds an information list to the right.
        """
        img = cv2.imread(self.IMAGE_FILE)
            #if img is None:
            #    print(f"Error: Could not load the image from {self.IMAGE_FILE}")
            #    return

        try:
            aspect_ratio = img.shape[0] / img.shape[1]
            output_height = int(self.OUTPUT_WIDTH * aspect_ratio * 0.55)

            img_resized = cv2.resize(img, (self.OUTPUT_WIDTH, output_height), interpolation=cv2.INTER_AREA)
            
            # The list goes up to (output_height - 5) lines to have a bottom margin
            list_end_line_dynamic = output_height - 5 
            
            ascii_output = []
            for r in range(output_height):
                row_chars = []
                
                # ASCII Art part of the image
                for c in range(self.OUTPUT_WIDTH):
                    b, g, r_pixel = img_resized[r, c]
                    color_code, char_to_print = self._get_ansi_color_and_char(b, g, r_pixel)
                    row_chars.append(f"{color_code}{char_to_print}{self.RESET}")
                
                # Add margin for the list
                row_chars.append(" " * self.MARGIN_RIGHT_FOR_LIST)

                # Add list information if the line is within the range
                if self.LIST_START_LINE <= r < list_end_line_dynamic:
                    info_index = r - self.LIST_START_LINE
                    if info_index < len(self.INFO_LIST):
                        info_name, info_name_color, info_value, info_value_color = self.INFO_LIST[info_index]
                        info_string = f"{info_name_color}{info_name}:{self.RESET} {info_value_color}{info_value}{self.RESET}"
                        row_chars.append(info_string)
                
                ascii_output.append("".join(row_chars))

            for line in ascii_output:
                print(line)
            print(self.RESET) # Reset all colors at the end

            # print(f"\nASCII art generated for '{self.IMAGE_FILE}' with a width of {self.OUTPUT_WIDTH} characters, using '{self.ASCII_CHAR}'.")
            # print(f"ASCII art height: {output_height} lines.")
            # print(f"Information list displayed from line {self.LIST_START_LINE + 1} to line {list_end_line_dynamic} (indices {self.LIST_START_LINE} to {list_end_line_dynamic -1}).")

        except FileNotFoundError:
            print(f"Error: The file '{self.IMAGE_FILE}' was not found. Please check the path: {self.IMAGE_FILE}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Define the information list here
    info_project_list = [
        ("Project Name", "\033[31m", "Digital Twin", "\033[97m"), # FG_RED, FG_WHITE
        ("Status", "\033[31m", "In Progress", "\033[34m"), # FG_RED, FG_BLUE
        ("Project ID", "\033[31m", "DT-2025-001", "\033[33m"), # FG_RED, FG_ORANGE
        ("Start Date", "\033[31m", "01/06/2025", "\033[97m"),
        ("Responsible", "\033[31m", "Alpha Team", "\033[97m"),
        ("Current Version", "\033[31m", "1.2.0 Beta", "\033[97m"),
        ("Next Step", "\033[31m", "Testing Phase", "\033[97m"),
        ("Budget (R$)", "\033[31m", "500.000,00", "\033[33m"),
        ("Overall Progress", "\033[31m", "75%", "\033[34m"),
        ("Team Involved", "\033[31m", "15 Members", "\033[97m"),
        ("Location", "\033[31m", "Rio Grande, RS", "\033[97m"), 
        ("Deadline", "\033[31m", "31/12/2025", "\033[31m"),
        ("Allocated Resources", "\033[31m", "Cloud/Local", "\033[97m"),
        ("Priority", "\033[31m", "High", "\033[33m"),
        ("Identified Risks", "\033[31m", "Medium", "\033[31m"),
        ("Last Update", "\033[31m", "07/06/2025 14:10", "\033[37m"),
    ]

    # Create an instance of the ImageToAsciiConverter class
    # and pass all desired parameters
    converter = ASCII_terminal_art(
        ascii_char="#", # Example: Use '*' instead of '#'
        output_width=50, # Example: Increase output width
        image_file="teste.png",
        margin_right_for_list=10, # Example: Increase margin
        list_start_line=2, # Example: Start the list earlier
        info_list=info_project_list
    )

    # Call the method to perform the conversion
    converter.convert_image_to_colored_ascii()