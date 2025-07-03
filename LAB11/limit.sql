create or replace function get_users(limit_val INT, offset_val INT)
RETURNS TABLE(user_id INT, name VARCHAR, surname VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT phonebook.user_id, phonebook.name, phonebook.surname, phonebook.phone
    FROM phonebook
    ORDER BY user_id
    LIMIT limit_val OFFSET offset_val;
END;
$$ LANGUAGE plpgsql;