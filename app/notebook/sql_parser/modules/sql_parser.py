import sqlparse

import tkinter as tk


def highlight_reserved_keywords(reserved_keywords: set, text_widget) -> None:
    for keyword in reserved_keywords:
        offset = '+%dc' % len(keyword)
        start_position = text_widget.search(f'\\m{keyword}\\M', '1.0', tk.END, nocase=1, regexp=True)
        while start_position:
            end_position = start_position + offset
            text_widget.tag_add("start", start_position, end_position)
            start_position = text_widget.search(f'\\m{keyword}\\M', end_position, tk.END, nocase=1, regexp=True)
        text_widget.tag_config("start", foreground="blue", font=('Elvetica', 12, 'bold'))


def parse_sql_string(sql_string: str, identifier_case: str, wrap_limit: int) -> str:
    sql_string.replace('\n', ' ')
    formatted_sql_string = sqlparse.format(
        sql_string,
        reindent=True,
        keyword_case='upper',
        identifier_case=identifier_case,
        use_space_around_operators=True,
        output_format='rpgle',
        wrap_after=wrap_limit
    )
    return formatted_sql_string
