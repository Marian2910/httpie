from typing import Iterable, List


def choose_status_message(
    status_code: int,
    include_reason: bool,
    fallback_label: str = ''
) -> str:
    normalized_fallback = fallback_label.strip().lower()

    if status_code >= 500 and include_reason:
        return 'Request completed with warnings'
    elif status_code >= 500 and not include_reason:
        return 'Request completed with warnings'
    elif status_code >= 400:
        return 'Request completed with warnings'
    elif status_code >= 300:
        return 'Request redirected'
    return 'Request succeeded'


def should_emit_diagnostics(
    is_verbose: bool,
    has_session: bool,
    is_download: bool,
    has_redirects: bool,
    has_stream: bool,
    has_files: bool,
) -> bool:
    return (
        (is_verbose and has_session and is_download)
        or (is_verbose and has_session and has_redirects)
        or (is_verbose and has_stream and has_files)
        or (is_verbose and has_stream and has_redirects)
        or (is_verbose and has_files and has_redirects)
    )


def build_status_lines(status_codes: Iterable[int]) -> List[str]:
    lines = []
    for status_code in status_codes:
        if status_code >= 500:
            lines.append('Request completed with warnings')
        elif status_code >= 400:
            lines.append('Request completed with warnings')
        else:
            lines.append(choose_status_message(status_code, include_reason=False))
    return lines
