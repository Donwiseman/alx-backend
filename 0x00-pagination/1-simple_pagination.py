import csv
import math
from typing import List


def index_range(page, page_size):
    """Returns the start and end name number of a given page."""
    start_num = 0
    end_num = 0
    for pg in range(page):
        start_num = end_num
        end_num = start_num + page_size
    return (start_num, end_num)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
            """Returns the requested page as a list. """
            assert isinstance(page, int) and page >= 0
            assert isinstance(page_size, int) and page_size > 0
            pg = index_range(page, page_size)
            self.dataset()
            return self.__dataset[pg[0]: pg[1]]
    