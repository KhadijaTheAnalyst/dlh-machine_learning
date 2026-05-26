-- This SQL script creates a trigger that decreases the quantity of items in the inventory after an order
-- is placed. The trigger is set to execute before a new record is inserted into the 'orders' table.
-- It updates the 'items' table by subtracting the number of items ordered from the current quantity
-- available for the specific item.  

DELIMITER $$

CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE id = NEW.item_id;
END$$

DELIMITER ;