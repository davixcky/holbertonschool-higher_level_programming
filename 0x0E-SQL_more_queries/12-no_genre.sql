-- Lists all shows contained in hbtn_0d_tvshows without a genre linked
SELECT m.title "title", sg.genre_id "genre_id"
FROM tv_shows m
LEFT JOIN tv_show_genres sg
	ON sg.show_id = m.id
	WHERE sg.show_id IS NULL
ORDER BY m.title;

