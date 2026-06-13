from pathlib import Path
import shutil
import logging

# Configure logging to track operations and errors professionally
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class FileOrganizer:
    """
    A professional-grade utility to organize files in a directory 
    based on their extensions into structured categories.
    """
    
    # Industry standard categorization map
    CATEGORY_MAP = {
        "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".xls", ".pptx", ".csv"],
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".bmp", ".webp"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv"],
        "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Executables": [".exe", ".msi", ".deb", ".sh", ".bat"],
        "Code_Files": [".py", ".js", ".html", ".css", ".cpp", ".c", ".json", ".yaml"]
    }

    def __init__(self, target_directory: str = None):
        """
        Initializes the organizer with a target directory.
        If no path is provided, it defaults to the current working directory.
        """
        if target_directory:
            self.target_dir = Path(target_directory).resolve()
        else:
            self.target_dir = Path(__file__).resolve().parent
            
        self.script_name = Path(__file__).name

    def _get_category(self, file_extension: str) -> str:
        """
        Determines the destination folder name based on the file extension.
        """
        ext = file_extension.lower()
        for category, extensions in self.CATEGORY_MAP.items():
            if ext in extensions:
                return category
        return "Others"

    def _handle_duplicate(self, destination_dir: Path, file_path: Path) -> Path:
        """
        Prevents overwriting existing files by appending a counter to the filename.
        """
        counter = 1
        new_path = destination_dir / file_path.name
        while new_path.exists():
            new_path = destination_dir / f"{file_path.stem}_{counter}{file_path.suffix}"
            counter += 1
        return new_path

    def organize(self):
        """
        Executes the file organization process scanning the target directory.
        """
        logging.info(f"Starting organization in target directory: {self.target_dir}")
        
        if not self.target_dir.exists():
            logging.error("Target directory does not exist.")
            return

        moved_count = 0

        # Iterate only through files in the immediate directory (non-recursive)
        for item in self.target_dir.iterdir():
            if item.is_file():
                # Safety check: Prevent the script from moving itself
                if item.name == self.script_name:
                    continue
                
                category = self._get_category(item.suffix)
                destination_folder = self.target_dir / category
                
                try:
                    # Create the category directory if it does not exist
                    destination_folder.mkdir(exist_ok=True)
                    
                    # Resolve safe path in case of duplicate names
                    final_destination = self._handle_duplicate(destination_folder, item)
                    
                    # Safely move the file
                    shutil.move(str(item), str(final_destination))
                    logging.info(f"Successfully moved: {item.name} -> {category}/")
                    moved_count += 1
                    
                except Exception as e:
                    logging.error(f"Failed to move {item.name}. Reason: {str(e)}")

        logging.info(f"Organization completed. Total files organized: {moved_count}")


if __name__ == "__main__":
    # Standard entry point execution
    organizer = FileOrganizer()
    organizer.organize()