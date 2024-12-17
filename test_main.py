from unittest import TestCase

from main import validate_toml


class Test(TestCase):
    print(f'\033[34mRun Test case # 1:\033[0m')

    def test_validate_toml_fail(self):
        if validate_toml('./bad.toml') != 0:
            print('Test case 1 - success')
        else:
            exit(1)

    def test_validate_toml_success(self):
        print(f'\033[34mRun Test case # 2:\033[0m')
        if validate_toml('./good.toml') == 0:
            print('Test case 2 - success')
        else:
            self.fail()
