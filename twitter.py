import re


# NOTE: Extracts username present in the url
url = input("URL: ").strip()
#
# username = re.sub(r"^.*(https?://)?(www\.)?twitter\.com/", "", url)
#
# print(f"Username: {username}")

if matches := re.search(
    r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE
):
    print("Username:", matches.group(1))
