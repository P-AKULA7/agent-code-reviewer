def build_requirement_input(pr: dict) -> dict:
    issue_texts = []

    for issue in pr.get("linked_issues") or []:
        number = issue.get("number")
        title = (issue.get("title") or "").strip()
        body = (issue.get("body") or "").strip()

        if not title and not body:
            continue

        heading = f"Issue #{number}" if number is not None else "Linked issue"
        issue_texts.append(f"{heading}: {title}\n{body}".strip())

    return {
        "title": pr.get("title") or "",
        "body": pr.get("pr_description") or "",
        "linked_issue": "\n\n".join(issue_texts),
    }
