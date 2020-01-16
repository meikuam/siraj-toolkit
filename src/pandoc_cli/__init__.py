from pypandoc import get_pandoc_path
try:
    print('check if pandoc is installed')
    pandoc_path = get_pandoc_path()
    print("pandoc_path: ", pandoc_path)
except OSError:
    print('pandoc is not installed, so try to download it.')
    from pypandoc.pandoc_download import download_pandoc

    # see the documentation how to customize the installation path
    # but be aware that you then need to include it in the `PATH`
    download_pandoc()

from src.pandoc_cli.pandoc_cli import Converter
