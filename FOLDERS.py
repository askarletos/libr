import os

class ResizedFoldersPrinter:
    def __init__(self, base_folder_path):
        self.base_folder_path = base_folder_path

    def print_resized_folders(self):
        try:
            with os.scandir(self.base_folder_path) as entries:
                for entry in entries:
                    if entry.is_dir():
                        subfolder_path = os.path.join(self.base_folder_path, entry.name)
                        if os.path.exists(os.path.join(subfolder_path, "resized")):
                            print(f'\nResized folders for folder {entry.name}:')
                            resized_folder_path = os.path.join(subfolder_path, "resized")
                            try:
                                with os.scandir(resized_folder_path) as resized_entries:
                                    for resized_entry in resized_entries:
                                        if resized_entry.is_dir():
                                            print(f'  Directory: {resized_entry.name}')
                            except FileNotFoundError as e:
                                print(f'The folder {resized_folder_path} does not exist: {e}')
                            except PermissionError as e:
                                print(f'Permission denied to access the folder {resized_folder_path}: {e}')
                            except OSError as e:
                                print(f'Error: {e}')
        except FileNotFoundError as e:
            print(f'The folder {self.base_folder_path} does not exist: {e}')
        except PermissionError as e:
            print(f'Permission denied to access the folder {self.base_folder_path}: {e}')
        except OSError as e:
            print(f'Error: {e}')

    def print_subfolders_contents(self):
        try:
            print(f'Contents of subfolders:')
            for root, dirs, files in os.walk(self.base_folder_path):
                for d in dirs:
                    subfolder_path = os.path.join(root, d)
                    subfolder_contents = os.listdir(subfolder_path)
                    print(f'{subfolder_path}: {subfolder_contents}')
        except FileNotFoundError as e:
            print(f'The folder {self.base_folder_path} does not exist: {e}')
        except PermissionError as e:
            print(f'Permission denied to access the folder {self.base_folder_path}: {e}')
        except OSError as e:
            print(f'Error: {e}')

# Χρήση της κλάσης ResizedFoldersPrinter
base_folder_path = 'C:\\tmp'
resized_printer = ResizedFoldersPrinter(base_folder_path)
resized_printer.print_resized_folders()
resized_printer.print_subfolders_contents()
