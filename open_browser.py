import os
import platform


def platform_os_open_browser(url: str) -> None:
    """OS awear way to open a web browser"""
    os_system = platform.system()

    if "Windows" in os_system:
        os.startfile(url)  # type: ignore
    elif "Darwin" in os_system:
        os.system(f"open {url}")
    elif "Linux" in os_system:
        os.system(f"xdg-open {url}")


def webbrowser_module(url: str) -> None:
    """OS agnostic way to open a web browser"""
    import webbrowser

    webbrowser.open(url)


def main(url: str):
    platform_os_open_browser(url)
    webbrowser_module(url)


if __name__ == "__main__":
    website_url = "https://google.com"
    raise SystemExit(main(website_url))
