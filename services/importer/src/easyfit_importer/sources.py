from __future__ import annotations


def categorize_source(source_name: str | None, device: str | None = None) -> str:
    text = f"{source_name or ''} {device or ''}".lower()
    if "watch" in text:
        return "Apple Watch"
    if "iphone" in text or "phone" in text:
        return "iPhone"
    if "health" in text or "apple" in text:
        return "Apple Health"
    if source_name:
        return "Third-party app"
    return "Unknown"


def categorize_device(device: str | None) -> str:
    if not device:
        return "Unknown"
    text = device.lower()
    if "watch" in text:
        return "Apple Watch"
    if "iphone" in text:
        return "iPhone"
    if "ipad" in text:
        return "iPad"
    return "Other"
