-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT m.title, g.id FROM tv_shows m left outer JOIN tv_show_genres sg ON sg.show_id = m.id left OUTER JOIN tv_genres g ON sg.genre_id = g.id ORDER BY m.title, g.id;

