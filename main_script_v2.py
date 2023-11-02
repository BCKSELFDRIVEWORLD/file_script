import os
import shutil

class FileOperations:
    def __init__(self):
        self.folder_paths = [
            "maps_old/pgms",
            "maps_old/pbstreams",
            "maps_old/compressed",
            "maps_old/pngs",
            "maps_old"
        ]
        self.directory = os.getcwd()
        self.folder_paths = [os.path.join(self.directory, folder) for folder in self.folder_paths]
        self.target_folder = os.getcwd()
        self.files = {}
        self.extensions = ["_23z.yaml","_23.yaml", ".yaml", "_150px.png", ".pbstream", ".pgm", ".png", ".txt"]
        self.cut_files = set()

    def list_files(self, directory_path):
        if os.path.exists(directory_path) and os.path.isdir(directory_path):
            files = [os.path.splitext(file)[0] for file in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, file))]
            return files
        else:
            return []

    def scan_files_in_folders(self):
        for folder_path in self.folder_paths:
            self.files[folder_path] = set(self.list_files(folder_path))

    def find_same_files(self):
        for file_list in self.files.values():
            for file in file_list:
                file_parts = file.split('_')  #
                if len(file_parts) >= 2:
                    filename_key = '_'.join(file_parts[:2])  
                    self.cut_files.add(filename_key)

    def copy_files(self):
        copied_files = set()
        self.target_folder = os.path.dirname(os.path.abspath(__file__)) 
        for file_name in self.cut_files:
            for folder_path in self.folder_paths:
                for extension in self.extensions:
                    file = file_name + extension
                    for root, dirs, files in os.walk(folder_path):
                        for name in files:
                            if file == name:
                                file_source_path = os.path.join(root, name)
                                file_target_folder = os.path.join(self.target_folder, file_name)
                                file_target_path = os.path.join(file_target_folder, name)
                                if not os.path.exists(file_target_folder):
                                    os.makedirs(file_target_folder, exist_ok=True)

                                try:
                                    if name not in copied_files:
                                        shutil.copy(file_source_path, file_target_path)
                                        print(f"'{name}' file has been copied.")
                                        copied_files.add(name)
                                except IOError as e:
                                    print(f"Error! There was a problem copying '{name}': {e}")
file_operations = FileOperations()
file_operations.scan_files_in_folders()
file_operations.find_same_files()
file_operations.copy_files()
