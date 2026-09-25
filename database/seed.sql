\copy MenuItem(menuItemID, itemName, price, category, availabilityStatus)
FROM 'menu_items.csv'
WITH (FORMAT csv, HEADER true);

\copy Ingredient(ingredientID, ingredientName, quantityAvailable, unitOfMeasure)
FROM 'ingredients.csv'
WITH (FORMAT csv, HEADER true);

\copy Orders(orderID, timestamp, orderStatus, totalPrice, processedByEmployee)
FROM 'orders.csv'
WITH (FORMAT csv, HEADER true);