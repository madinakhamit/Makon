CREATE OR REPLACE PROCEDURE del(type_of_com varchar,us_name_phone varchar)
LANGUAGE plpgsql
AS $$
DECLARE 
    existing_id INT;
BEGIN

    -- Если нажали 1
    IF type_of_com = '1' THEN
        delete from phonebook 
        WHERE phonebook.name = del.us_name_phone; 
    -- or — 2 удаляем
    ELSE
        delete from phonebook 
        WHERE phonebook.phone = del.us_name_phone; 
    END IF;
END;
$$;