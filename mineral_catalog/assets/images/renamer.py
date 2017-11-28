import os

from django.utils.encoding import uri_to_iri


def rename_images():
    for file in os.listdir('.'):
        os.rename(file, uri_to_iri(file))


if __name__ == '__main__':
    rename_images()
