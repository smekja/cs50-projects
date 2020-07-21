SELECT people.name
FROM people
WHERE people.id IN (SELECT directors.person_id FROM directors JOIN movies ON directors.movie_id = movies.id WHERE movies.id IN(SELECT ratings.movie_id FROM ratings JOIN movies ON ratings.movie_id = movies.id WHERE ratings.rating >= 9));