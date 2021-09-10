set nu
syntax on
set mouse
set tabstop=4
set nocompatible
filetype on
filetype plugin on
filetype indent on
set cursorline
set cursorcolumn
set shiftwidth=4
set expandtab
set nowrap
set incsearch
set ignorecase
set showmode
set showcmd
set showmatch
set hlsearch
set history=1000
set wildmenu
set wildmode=list:longest
set wildignore=*.docx,*.jpg,*.png,*.gif,*.exe
:colorscheme molokai
" STATUS LINE ------------------------------------------------------------ {{{

" Clear status line when vimrc is reloaded.
set statusline=

" Status line left side.
set statusline+=\ %F\ %M\ %Y\ %R

" Use a divider to separate the left side from the right side.
set statusline+=%=

" Status line right side.
set statusline+=\ ascii:\ %b\ hex:\ 0x%B\ row:\ %l\ col:\ %c\ percent:\ %p%%

" Show the status on the second to last line.
set laststatus=2

" }}}
