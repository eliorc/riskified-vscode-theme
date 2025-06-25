# Riskified Theme for VS Code

![Riskified Logo](https://cdn.prod.website-files.com/650ab8997a4c369432cfd6c6/6513d81fc2c42abfdec205c0_logo%20positive.png)

A Visual Studio Code theme inspired by Riskified's branding. This pack includes two themes:

*   **Riskified Dark**: The primary dark theme.
*   **Riskified Dark Purple**: A variation with purple accents.

## Installation

1.  Open **Extensions** sidebar panel in VS Code. `View → Extensions`
2.  Search for `Riskified Theme`.
3.  Click **Install** to install it.
4.  Click **Reload** to reload your editor.
5.  Code > Preferences > Color Theme > **Riskified Dark** or **Riskified Dark Purple**.
    (Or `File > Preferences > Color Theme` on Windows/Linux)

## Activating Theme

You can activate the theme through the command palette or your settings:

**Command Palette:**

1.  Open the Command Palette (Ctrl+Shift+P or Cmd+Shift+P).
2.  Type `Preferences: Color Theme` and select it.
3.  Choose either "Riskified Dark" or "Riskified Dark Purple" from the list.

**Settings:**

1.  Open your VS Code `settings.json` file.
2.  Set the `workbench.colorTheme` property to either `"Riskified Dark"` or `"Riskified Dark Purple"`:

    ```json
    {
      "workbench.colorTheme": "Riskified Dark"
    }
    ```
    or
    ```json
    {
      "workbench.colorTheme": "Riskified Dark Purple"
    }
    ```

## Screenshots

*(Coming Soon! Add screenshots of the themes in action here.)*

## Customization

If you wish to customize the theme further, you can do so by modifying your `settings.json` file. VS Code provides various settings to tweak the editor's appearance. For example, you can override specific theme colors:

```json
{
  "workbench.colorCustomizations": {
    "[Riskified Dark]": { // Or "[Riskified Dark Purple]"
      "editor.background": "#1E1E1E", // Example: Change background color
      "activityBar.background": "#252526"
    }
  },
  "editor.tokenColorCustomizations": {
    "[Riskified Dark]": { // Or "[Riskified Dark Purple]"
        "comments": "#55DD55" // Example: Change comment color
    }
  }
}
```

For more details, refer to the [VS Code Theme Color Reference](https://code.visualstudio.com/api/references/theme-color) and [Syntax Highlight Guide](https://code.visualstudio.com/api/language-extensions/syntax-highlight-guide).

## Disclaimer

This theme is an independent project created by a Riskified employee and is not an official Riskified product. It is not supported by Riskified, and Riskified has no responsibility or liability for this theme. All views and work are my own.

## Feedback and Contributions

Found a bug or have a suggestion? Please [open an issue](https://github.com/your-github-username/riskified-vscode-theme/issues) on GitHub. (Please replace with your actual repository URL)

Contributions are welcome! Fork the repository and submit a pull request.

## License

This theme is released under the [MIT License](LICENSE). (You might want to add a `LICENSE` file to your project.)
