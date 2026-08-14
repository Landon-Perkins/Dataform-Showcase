from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INCLUDES_DIR = ROOT / "includes"

FILES = {
    "date_helpers.js": """function generateDateSpine(startDate, endDate) {
  return `
    SELECT CAST(d AS DATE) AS date_day
    FROM UNNEST(GENERATE_DATE_ARRAY('${startDate}', '${endDate}', INTERVAL 1 DAY)) AS d
  `;
}

function getMonthStart(dateString) {
  return `DATE_TRUNC(${dateString}, MONTH)`;
}

module.exports = {
  generateDateSpine,
  getMonthStart,
};
""",
    "business_rules.js": """function normalizeCategory(value) {
  return `LOWER(TRIM(CAST(${value} AS STRING)))`;
}

function isActive(flag) {
  return `COALESCE(${flag}, FALSE)`;
}

function flagMissingValue(columnName) {
  return `CASE WHEN ${columnName} IS NULL THEN 1 ELSE 0 END AS missing_${columnName}`;
}

module.exports = {
  normalizeCategory,
  isActive,
  flagMissingValue,
};
""",
    "metric_helpers.js": """function safeDivide(numerator, denominator) {
  return `SAFE_DIVIDE(${numerator}, ${denominator})`;
}

function pctChange(currentValue, priorValue) {
  return `SAFE_DIVIDE((${currentValue} - ${priorValue}), ${priorValue})`;
}

function rollingWindow(metric, days) {
  return `AVG(${metric}) OVER (ORDER BY date_day ROWS BETWEEN ${days} PRECEDING AND CURRENT ROW)`;
}

module.exports = {
  safeDivide,
  pctChange,
  rollingWindow,
};
""",
}


def main() -> None:
    INCLUDES_DIR.mkdir(parents=True, exist_ok=True)
    for file_name, content in FILES.items():
        path = INCLUDES_DIR / file_name
        path.write_text(content, encoding="utf-8")
        print(f"Generated {path.relative_to(ROOT)}")

    print(f"\nDone. {len(FILES)} helper files created in {INCLUDES_DIR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
