# region
from pprint import pprint
from re import findall
from sqlite3 import connect
from sqlite3.dbapi2 import Connection, Cursor

# endregion
from typing import List

podcast_db: Connection = connect("database.db")
podcast_cur: Cursor = podcast_db.cursor()

podcast_cur.execute(
    """SELECT url
FROM reference;"""
)

url: str
url_list: list[str] = [url for url, *left in podcast_cur.fetchall()]

hostname: str
hostname_list: list[str] = [
    hostname for url in url_list for hostname in findall(r"//([^\s/]*)/", url)
]


def extractor(host: str) -> str:
    part_list: list[str] = host.split(".")[::-1]

    excluded_list: list[str] = [
        "ac",
        "au",
        "ca",
        "co",
        "com",
        "eu",
        "europa",
        "fm",
        "fr",
        "gov",
        "hk",
        "io",
        "jp",
        "kr",
        "me",
        "net",
        "or",
        "org",
        "uk",
    ]

    index: int
    for index in range(2):
        if part_list[index] not in excluded_list:
            return part_list[index]

    return part_list[2]


hostname_group_dict: dict[str, list[str]] = {}

for hostname in {*hostname_list}:
    group: str = extractor(hostname)
    hostname_group_dict[group] = hostname_group_dict.get(group, []) + [hostname]

hostnames: list[str]
for group, hostnames in hostname_group_dict.items():
    podcast_cur.execute(
        """INSERT INTO group_tabulated("group", hostname_count, total_link_count)
VALUES (?, ?, ?);""",
        [
            group,
            len(hostnames),
            sum(hostname_list.count(hostname) for hostname in hostnames),
        ],
    )

podcast_db.commit()
