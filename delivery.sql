1.
SELECT
  c.login,
  COUNT (o.track)
FROM
  «Couriers» AS c
  INNER JOIN «Orders» AS o ON o.courierId = c.id
WHERE
  inDelivery = true
GROUP BY
  c.login;

2.
SELECT
  track,
  cancelled,
  finished,
  inDelivery CASE WHEN finished == true THEN «status = 2» WHEN canсelled == true THEN «status = - 1» WHEN inDelivery == true THEN «status = 1» ELSE “status = 0” END
FROM
  «Orders»;




