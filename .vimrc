" general
" set number
syntax on
set tabstop=4

" Download plugins to this directory
call plug#begin("~/.vim/plugged")

" Plugins
Plug 'dense-analysis/ale'
Plug 'preservim/nerdtree'

" After this call, plugins are visible to nvim
call plug#end()

" ALE
let g:ale_fixers = {
			\ 'go': ["goimports"], 
			\ 'python': ["black"],
			\ }
let g:ale_linters = {
			\ 'go': ["gopls"],
			\ 'python': ["pylint"]
			\ }
let g:gofmt_command = "goimports"
let g:ale_completion_enabled = 1
let g:ale_fix_on_save = 1
set number

nnoremap <F4> :NERDTreeToggle<CR>

nnoremap <F3> :NERDTree<CR>

set shiftwidth=4
colorscheme 1989
