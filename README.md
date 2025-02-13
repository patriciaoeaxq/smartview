# SmartView

SmartView is a Python-based program designed to enhance your typing speed and efficiency on Windows. It allows users to create custom dictionary terms and shortcuts for faster typing.

## Features

- Create custom terms and shortcuts.
- Automatically replace shortcuts with full terms as you type.
- Easy to add or remove shortcuts via a JSON configuration file.
- Runs in the background and waits for shortcuts.

## Requirements

- Python 3.x
- `keyboard` module (install via `pip install keyboard`)

## Installation

1. Make sure you have Python 3.x installed on your system.
2. Install the `keyboard` module by running:
   ```
   pip install keyboard
   ```
3. Download the `smartview.py` file to your local machine.

## Usage

1. Open `smartview.py` in a text editor.
2. Add your custom shortcuts using the `add_term` method:
   ```python
   smartview.add_term('brb', 'be right back')
   smartview.add_term('omw', 'on my way')
   ```
3. Save your changes and run the program:
   ```
   python smartview.py
   ```
4. SmartView will run in the background, replacing your shortcuts with the full terms.
5. Press `ESC` to stop the program.

## Configuration

SmartView uses a JSON file (`custom_terms.json`) to store your shortcuts. You can manually edit this file to add or remove shortcuts. The format is simple:

```json
{
    "shortcut": "expansion"
}
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License.