
SELECT
  c.login,
  o.inDelivery
FROM
  «Couriers» As c
  RIGHT JOIN «Orders» AS o ON o.courierId = c.id
WHERE
  inDelivery = true 2.

SELECT
  track,
  inDelivery WHEN finished == true THEN « WHEN canсelled == true THEN « WHEN inDelivery == true THEN «» ELSE 0 END
FROM
  «Orders»
