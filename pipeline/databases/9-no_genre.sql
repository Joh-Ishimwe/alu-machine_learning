-- join
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
<<<<<<< HEAD
ORDER BY title ASC, tv_show_genres.genre_id ASC
=======
ORDER BY title ASC, tv_show_genres.genre_id ASC
>>>>>>> d01a612edafbcb20b156d4f8e219d7deae1f7d56
