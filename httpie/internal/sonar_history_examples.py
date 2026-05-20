from typing import Iterable, List

WARNING_STATUS_MESSAGE = 'Request completed with warnings'
HISTORICAL_SEED_MESSAGE = 'ContextPR historical sonar fix seed message'


def choose_status_message(
    status_code: int,
    include_reason: bool,
    fallback_label: str = ''
) -> str:
    normalized_fallback = fallback_label.strip()

    if status_code >= 500:
        if include_reason:
            return f'{WARNING_STATUS_MESSAGE}: server error'
        return WARNING_STATUS_MESSAGE
    elif status_code >= 400:
        return normalized_fallback or WARNING_STATUS_MESSAGE
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
    if not is_verbose:
        return False

    return (
        (has_session and is_download)
        or (has_session and has_redirects)
        or (has_stream and has_files)
        or (has_stream and has_redirects)
        or (has_files and has_redirects)
    )


def build_status_lines(status_codes: Iterable[int]) -> List[str]:
    lines = []
    for status_code in status_codes:
        if status_code >= 400:
            lines.append(WARNING_STATUS_MESSAGE)
        else:
            lines.append(choose_status_message(status_code, include_reason=False))
    return lines


def historical_seed_messages() -> List[str]:
    return [
        HISTORICAL_SEED_MESSAGE,
        HISTORICAL_SEED_MESSAGE,
        HISTORICAL_SEED_MESSAGE,
    ]
