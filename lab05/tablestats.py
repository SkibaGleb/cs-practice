def read_rows(lines):
    """
    Parse CSV lines with header into list of dicts.
    Empty lines and lines with wrong field count are skipped.
    """
    rows = []
    header = None
    for line in lines:
        line = line.strip()
        if not line:
            continue
        fields = [field.strip() for field in line.split(",")]
        if header is None:
            header = fields
            continue
        if len(fields) != len(header):
            continue
        rows.append(dict(zip(header, fields)))
    return rows


def count_types(rows):
    """Count records of each type."""
    counts = {}
    for row in rows:
        kind = row.get("тип", "")
        counts[kind] = counts.get(kind, 0) + 1
    return counts


def total_minutes(rows, kind):
    """Sum minutes for records of given type, rounded to 1 decimal."""
    total = 0.0
    for row in rows:
        if row.get("тип", "") != kind:
            continue
        value = row.get("минуты", "").strip().replace(",", ".")
        try:
            total += float(value)
        except ValueError:
            continue
    return round(total, 1)


def to_csv(counts):
    """Format summary as CSV: header 'тип,количество', rows sorted by type."""
    lines = ["тип,количество"]
    for kind in sorted(counts):
        lines.append(f"{kind},{counts[kind]}")
    return "\n".join(lines) + "\n"