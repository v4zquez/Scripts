set number
set mouse=a
set numberwidth=1
set clipboard=unnamed
syntax enable
set showcmd
set ruler
set encoding=utf-8
set showmatch
set sw=2
set relativenumber
set laststatus=2
set noshowmode

filetype indent on
set shiftwidth=4
set cindent

highlight Comment ctermfg=LightGreen

call plug#begin('~/.vim/plugged')

" Themes
" Plug 'morhetz/gruvbox'
" Plug 'dikiaap/minimalist'
" Plug 'ayu-theme/ayu-vim'

" set termguicolors
" let ayucolor="dark"
" colorscheme ayu
" set t_Co=256
" syntax on
" colorscheme minimalist

" IDE
Plug 'easymotion/vim-easymotion'
Plug 'scrooloose/nerdtree'
Plug 'christoomey/vim-tmux-navigator'
Plug 'vim-perl/vim-perl', { 'for': 'perl', 'do': 'make clean carp dancer highlight-all-pragmas moose test-more try-tiny' }

call plug#end()

let NERDTreeQuitOnOpen=1

let mapleader=" "

nmap <Leader>s <Plug>(easymotion-s2)
nmap <Leader>nt :NERDTreeFind<CR>
