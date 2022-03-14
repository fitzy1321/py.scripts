"""Helper Functions."""

from xml.dom import minidom

from src.config import ConfigManager


def exit_now():
    """Exit program now."""
    print("Closing Program")
    exit()


def get_debug_url(service_path: str):
    """Get url for api in local debug mode."""
    doc = minidom.parse(service_path)
    return doc.getElementsByTagName("IISUrl")[0].firstChild.nodeValue
