import os
import platform

website_url = "https://google.com"

os_system = platform.system()

if "Windows" in os_system:
    os.startfile(website_url)  # type: ignore
elif "Darwin" in os_system:
    os.system(f"open {website_url}")
elif "Linux" in os_system:
    os.system(f"xdg-open {website_url}")
