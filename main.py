import os

from di.di import Di


def main():
    di = Di(
        os.getenv('token'),
        os.getenv('PORT'),
        os.getenv('url')
    )
    di.bot().start()


if __name__ == '__main__':
    main()
