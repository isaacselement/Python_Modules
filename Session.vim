let SessionLoad = 1
if &cp | set nocp | endif
let s:cpo_save=&cpo
set cpo&vim
nmap gx <Plug>NetrwBrowseX
nnoremap <silent> <Plug>NetrwBrowseX :call netrw#NetrwBrowseX(expand("<cWORD>"),0)
let &cpo=s:cpo_save
unlet s:cpo_save
set backspace=2
set fileencodings=ucs-bom,utf-8,default,latin1
set modelines=0
set ruler
set runtimepath=~/.vim,~/.vim/bundle/Vundle.vim,~/.vim/bundle/python-mode,/usr/share/vim/vimfiles,/usr/share/vim/vim73,/usr/share/vim/vimfiles/after,~/.vim/after,~/.vim/bundle/Vundle.vim,~/.vim/bundle/Vundle.vim/after,~/.vim/bundle/python-mode/after
set shiftround
set wildignore=*.pyc
set window=0
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
cd ~/Workspaces/python/Python_Modules
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +137 helper/I18NHelper.py
badd +28 network/FormPoster.py
badd +24 ~/.vimrc
silent! argdel *
edit helper/I18NHelper.py
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
set nosplitbelow
set nosplitright
wincmd t
set winheight=1 winwidth=1
exe 'vert 1resize ' . ((&columns * 30 + 90) / 180)
exe 'vert 2resize ' . ((&columns * 149 + 90) / 180)
argglobal
enew
file ~/Workspaces/python/Python_Modules/helper/
let s:cpo_save=&cpo
set cpo&vim
nmap <buffer>  <Plug>NetrwHideEdit
nmap <buffer>  <Plug>NetrwRefresh
nnoremap <buffer> <silent> C :let g:netrw_chgwin= winnr()
nnoremap <buffer> <silent> c :exe "keepjumps lcd ".fnameescape(b:netrw_curdir)
nnoremap <buffer> <F1> :he netrw-quickhelp
imap <buffer>  <Plug>NetrwHideEdit
imap <buffer>  <Plug>NetrwRefresh
inoremap <buffer> <silent> C :let g:netrw_chgwin= winnr()
inoremap <buffer> <silent> c :exe "keepjumps lcd ".fnameescape(b:netrw_curdir)
let &cpo=s:cpo_save
unlet s:cpo_save
setlocal noautoindent
setlocal nobinary
setlocal bufhidden=delete
setlocal nobuflisted
setlocal buftype=nofile
setlocal nocindent
setlocal cinkeys=0{,0},0),:,0#,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=
setlocal comments=s1:/*,mb:*,ex:*/,://,b:#,:%,:XCOMM,n:>,fb:-
setlocal commentstring=/*%s*/
setlocal complete=.,w,b,u,t,i
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
setlocal cursorline
setlocal define=
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal noexpandtab
if &filetype != 'netrw'
setlocal filetype=netrw
endif
setlocal foldcolumn=0
setlocal foldenable
setlocal foldexpr=0
setlocal foldignore=#
setlocal foldlevel=0
setlocal foldmarker={{{,}}}
setlocal foldmethod=manual
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldtext=foldtext()
setlocal formatexpr=
setlocal formatoptions=tcq
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal grepprg=
setlocal iminsert=0
setlocal imsearch=0
setlocal include=
setlocal includeexpr=
setlocal indentexpr=
setlocal indentkeys=0{,0},:,0#,!^F,o,O,e
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255,.,~,-,*,/
setlocal keywordprg=
setlocal nolinebreak
setlocal nolisp
setlocal nolist
setlocal makeprg=
setlocal matchpairs=(:),{:},[:]
setlocal modeline
setlocal nomodifiable
setlocal nrformats=octal,hex
set number
setlocal nonumber
setlocal numberwidth=4
setlocal omnifunc=
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal quoteescape=\\
setlocal readonly
setlocal norelativenumber
setlocal noscrollbind
setlocal shiftwidth=8
setlocal noshortname
setlocal nosmartindent
setlocal softtabstop=0
setlocal nospell
setlocal spellcapcheck=
setlocal spellfile=
setlocal spelllang=en
setlocal statusline=
setlocal suffixesadd=
setlocal swapfile
setlocal synmaxcol=3000
if &syntax != 'netrw'
setlocal syntax=netrw
endif
setlocal tabstop=32
setlocal tags=
setlocal textwidth=0
setlocal thesaurus=
setlocal noundofile
setlocal nowinfixheight
setlocal nowinfixwidth
setlocal nowrap
setlocal wrapmargin=0
lcd ~/Workspaces/python/Python_Modules
wincmd w
argglobal
let s:cpo_save=&cpo
set cpo&vim
inoremap <buffer> <silent> <Nul> =pymode#rope#complete(0)
inoremap <buffer> <silent> <C-Space> =pymode#rope#complete(0)
noremap <buffer> <silent> ra :PymodeRopeAutoImport
noremap <buffer> <silent> r1p :call pymode#rope#module_to_package()
noremap <buffer> <silent> rnc :call pymode#rope#generate_class()
noremap <buffer> <silent> rnp :call pymode#rope#generate_package()
noremap <buffer> <silent> rnf :call pymode#rope#generate_function()
noremap <buffer> <silent> ru :call pymode#rope#use_function()
noremap <buffer> <silent> rs :call pymode#rope#signature()
noremap <buffer> <silent> rv :call pymode#rope#move()
noremap <buffer> <silent> ri :call pymode#rope#inline()
vnoremap <buffer> <silent> rl :call pymode#rope#extract_variable()
vnoremap <buffer> <silent> rm :call pymode#rope#extract_method()
noremap <buffer> <silent> r1r :call pymode#rope#rename_module()
noremap <buffer> <silent> rr :call pymode#rope#rename()
noremap <buffer> <silent> ro :call pymode#rope#organize_imports()
noremap <buffer> <silent> f :call pymode#rope#find_it()
noremap <buffer> <silent> d :call pymode#rope#show_doc()
noremap <buffer> <silent> g :call pymode#rope#goto_definition()
onoremap <buffer> C :call pymode#motion#select('^\s*class\s', 0)
vnoremap <buffer> <silent> K :call pymode#doc#show(@*)
nnoremap <buffer> <silent> K :call pymode#doc#find()
onoremap <buffer> M :call pymode#motion#select('^\s*def\s', 0)
vnoremap <buffer> [M :call pymode#motion#vmove('^\s*def\s', 'b')
vnoremap <buffer> [[ :call pymode#motion#vmove('\v^(class|def)\s', 'b')
onoremap <buffer> [M :call pymode#motion#move('^\s*def\s', 'b')
onoremap <buffer> [C :call pymode#motion#move('\v^(class|def)\s', 'b')
onoremap <buffer> [[ :call pymode#motion#move('\v^(class|def)\s', 'b')
nnoremap <buffer> [M :call pymode#motion#move('^\s*def\s', 'b')
nnoremap <buffer> [C :call pymode#motion#move('\v^(class|def)\s', 'b')
nnoremap <buffer> [[ :call pymode#motion#move('\v^(class|def)\s', 'b')
nnoremap <buffer> <silent> \b :call pymode#breakpoint#operate(line('.'))
vnoremap <buffer> <silent> \r :PymodeRun
nnoremap <buffer> <silent> \r :PymodeRun
vnoremap <buffer> ]M :call pymode#motion#vmove('^\s*def\s', '')
vnoremap <buffer> ]] :call pymode#motion#vmove('\v^(class|def)\s', '')
onoremap <buffer> ]M :call pymode#motion#move('^\s*def\s', '')
onoremap <buffer> ]C :call pymode#motion#move('\v^(class|def)\s', '')
onoremap <buffer> ]] :call pymode#motion#move('\v^(class|def)\s', '')
nnoremap <buffer> ]M :call pymode#motion#move('^\s*def\s', '')
nnoremap <buffer> ]C :call pymode#motion#move('\v^(class|def)\s', '')
nnoremap <buffer> ]] :call pymode#motion#move('\v^(class|def)\s', '')
vnoremap <buffer> aM :call pymode#motion#select('^\s*def\s', 0)
onoremap <buffer> aM :call pymode#motion#select('^\s*def\s', 0)
vnoremap <buffer> aC :call pymode#motion#select('^\s*class\s', 0)
onoremap <buffer> aC :call pymode#motion#select('^\s*class\s', 0)
vnoremap <buffer> iM :call pymode#motion#select('^\s*def\s', 1)
onoremap <buffer> iM :call pymode#motion#select('^\s*def\s', 1)
vnoremap <buffer> iC :call pymode#motion#select('^\s*class\s', 1)
onoremap <buffer> iC :call pymode#motion#select('^\s*class\s', 1)
inoremap <buffer> <silent> . .=pymode#rope#complete_on_dot()
let &cpo=s:cpo_save
unlet s:cpo_save
setlocal autoindent
setlocal nobinary
setlocal bufhidden=
setlocal buflisted
setlocal buftype=
setlocal nocindent
setlocal cinkeys=0{,0},0),:,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=+1
setlocal comments=s1:/*,mb:*,ex:*/,://,b:#,:XCOMM,n:>,fb:-
setlocal commentstring=#%s
setlocal complete=.,w,b,u,t,i
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
setlocal nocursorline
setlocal define=^s*\\(def\\|class\\)
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal expandtab
if &filetype != 'python'
setlocal filetype=python
endif
setlocal foldcolumn=0
setlocal foldenable
setlocal foldexpr=pymode#folding#expr(v:lnum)
setlocal foldignore=#
setlocal foldlevel=8
setlocal foldmarker={{{,}}}
setlocal foldmethod=expr
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldtext=pymode#folding#text()
setlocal formatexpr=
setlocal formatoptions=cq
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal grepprg=
setlocal iminsert=0
setlocal imsearch=0
setlocal include=s*\\(from\\|import\\)
setlocal includeexpr=substitute(v:fname,'\\.','/','g')
setlocal indentexpr=pymode#indent#get_indent(v:lnum)
setlocal indentkeys=!^F,o,O,<:>,0),0],0},=elif,=except
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255
setlocal keywordprg=
setlocal nolinebreak
setlocal nolisp
setlocal nolist
setlocal makeprg=
setlocal matchpairs=(:),{:},[:]
setlocal modeline
setlocal modifiable
setlocal nrformats=octal,hex
set number
setlocal number
setlocal numberwidth=4
setlocal omnifunc=pymode#rope#completions
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal quoteescape=\\
setlocal noreadonly
setlocal norelativenumber
setlocal noscrollbind
setlocal shiftwidth=4
setlocal noshortname
setlocal nosmartindent
setlocal softtabstop=4
setlocal nospell
setlocal spellcapcheck=
setlocal spellfile=
setlocal spelllang=en
setlocal statusline=
setlocal suffixesadd=.py
setlocal swapfile
setlocal synmaxcol=3000
if &syntax != 'python'
setlocal syntax=python
endif
setlocal tabstop=4
setlocal tags=
setlocal textwidth=120
setlocal thesaurus=
setlocal noundofile
setlocal nowinfixheight
setlocal nowinfixwidth
setlocal nowrap
setlocal wrapmargin=0
6
normal zo
24
normal zo
129
normal zo
let s:l = 142 - ((39 * winheight(0) + 28) / 56)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
142
normal! 0
lcd ~/Workspaces/python/Python_Modules
wincmd w
2wincmd w
exe 'vert 1resize ' . ((&columns * 30 + 90) / 180)
exe 'vert 2resize ' . ((&columns * 149 + 90) / 180)
tabnext 1
if exists('s:wipebuf')
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToO
let s:sx = expand("<sfile>:p:r")."x.vim"
if file_readable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &so = s:so_save | let &siso = s:siso_save
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
