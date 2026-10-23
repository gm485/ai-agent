import os

from config import MAX_CHARS


def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory);
        target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))

        if os.path.commonpath([working_dir_abs, target_dir]) != working_dir_abs:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory';

        if not os.path.isfile(target_dir):
            return f'Error: File not found or is not a regular file: "{file_path}"';
        #read contents of the file
        with open(target_dir) as file_contents:
            read_file_contents = file_contents.read(MAX_CHARS);
            if file_contents.read(1):
                read_file_contents += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return read_file_contents;



    except Exception as e:
        return f'Error: {e}';

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "list file contents inside a file if it goes past the max chars variable the output will truncate what was missing from the original output.",
        "parameters": {
            "type": "object",
            "properties": {
                "get_file_content": {
                    "type": "string",
                    "description": "string output of what is inside a file similar to the cat command on UNIX systems.",
                },


            },
        },
    },
}
