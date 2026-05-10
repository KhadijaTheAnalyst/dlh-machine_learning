-- Create a trigger to decrease item quantity after an order is placed
-- Trigger fires AFTER order is inserted
-- Updates the items table to decrease quantity

DROP TRIGGER IF EXISTS decrease_quantity_after_order;

DELIMITER $$

CREATE TRIGGER decrease_quantity_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    -- Decrease the item quantity by the order amount
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE id = NEW.item_id;
END$$

DELIMITER ;