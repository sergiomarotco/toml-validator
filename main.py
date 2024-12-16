import argparse
import subprocess
from subprocess import CompletedProcess


def validate_toml(toml_path: str) -> int:
    """

    :type toml_path: str
    :rtype: int
    """
    try:  # Запуск toml-validator
        print(f'\033[34mTOML file validation:\033[0m')
        result: CompletedProcess[str] = subprocess.run(
            ["toml-validator", toml_path],
            text=True,  # для возврата строкового результата (Python 3.7+)
            capture_output=True,  # чтобы захватить вывод команды
            check=True  # для возбуждения исключения при ошибке
        )
        if result.returncode == 0:  # Вывод успешного результата
            #print("Validation succeeded!")
            print(f'\033[32m{result.stdout}\033[0m')
            return result.returncode
    except subprocess.CalledProcessError as e:  # Вывод ошибки
        print("\033[31mValidation failed!")
        print(f'\033[33m{e.stderr}\033[0m')
        stdout_array = e.stdout.split('\n')
        cleaned_list = [item for item in stdout_array if item not in ("", None)]
        for line in cleaned_list:
            print(f'\033[31m{line}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A script that validate TOML file in 'toml_path' parameter.",
                                     usage="main.py --toml_path ./in/some/folder/file.toml")
    parser.add_argument('--toml_path', required=True, help="Path to *.toml file u need to validate")
    args = parser.parse_args()
    return_code: int = validate_toml(args.toml_path)
    exit(return_code)
