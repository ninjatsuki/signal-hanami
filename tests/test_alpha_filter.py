import json
from unittest.mock import Mock, patch

import pytest

from alpha_filter import _format_catalog, filter_alpha


def test_format_catalog_uses_summary_text() -> None:
    items = [
        {
            "title": "OpenAI API pricing change",
            "url": "https://example.com",
            "source": "GitHub",
            "description": "Pricing update for model access.",
        }
    ]

    text = _format_catalog(items)

    assert "OpenAI API pricing change" in text
    assert "https://example.com" in text


def test_filter_alpha_returns_empty_for_empty_input() -> None:
    assert filter_alpha([]) == []


def test_filter_alpha_requires_groq_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("GROQ_API_KEY", raising=False)

    with pytest.raises(RuntimeError, match="GROQ_API_KEY"):
        filter_alpha([{"title": "Example", "description": "Example item", "source": "GitHub"}])


def test_filter_alpha_parses_response() -> None:
    payload = {"alpha_items": [{"title": "Example item", "url": "https://example.com", "source": "GitHub"}]}
    response = Mock()
    response.raise_for_status.return_value = None
    response.json.return_value = {"choices": [{"message": {"content": json.dumps(payload)}}]}

    with patch("alpha_filter.httpx.post", return_value=response), patch.dict("os.environ", {"GROQ_API_KEY": "test-key"}):
        result = filter_alpha([{"title": "Example item", "description": "Example item", "source": "GitHub"}])

    assert result == payload["alpha_items"]
