import polkadot


BUNDLE_DIR = '.vim/bundle'

DOTFILES = [
    polkadot.gitclone('.oh-my-zsh', 'https://github.com/robbyrussell/oh-my-zsh.git'),
    polkadot.gitclone('.dircolors-solarized', 'https://github.com/seebi/dircolors-solarized.git'),
    polkadot.copy('*', 'dotfiles/*'),
    polkadot.mkdir(BUNDLE_DIR),
]

plugins = [
    ('tcomment_vim', 'https://github.com/tomtom/tcomment_vim.git'),
    ('snipmate-snippets', 'https://github.com/honza/vim-snippets.git'),
    ('syntastic', 'https://github.com/scrooloose/syntastic.git'),
    ('tcomment_vim', 'https://github.com/tomtom/tcomment_vim.git'),
    ('tlib_vim', 'https://github.com/tomtom/tlib_vim.git'),
    ('vim-addon-mw-utils', 'https://github.com/MarcWeber/vim-addon-mw-utils.git'),
    ('vim-airline', 'https://github.com/bling/vim-airline'),
    ('vim-colors-solarized', 'https://github.com/altercation/vim-colors-solarized.git'),
    ('vim-fireplace', 'https://github.com/tpope/vim-fireplace.git'),
    ('vim-gitgutter', 'https://github.com/airblade/vim-gitgutter.git'),
    ('vim-javascript', 'https://github.com/pangloss/vim-javascript.git'),
    ('vim-json', 'https://github.com/elzr/vim-json.git'),
    ('vim-jst', 'https://github.com/briancollins/vim-jst.git'),
    ('vim-jsx', 'https://github.com/mxw/vim-jsx.git'),
    ('vim-less', 'https://github.com/groenewege/vim-less'),
    ('vim-snipmate', 'https://github.com/garbas/vim-snipmate.git'),
]

for name, repository in plugins:
    DOTFILES.append(polkadot.gitclone('%s/%s' % (BUNDLE_DIR, name), repository))