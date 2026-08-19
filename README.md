<a id="readme-top"></a>

![Python](https://img.shields.io/badge/Language-Python_3.11+-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Cross--platform-blue)
![Status](https://img.shields.io/badge/Status-In_Development-green)

<br />
<div align="center">
  <h3 align="center">Snippy</h3>

  <p align="center">
    A lightweight, keyboard-driven text expansion and system automation tool for Windows, macOS, and Linux.
    <br />
    <br />
    <a href="#about-the-project">Explore the docs »</a>
    <br />
    <br />
    <a href="https://github.com/ByteOwn3r/Snippy">View Repository</a>
    &middot;
    <a href="https://github.com/ByteOwn3r/Snippy/issues">Report Bug</a>
    &middot;
    <a href="https://github.com/ByteOwn3r/Snippy/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
## Table of Contents
<ol>
  <li>
    <a href="#about-the-project">About The Project</a>
    <ul>
      <li><a href="#built-with">Built With</a></li>
    </ul>
  </li>
  <li>
    <a href="#getting-started">Getting Started</a>
    <ul>
      <li><a href="#prerequisites">Prerequisites</a></li>
      <li><a href="#installation">Installation</a></li>
      <li><a href="#configuration">Configuration</a></li>
    </ul>
  </li>
  <li><a href="#usage">Usage</a></li>
  <li><a href="#project-architecture">Project Architecture</a></li>
  <li><a href="#license">License</a></li>
  <li><a href="#contact">Contact</a></li>
</ol>

<!-- ABOUT THE PROJECT -->
## About The Project

Snippy is a productivity tool designed to accelerate typing and system interaction. It listens for specific keyboard shortcuts (triggers) and automatically expands them into predefined text, dynamic variables, or system actions. Unlike traditional text expanders, it can execute shell commands and launch applications directly from the keyboard.

### Key Capabilities

| Feature | Description                                                                               | Example |
|-------------------|-------------------------------------------------------------------------------------------|-----------|
| **Text Expansion** | Replaces shortcuts with long-form text.                                                   | `;lorem` $\rightarrow$ Lorem Ipsum... |
| **Dynamic Variables** | Inserts real-time data like dates and times.                                              | `{date}` $\rightarrow$ 19/08/2026 |
| **App Launcher** | Opens system applications (Note: macOS-specific; needs modification for other platforms). | `;open,Safari` $\rightarrow$ Opens Safari |
| **System Commands** | Executes shell commands via shortcuts.                                                    | `.;` $\rightarrow$ runs custom script |
| **Contextual Args** | Supports arguments for dynamic content.                                                   | `;email,1` $\rightarrow$ user@gmail.com |
| **Hot Reload** | Updates the dictionary without restarting.                                                | `;reload` $\rightarrow$ re-reads `dictionary.json` |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

| Category | Technology |
|-----------|------------|
| Language | Python 3.11+ |
| Keyboard Hook | `pynput` |
| OS Integration | `subprocess` (Cross-platform) |
| Dependency Management | `uv` |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

- **Python 3.11** or higher
- **Accessibility Permissions**: The app requires permission to monitor the keyboard (via `pynput`).
- **Optional: macOS**: For better integration on the system and full use of the commands

### Installation

1. **Clone the repo**
   ```sh
   git clone https://github.com/ByteOwn3r/Snippy.git
   cd Snippy
   ```
2. **Install dependencies** (using `uv`)
   ```sh
   uv sync
   ```

### Configuration

Since `dictionary.json` and `Variables.py` contain personal information, they are included in `.gitignore` and not uploaded to the repository. To get the tool working, you must create these files based on the provided examples:

1. **`dictionary.json`** (use `dictionary_example.json` as a template):
   Define your shortcuts and their behavior:
   - `type: "text"`: Expands to the provided value.
   - `type: "open"`: Opens the app provided in the argument (currently macOS-specific).
   - `type: "command"`: Executes a shell command.
2. **`Variables.py`** (use `Variables_example.py` as a template):
   Configure global constants, such as your email list (`EMAILS`) and the absolute path to your `dictionary.json` file.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE -->
## Usage

To start the expansion engine:
```bash
python main.py
```

### Workflow
1. **Trigger**: Type a shortcut defined in your dictionary (e.g., `;addr`).
2. **Activation**: Press the **Space** key.
3. **Expansion**: The tool automatically deletes the trigger and types the expanded text or executes the system action.

**Example with Arguments**:
If you have `;email` configured as `{arg}`, typing `;email,1` followed by **Space** will expand to the first email in your `Variables.py` list.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ARCHITECTURE -->
## Project Architecture

```
├── main.py              # Core engine, keyboard listener, and expansion logic
├── Variables.py          # Global constants and configuration paths
├── dictionary.json       # Mapping of shortcuts to values and actions
├── pyproject.toml        # Project dependencies and metadata
└── uv.lock               # Locked dependency versions
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

ByteOwn3r - [GitHub](https://github.com/ByteOwn3r)

Project Link: [https://github.com/ByteOwn3r/Snippy](https://github.com/ByteOwn3r/Snippy)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
