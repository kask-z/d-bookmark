command! -bar
      \ DbookmarkEdit
      \ execute 'edit' fnameescape(denite#bookmark_info)

function bookmark#hello()
	echo 'hellow'
endfunction

function bookmark#echotest()
	python _echotest()
endfunction
