CREATE OR REPLACE FUNCTION query(com VARCHAR, quer VARCHAR) 
RETURNS TABLE(user_id INT, name VARCHAR, surname VARCHAR, phone VARCHAR) AS $$
BEGIN
    IF com = '1' THEN
        RETURN QUERY
        SELECT * FROM phonebook WHERE phonebook.user_id = quer::int;
    ELSIF com = '2' THEN
        RETURN QUERY
        SELECT * FROM phonebook WHERE phonebook.name = quer;
    ELSIF com = '3' THEN
        RETURN QUERY
        SELECT * FROM phonebook WHERE phonebook.surname = quer;
    ELSIF com = '4' THEN
        RETURN QUERY
        SELECT * FROM phonebook WHERE phonebook.phone = quer;
    END IF;
END;
$$ LANGUAGE plpgsql;