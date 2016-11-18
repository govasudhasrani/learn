import time
import os.path
from os import listdir
import sys
from datetime import datetime
import shutil


class DirectoryValidator:
    validated_directories = set()

    @classmethod
    def validate(cls, directory):

        if directory is None:
            raise ValueError("Directory value was not specified.")

        if len(cls.validated_directories) and directory in cls.validated_directories:
            return True

        if not os.path.exists(directory):
            raise ValueError("The given directory {0} does not exist.".format(directory))

        if not os.path.isdir(directory):
            raise ValueError("Given input {0} is not a directory.".format(directory))

        cls.validated_directories.add(directory)


def filter_and_sort_files(directory, filter_date):
    """
    Sort files based on last modified time of files
    :param directory:
    :return:
    """
    DirectoryValidator.validate(directory)

    files = filter(lambda file: os.path.isfile(file) and
                                datetime.fromtimestamp(os.path.getmtime(file)).date() == filter_date,
                    [os.path.join(directory, item) for item in os.listdir(directory)])
    # Good reference on lambda: http://www.secnetix.de/olli/Python/lambda_functions.hawk
    files.sort(key=lambda file: os.path.getmtime(file))

    return files


def add_file_prefix_and_move_to_dir(files, destn_dir):
    """

    :param files:
    :return:
    """
    DirectoryValidator.validate(destn_dir)
    for file in files:
        date_prefix = time.strftime("%d_%H_%M_%S", time.localtime(os.path.getmtime(file)))
        new_path = os.path.join(destn_dir, date_prefix + "." + os.path.basename(file))

        print "New path: ", new_path

        shutil.copyfile(file, new_path)


if __name__ == "__main__":

    """
    Usage example:

        Please specify source files directory(cwd:/Users/MyHome/PycharmProjects/GitHubProjects/Utilities): /Users/<src folder>
        Please specify destination directory(cwd:/Users/MyHome/PycharmProjects/GitHubProjects/Utilities): /Users/<dest_folder>
        Press enter to choose today as filter criteria or provide other date (%Y-%m-%d): 2016-11-11
    """

    # Default values
    src_dir, dest_dir = "", ""

    # Validate input values
    if len(sys.argv) == 1:
        src_dir = raw_input("Please specify source files directory(cwd:{0}): ".format(os.getcwd()))
        dest_dir = raw_input("Please specify destination directory(cwd:{0}): ".format(os.getcwd()))
        filter_criteria = raw_input("Press enter to choose today as filter criteria or provide other date (%Y-%m-%d): ")
    else:
        src_dir = sys.argv[1]
        dest_dir = sys.argv[2]

    try:
        for dir in (src_dir, dest_dir):
            DirectoryValidator.validate(dir)
    except ValueError as err:
        print err.message
        exit(1)

    if filter_criteria:
        filter_criteria = datetime.strptime(filter_criteria, "%Y-%m-%d").date()
    else:
        filter_criteria = datetime.now().date()

    # Filtered files
    filtered_files = filter_and_sort_files(src_dir, filter_criteria)

    # Add date prefix to files
    add_file_prefix_and_move_to_dir(filtered_files, dest_dir)
