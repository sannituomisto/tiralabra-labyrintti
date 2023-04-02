"""Sovelluksen toiminnasta ja sen aloituksesta vastaava moduuli."""
from sovellus import Sovellus


def main():
    """Aloittaa sovelluksen käyttöliittymän kanssa sovelluksen toiminnan.
    """
    sovellus = Sovellus()
    sovellus.suorita()


if __name__ == '__main__':
    main()
