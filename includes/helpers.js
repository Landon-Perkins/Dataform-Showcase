function generateDateSpine(startDate, endDate) {
  return `
    SELECT CAST(d AS DATE) AS date_day
    FROM UNNEST(GENERATE_DATE_ARRAY('${startDate}', '${endDate}', INTERVAL 1 DAY)) AS d
  `;
}

module.exports = { generateDateSpine };

// Lightweight helper example used to illustrate reusable Dataform support logic.
