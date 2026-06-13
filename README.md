# Automated File Organizer Utility

A production-grade Python automation tool designed to clean up cluttered directories (such as Downloads or Desktop) by scanning and organizing files into structured folders based on their file extensions.

## 🌟 Key Features

- **Dynamic Industry-Standard Mapping**: Automatically categorizes files into dedicated folders including Documents, Images, Videos, Audio, Archives, Executables, and Code Files.
- **Smart Duplicate Prevention**: Features an automated collision handler that appends a sequential counter to filenames if a file with the same name already exists in the destination directory, preventing accidental overwrites.
- **Self-Preservation Safeguard**: Includes a defensive check that prevents the script from moving itself during execution, maintaining runtime stability.
- **Comprehensive Logging**: Fully integrated with standard Python `logging` to track directory operations, structural changes, and exceptions in real time.

## 🛠️ Implementation Details

The core processing logic is encapsulated inside the `FileOrganizer` class using modern object-oriented principles:
- Uses `pathlib.Path` for cross-platform file system path resolution (compatible with Linux, Windows, and macOS).
- Uses `shutil.move` for secure and atomic file system operations.
- Runs non-recursively to organize only the immediate target directory without unexpected sub-folder traversal.

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system.

### Installation & Execution
1. Clone this repository or download the script file:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/python-file-organizer.git](https://github.com/YOUR_USERNAME/python-file-organizer.git)
   cd python-file-organizer
