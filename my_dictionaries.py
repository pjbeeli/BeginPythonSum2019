"""
File Info here
"""


def my_code():
    """
    Test function
    :return: 
    """
    urls = {
        "google": "www.google.com",
        "yahoo": "www.yahoo.com",
        "twitter": "www.twitter.com",
        "wsu": "weber.edu"
    }

    print(urls, type(urls))
    # Access by key: [key]
    print(urls["wsu"])



if __name__ == '__main__':
    my_code()
    exit(0)