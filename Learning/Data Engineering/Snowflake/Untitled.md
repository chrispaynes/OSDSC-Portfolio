``` sql

SELECT
    JSON:full_name,
    s1.value
FROM
    unknown,
    TABLE(FLATTEN(JSON:experience)) s1
LIMIT 10;

```
