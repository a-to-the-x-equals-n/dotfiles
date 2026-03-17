#!/usr/bin/env bash
# setup.sh — wire up dotfiles on a new system

DOTFILES="$HOME/.dotfiles"

source "$DOTFILES/.bash_colors"

OK_MSG="  [${E_B_GR}ok${E_X}]"
ERR_MSG="  [${E_B_RD}error${E_X}]"
SKIP_MSG="  [${E_B_YW}skip${E_X}]"

symlink() {
    local target="$1"   # real file in dotfiles
    local link="$2"     # where the app expects it

    if [ -L "$link" ]; then
        echo -e "$SKIP_MSG  $link already symlinked"
        return
    fi

    if [ -e "$link" ]; then
        echo -e "$SKIP_MSG  $link exists — backing up to $link.bak"
        mv "$link" "$link.bak"
    fi

    ln -s "$target" "$link" \
        && echo -e "$OK_MSG  $link ${E_B_YW}->${E_X} $target" \
        || echo -e "$ERR_MSG  failed to symlink $link"
}

inject_bashrc() {
    local line="$1"
    if grep -qF "$line" "$HOME/.bashrc"; then
        echo -e "$SKIP_MSG  .bashrc already sources $line"
    else
        echo "$line" >> "$HOME/.bashrc" \
            && echo -e "$OK_MSG  added to .bashrc: $line" \
            || echo -e "$ERR_MSG  failed to write to .bashrc"
    fi
}

# ----------------------------------------------------------------

echo -e "\n${E_B_MG}dotfiles setup${E_X}\n"

# -- .bashrc --
echo -e "${E_B_CY}.bashrc${E_X}"
inject_bashrc "[ -f ~/.dotfiles/.bash_exports ]   && source ~/.dotfiles/.bash_exports"
inject_bashrc "[ -f ~/.dotfiles/.bash_functions ] && source ~/.dotfiles/.bash_functions"

# -- micro --
echo -e "\n${E_B_CY}micro${E_X}"
mkdir -p "$HOME/.config/micro"
symlink "$DOTFILES/micro/settings.json"  "$HOME/.config/micro/settings.json"
symlink "$DOTFILES/micro/bindings.json"  "$HOME/.config/micro/bindings.json"
symlink "$DOTFILES/micro/colorschemes"   "$HOME/.config/micro/colorschemes"

echo -e "\n${E_B_GR}done.${E_X} reload your shell: ${E_B_YW}source ~/.bashrc${E_X}\n"
