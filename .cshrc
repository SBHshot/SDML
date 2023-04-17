alias setprompt 'set prompt="$cwd:t% "' 
setprompt # to set the initial prompt 

alias cd 'chdir \!* && setprompt' 
alias pushd 'pushd \!* && setprompt' 
alias popd 'popd \!* && setprompt' 

