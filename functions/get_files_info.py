def get_files_info(working_directory, directory="."):
    """
    Get information about files in the specified directory.

    Args:
        working_directory (str): The base directory to start from.
        directory (str): The subdirectory to inspect. Defaults to the current directory.

    Returns:
        list: A list of dictionaries containing file names and their sizes.
    """
    import os
    
    print(f"Result for '{directory}' directory:")

    full_path = os.path.join(working_directory, directory)
    if directory == ".":
        pass
    elif directory not in os.listdir(working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    elif not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'

    files_info = ""

    for filename in os.listdir(full_path):
        file_path = os.path.join(full_path, filename)
        size = os.path.getsize(file_path)
        is_dir = os.path.isdir(file_path)
        files_info = files_info + "- " + filename + ": file size=" + str(size) + " bytes, is_dir=" + str(is_dir) + "\n"
    return files_info

from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)