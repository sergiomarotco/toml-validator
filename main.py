import subprocess
from subprocess import CompletedProcess


def validate_toml(toml_path: str) -> int:
    try: # Запуск toml-validator
        print(f'\033[34mTOML file validation:\033[0m')
        result: CompletedProcess[str] = subprocess.run(
            ["toml-validator", toml_path],
            text=True,  # для возврата строкового результата (Python 3.7+)
            capture_output=True,  # чтобы захватить вывод команды
            check=True  # для возбуждения исключения при ошибке
        )
        if result.returncode == 0: # Вывод успешного результата
            #print("Validation succeeded!")
            print(f'\033[32m{result.stdout}\033[0m')
            return result.returncode
    except subprocess.CalledProcessError as e: # Вывод ошибки
        print("\033[31mValidation failed!")
        print(f'\033[33m{e.stderr}\033[0m')
        stdout_array = e.stdout.split('\n')
        cleaned_list = [item for item in stdout_array if item not in ("", None)]
        for line in cleaned_list:
            print(f'\033[31m{line}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file_path: str = "./bad.toml"
    return_code: int = validate_toml(file_path)
    exit(return_code)
