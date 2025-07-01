# Desktop tools

This describes the various tools used and corresponding configuration

## tool-versions

Most desktop tools are installed using asdf and the corresponding file
~/.tool-versions is:

```
bat 0.25.0
bats 1.12.0
bottom 0.10.2
dust 1.2.0
eza 0.21.6
fd 10.2.0
fzf 0.62.0
golang 1.24.4
just 1.40.0
hyperfine 1.19.0
lazygit 0.52.0
ripgrep 14.1.1
shellcheck 0.10.0
shfmt 3.11.0
starship 1.23.0
tokei 12.1.2 
zoxide 0.9.8
nodejs 24.2.0
```

## bat

A replacement for cat.

Add the following line to ~/.bashrc:

```
alias cat='bat --paging=never'
```

## bats

Bash Automated Testing system.


## bottom

Equivalent to the 'top' command.
Also try installing 'btop' instead.

## dust

Fancy disk usage tool.

Alternatives are 'ncdu', 'gdu', 'dua'.

## eza

Modern replacement to 'ls'.

Add the following line to ~/.bashrc:

```
alias ls='eza'
```

## fd

 better 'find'.

## fzf

Fuzzyfinder application.

Add the following line to ~/.bashrc

```
[ -f ~/.fzf.bash ] && source ~/.fzf.bash
```

## hyperfine

Command line benchmarking.

## lazygit

git TUI.

## ripgrep

A better grep - use the 'rg' command.

## shellcheck

Shell linter.

## shfmt

Shell formatter.

## starship

Allows modifying of the shell prompt. The following configuration
shows the current git status and other miscellaneous criteria.

A useful command is 'starship explain'.

The configuration file used is in ~/.config/starship.toml:

```
# Get editor completions based on the config schema
"$schema" = 'https://starship.rs/config-schema.json'

# Inserts a blank line between shell prompts
add_newline = true

# Replace the '❯' symbol in the prompt with '➜'
[character]
success_symbol = '[➜](bold green)'

[hostname]
ssh_only = false
format = '[$ssh_symbol](bold blue) [$hostname](bold red) '
disabled = false

[directory]
disabled = false
truncation_symbol = '…/'

[battery]
full_symbol = '🔋 '
charging_symbol = '⚡️ '
discharging_symbol = '💀 '

[[battery.display]]
threshold = 10
style = 'bold red'

[python]
disabled = true

[env_var.USER]
disabled = true
default = 'unknown user'

[env_var.SHELL]
disabled = true
variable = 'SHELL'
default = 'unknown shell'

[git_branch]
disabled = false
symbol = '🌱 '
ignore_branches = ['master', 'main']

[git_commit]
disabled = false
commit_hash_length = 6
tag_symbol = '🔖 '

[git_state]
disabled = false
format = '[\($state( $progress_current of $progress_total)\)]($style) '
cherry_pick = '[🍒 PICKING](bold red)'

[git_metrics]
disabled = false
added_style = 'bold blue'
format = '[+$added]($added_style)/[-$deleted]($deleted_style) '

[git_status]
disabled = false
conflicted = '🏳'
ahead = '🏎💨'
behind = '😰'
diverged = '😵'
up_to_date = '✓'
untracked = '🤷'
stashed = '📦'
modified = '📝'
staged = '[++\($count\)](green)'
renamed = '👅'
deleted = '🗑'

[golang]
format = '[🏎💨 $version](bold cyan) '

[jobs]
disabled = true
symbol = '+ '
number_threshold = 4
symbol_threshold = 0

[memory_usage]
disabled = true
threshold = -1
symbol = ' '
style = 'bold dimmed green'

# Disable the package module, hiding it from the prompt completely
[package]
disabled = true

[status]
style = 'bg:blue'
symbol = '🔴 '
success_symbol = '🟢 SUCCESS'
format = '[\[$symbol$common_meaning$signal_name$maybe_int\]]($style) '
map_symbol = true
disabled = false

[sudo]
style = 'bold green'
symbol = '👩‍💻 '
disabled = false

[time]
disabled = false
format = '[ $time ]($style) '
```

Add the following line to ~/.bashrc

```
eval "$($HOME/.asdf/shims/starship init bash)"
```

## tokei
 
Code statistics.

## zoxide

A better 'cd' command.

The following line must be the last line in ~/.bashrc:

```
eval "$($HOME/.asdf/shims/zoxide init bash)"
```

