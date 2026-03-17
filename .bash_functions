# functions and aliases

mybash() {
    code ~/.dotfiles
}
alias helpfuls=mybash

home() {
    cd ~/xdev/
}

view() {
    local target="${1:-.}"

    if [ -f "$target" ]; then
        explorer.exe /select,"$(wslpath -w "$(realpath "$target")")"
    else
        explorer.exe "$(wslpath -w "$target")"
    fi
}

postit() {
    lua ~/.dotfiles/scripts/note.lua "$1"
}
alias note=postit

dezone() {
    ~/.dotfiles/scripts/rm_zoneid.py "$@"
}

allowance() {
    python -B ~/xdev/allowance/app.py
}
alias chores=allowance

hw() {
    local target
    target="$(python ~/.dotfiles/scripts/hw.py "$@")" || return
    cd "$target" || return
}

ocr() {
    python3 ~/.dotfiles/scripts/ocr.py "$@"
}
alias tesseract=ocr

pals() {
    (
        cd "$HOME/xdev/pal_app" || exit 1
        python3 -m pal_app "$@"
    )
}

winhome() {
    local desktop_path='/mnt/c/Users/logan/OneDrive/Desktop'
    local ss_path='/mnt/c/Users/logan/Pictures/Screenshots'
    local rec_path='/mnt/c/Users/logan/Documents/Sound Recordings'
    local dl_path='/mnt/c/Users/logan/Downloads'

    if [ $# -eq 0 ]; then
        cd "$desktop_path"
        return
    fi

    for arg in "$@"; do
        case "$arg" in
            -o)
                echo -e "${B}${YW}  ${desktop_path}${_X}"
                ;;
            +o)
                echo -e "${B}${YW}  ${desktop_path}${_X}"
                cd "$desktop_path"
                ;;
            -ss)
                echo -e "${B}${YW}  ${ss_path}${_X}"
                ;;
            +ss)
                echo -e "%b\n" "${B}${YW}  ${ss_path}${_X}"
                cd "$ss_path"
                ;;
            +d)
                echo -e "${dl_path}"
                cd "$dl_path"
                return
                ;;
            -d)
                echo -e "${dl_path}"
                return
                ;;
            -r)
                echo "$desktop_path"
                return
                ;;
            -h)
                echo -e "$HELP"
                echo -e "$USAGE [winhome | whome | desktop] [-o | +o] [-ss | +ss] [-r]"
                echo -e "   ss - Screenshots folder"
                echo -e "    o - Windows desktop"
                echo -e "   ${GR}+${_X}[ss | o] : cd and echo path"
                echo -e "   ${GR}-${_X}[ss | o] : echo path only"
                echo -e "          ${GR}-${_X}r : echo plain path"
                return
                ;;
            *)
                echo -e "$ERR Unknown option: '${YW}$arg${_X}'"
                echo -e "$USAGE [winhome | whome | desktop] [-o | +o] [-ss | +ss] [-r]"
                echo -e "   ss - Screenshots folder"
                echo -e "    o - Windows desktop"
                echo -e "   ${GR}+${_X}[ss | o] : cd and echo path"
                echo -e "   ${GR}-${_X}[ss | o] : echo path only"
                echo -e "          ${GR}-${_X}r : echo plain path"
                return 1
                ;;
        esac
    done
}
alias desktop=winhome
alias whome=winhome

summon() {
    local ss_path='/mnt/c/Users/logan/Pictures/Screenshots'
    local ss=$(ls -t "$ss_path"/Screenshot*.png 2>/dev/null | head -n 1)

    if [ -z "$ss" ]; then
        echo "[${RD}error${_X}]: no files found"
        exit 1
    fi

    if [ $# -eq 0 ]; then
        mv "$ss" .
        printf "%b\n" "$OK moved screenshot: ${MG}$(basename "$ss")${_X}"
        return
    fi

    case "$@" in
        +c)
            cp "$ss" .
            printf "%b\n" "$OK copied screenshot: $(basename "${CY}$ss${_X}")"
            ;;
        -c)
            mv "$ss" .
            printf "%b\n" "$OK moved screenshot: $(basename "${CY}$ss${_X}")"
            ;;
        *)
            echo "[${RD}error${_X}] Unknown option: '${YW}$arg${_X}'"
            echo "[${CY}usage${_X}]  summon  [-c | +c]"
            echo "  ${BL}+c${_X}: cp to pwd"
            echo "  ${BL}-c${_X}: mv to pwd"
            return 1
            ;;
    esac
}

fox() {
    powershell.exe -Command "Start-Process firefox \"$@\""
}

flashcards() {
    python ~/.dotfiles/flashcard/app.py
}

gamegenie() {
    python ~/.dotfiles/gamegenie/gamegenie.py "$@"
}
alias cheats=gamegenie

alias vim=nvim
