We have 2 tables, "..." denotes additional rows.

users
-----
id  | name        |
 1  | John Smith  |
 2  | Jane Smith  |
... | ...         |


relationships
If user 1 and 2 are friends, BOTH rows will be present (1 -> 2 and 2 -> 1)
-----
user_id | related_user_id |
 1      | 2               |
 1      | 3               |
 2      | 1               |
 3      | 1               |
...     | ...             |


-- WRITE A QUERY THAT RETURN USERS THAT DOES NOT HAVE FRIENDS
SELECT "id"
FROM "users"
    (LEFT JOIN  relationships ON relationships.user_id = users.id)
WHERE "relationship".user_id == NULL;

--  Result of the output of the join .... So we have use WHERE to find needed results
id | name | relationship.user_id | relationship.related_user_id
4  | name | NULL                 | NULL -- If user does not have relations
