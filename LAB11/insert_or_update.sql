CREATE OR REPLACE PROCEDURE insert_or_update_user(name varchar, surname varchar, phone varchar)
LANGUAGE plpgsql
AS $$
DECLARE 
    existing_id INT;
BEGIN
    -- Поиск пользователя с таким именем и фамилией и добавляем его в эту переменную 
    SELECT user_id INTO existing_id 
    FROM phonebook 
    WHERE phonebook.name = insert_or_update_user.name AND phonebook.surname = insert_or_update_user.surname;

    -- Если нашли пользователя  that обновляем
    IF FOUND THEN--found работает только так
        UPDATE phonebook 
        SET phone = insert_or_update_user.phone 
        WHERE user_id = existing_id;
    -- or — вставляем
    ELSE
        INSERT INTO phonebook(name, surname, phone)
        VALUES (insert_or_update_user.name, insert_or_update_user.surname, insert_or_update_user.phone);
    END IF;
END;
$$;