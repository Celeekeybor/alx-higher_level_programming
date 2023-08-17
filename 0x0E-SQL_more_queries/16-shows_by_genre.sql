-- lists all shows and linked genres from the database hbtn_0d_tvshows
   -- If a show doesn’t have a genre, display NULL in the genre column
   -- Each record should display:
      -- tv_shows.title - tv_genres.name
   -- Results must be sorted in ascending order by the show title and genre
   -- The database name will be passed as an argument of the mysql command

SELECT title, tv_genres.name FROM tv_shows
LEFT JOIN tv_show_genres ON id=tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title, tv_genres.name;
