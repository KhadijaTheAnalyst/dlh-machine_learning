-- Create a trigger to decrease item quantity after an order is placed

DELIMITER $$

CREATE TRIGGER decrease_quantity_after_order
BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE id = NEW.item_id;
END$$

DELIMITER ;
