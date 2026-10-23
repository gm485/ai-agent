import os
import subprocess;

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:

    try:
        working_dir_abs = os.path.abspath(working_directory);
        target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))

        if os.path.commonpath([working_dir_abs, target_dir]) != working_dir_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_dir):
            return f'Error: "{file_path}" does not exist or is not a regular file';
        if not target_dir.endswith(".py"):
           return  f'Error: "{file_path}" is not a Python file';

        command = ["python", target_dir]
        if args:
            command.extend(args);

        process_obj = subprocess.run(command, cwd=working_dir_abs, capture_output=True, text=True, timeout=30)

        output = [];
        if process_obj.returncode != 0:
            output.append(f'Process exited with code {process_obj.returncode}')

        if process_obj.stdout == "" and process_obj.stderr == "":
            output.append("No output produced")

        if process_obj.stdout:
            output.append(f"STDOUT: {process_obj.stdout}");
        if process_obj.stderr:
            output.append(f"STDERR: {process_obj.stderr}");

        output_str = "\n".join(output)
        return output_str;


    except Exception as e:
        return f'Error executing python file: {e}'

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "run a file, but the file must end in .py. must be a python script file",
        "parameters": {
            "type": "object",
            "properties": {
                "run_python_file": {
                    "type": "string",
                    "properties": "takes args argument and file path of the file",
                    "required": "arguments is required for this run command",
                    "description": "run a python shell script file",
                },
            },
        },
    },
}
