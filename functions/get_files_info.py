import os

def get_dir_size(path='.'):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total


def get_files_info(working_directory, directory="."):
    path_directory = os.path.abspath(os.path.join(os.path.abspath(working_directory), directory))
    if (not os.path.exists(path_directory)) or \
        (not os.getcwd() in os.path.abspath(path_directory)) or \
        (path_directory == os.path.abspath(os.path.join(working_directory, '../'))):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    elif not os.path.isdir(path_directory):
        return f'Error: "{directory}" is not a directory'
    else:
        result = []
        for file in os.listdir(path_directory):
            try:
                is_dir = os.path.isdir(os.path.join(path_directory,file))
                if is_dir: file_size = get_dir_size(os.path.join(path_directory, file))
                else: file_size = os.path.getsize(os.path.join(path_directory,file))
                result.append(f"- {file}: file_size:{file_size} bytes, is_dir={is_dir}")
            except Exception as e:
                return f"Error: {e}"
        return '\n'.join(result)

if __name__ == "__main__":
    result = get_files_info(r"\\wsl.localhost\Ubuntu\home\danie\Bootdev\aiagent", '.')
    print(result)