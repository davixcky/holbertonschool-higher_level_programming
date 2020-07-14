-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
select m.title "title", g.id "genre_id" from tv_shows m, tv_genres g, tv_show_genres sg where sg.genre_id = g.id and sg.show_id = m.id order by m.title, g.id;
