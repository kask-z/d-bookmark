command! -bar
      \ DbookmarkEdit
      \ execute 'edit' fnameescape(denite#bookmark_info)

function Hello#w()
	echo 'hellow'
endfunction
