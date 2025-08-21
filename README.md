
# 🖼️ ASCII Terminal Art Generator

## Project Description
This project provides a Python-based utility to convert images into colored ASCII art, displaying the output directly in the terminal. Beyond simple conversion, it intelligently maps image colors to ANSI escape codes for vibrant terminal output and includes the capability to embed a dynamic information list alongside the generated ASCII art.

## System Behavior

The `ASCII_terminal_art` class takes an image file and several configuration parameters as input. It resizes the image based on the desired output width, maintaining its aspect ratio. Each pixel in the resized image is then analyzed for its RGB values. Based on the pixel's brightness and color dominance, an appropriate ANSI foreground color and a specified ASCII character (or a blank space for very dark pixels) are selected. The converted colored ASCII characters are then assembled row by row. Crucially, the system also integrates a user-defined information list, displaying it dynamically to the right of the ASCII art, creating a rich, informative visual in the terminal.

---

## Code Structure 🏗️
The project consists of a single Python file:

* `ASCII_terminal_art.py`: This file contains the `ASCII_terminal_art` class, which encapsulates all the logic for image conversion, color mapping, and terminal output. 

    * `ASCII_terminal_art` class:
        * `__init__`: Constructor for initializing class parameters, including the ASCII character, output width, image file path, list positioning, and ANSI color codes.
        * `_get_ansi_color_and_char`: A private helper method that maps RGB pixel values to ANSI foreground color codes and determines if the ASCII character or a space should be used.
        * `convert_image_to_colored_ascii`: The main method responsible for loading, resizing and processing the image. 
        * `show`: Method responsible for printing the colored ASCII art with the embedded information list.
---

## Configuration Structure ⚙️
The system is highly configurable through the parameters passed to the `ASCII_terminal_art` class constructor:

* **`ascii_char`**: The character used to represent pixels in the ASCII art (e.g., `#`, `*`, `@`). Default is `#`.
* **`output_width`**: The desired width of the ASCII art in characters. The height is automatically calculated to maintain aspect ratio. Default is `50`.
* **`image_file`**: The path to the input image file (e.g., `test.jpg`, `teste.png`). Default is `test.jpg`.
* **`margin_right_for_list`**: The number of spaces to add between the ASCII art and the information list. Default is `8`.
* **`list_start_line`**: The line number (0-indexed) where the information list begins in the ASCII output. Default is `4`.
* **`info_list`**: A list of tuples, where each tuple represents an item in the information list. Each tuple should contain:
    * `info_name` (str): The name of the information field.
    * `info_name_color` (str): ANSI color code for the info name.
    * `info_value` (str): The value of the information field.
    * `info_value_color` (str): ANSI color code for the info value.

**Example Configuration:**

```python
import ASCII_terminal_art

info_project_list = [
    ("Project Name", "\033[31m", "DT", "\033[97m"),
    ("Status", "\033[31m", "In Progress", "\033[34m"),
    # ... more items
]

converter = ASCII_terminal_art(
    ascii_char="#",
    output_width=50,
    image_file="test.png",
    margin_right_for_list=10,
    list_start_line=2,
    info_list=info_project_list
)

converter.convert_image_to_colored_ascii()
converter.show() 

```

---

## Notes 📝
* **Terminal Compatibility**: The colored output relies on ANSI escape codes. Ensure your terminal supports ANSI color codes for proper display. Most modern terminals do.
* **OpenCV Dependency**: This project requires `opencv-python` to be installed. You can install it via pip: `pip install opencv-python`.
* **Image File Path**: Always double-check the `image_file` path. The script will print an error if the file is not found.
* **Aspect Ratio Correction**: A factor of `0.55` is applied to the calculated `output_height` (`output_height = int(self.OUTPUT_WIDTH * aspect_ratio * 0.55)`) to account for the non-square nature of terminal characters, which are typically taller than they are wide. This helps prevent the ASCII art from appearing stretched.
* **List Display Range**: The `info_list` will be displayed from `list_start_line` up to `output_height - 5` to ensure a small bottom margin.

---

## Common Errors 🐛
* **`FileNotFoundError`**:
    * **Cause**: The `image_file` path provided does not point to an existing image.
    * **Solution**: Verify the image path and filename, ensuring it's correct and the file is accessible from where the script is run.
* **`AttributeError: 'NoneType' object has no attribute 'shape'`**:
    * **Cause**: This usually occurs when `cv2.imread()` fails to load the image, returning `None`. This can be due to a corrupt image, an unsupported image format, or the `FileNotFoundError` not being caught earlier (though the current code has a `try-except` for `FileNotFoundError`).
    * **Solution**: Ensure the image file is not corrupted and is in a format supported by OpenCV (e.g., JPG, PNG, BMP). Double-check the path.
* **No Colors in Terminal**:
    * **Cause**: Your terminal emulator might not support ANSI escape codes, or support is disabled.
    * **Solution**: Try running the script in a different terminal (e.g., Git Bash on Windows, or any modern Linux/macOS terminal). Ensure your terminal settings allow ANSI colors.
* **ASCII Art looks stretched/squished**:
    * **Cause**: The `0.55` aspect ratio correction factor in `output_height` calculation might not be perfect for all fonts/terminals.
    * **Solution**: Experiment with the `0.55` value in `output_height = int(self.OUTPUT_WIDTH * aspect_ratio * 0.55)` to find a value that visually suits your terminal and font.

---

## Version 🏷️
* **Current Version**: 1.0.0 Beta
* **Version History**:
    * **1.0.0 Alpha**: Initial release with basic image-to-ASCII conversion.

---

## Team 👥
* **Author**: Gabriel Rocha de Souza   

"Transforming pixels into purpose, one character at a time."
