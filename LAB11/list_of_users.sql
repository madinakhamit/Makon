CREATE OR REPLACE PROCEDURE insert_many_users(
    names TEXT[], 
    surnames TEXT[], 
    phones TEXT[]
) 
LANGUAGE plpgsql
AS $$
DECLARE
    i INT := 1;
    entry TEXT;
BEGIN
    -- Создание временной таблицы для хранения ошибок
    CREATE TEMP TABLE IF NOT EXISTS error_log (
        error_message TEXT
    );

    -- цикл по массивам
    WHILE i <= array_length(names, 1) LOOP
        IF phones[i] ~ '^\d{11}$' THEN
            BEGIN
                -- вставить пользователя в таблицу
                INSERT INTO phonebook(name, surname, phone)
                VALUES (names[i], surnames[i], phones[i]);
            EXCEPTION WHEN unique_violation THEN
                -- если копия
                entry := 'DUPLICATE: ' || names[i] || ' ' || surnames[i] || ' - ' || phones[i];
                -- Сохраняем ошибку в временной таблице
                INSERT INTO error_log(error_message) VALUES (entry);
            END;
        ELSE
            -- Если телефон ошибочный
            entry := 'INVALID: ' || names[i] || ' ' || surnames[i] || ' - ' || phones[i];
            -- Сохраняем ошибку в временной таблице
            INSERT INTO error_log(error_message) VALUES (entry);
        END IF;
        i := i + 1;
    END LOOP;

    -- Выводим все ошибки
    RAISE NOTICE 'Errors:';--вывод в консоль
    FOR entry IN 
        SELECT error_message FROM error_log -- как обычный форик 
    LOOP
        RAISE NOTICE '%', entry;-- вывод в лог именно  с %
    END LOOP;
END;
$$;