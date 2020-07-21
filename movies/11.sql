SELECT movies.title
FROM movies
JOIN ratings ON movies.id = ratings.movie_id
WHERE movies.id IN (SELECT stars.movie_id FROM stars WHERE stars.person_id =(SELECT people.id FROM people WHERE people.name = "Chadwick Boseman"))
ORDER BY rating DESC LIMIT 5;