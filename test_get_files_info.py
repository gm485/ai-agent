import unittest;
from functions.get_files_info import get_files_info;



def main():

    result1 = get_files_info('calculator', ".")
    print(f'Result for current directory:\n ',result1)
    result2 = get_files_info("calculator", "/bin");
    print(f"Result for the '/bin' directory:\n ",result2)
    result3 = get_files_info("calculator", "pkg")
    print(f"Result for 'pkg' directory:\n ",result3)
    result4 = get_files_info("calculator", "../")
    print(f"Result for the '../' directory:\n ",result4)


if __name__ == "__main__":
    main();
