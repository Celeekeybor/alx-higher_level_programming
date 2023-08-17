-- lists all genres of the show Dexter.
   -- Each record should display:
      -- tv_genres.name
   -- Results must be sorted in ascending order by the genre name
   -- The database name will be passed as an argument of the mysql command

SELECT name FROM tv_genres
JOIN tv_show_genres ON id=tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.id=tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY name;
