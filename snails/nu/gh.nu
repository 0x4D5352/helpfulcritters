# Finding Repos with Specific Keywords in the Code, Collecting the Names and Getting a Histogram of Volume, then Combining with Unique Values and Cloning Locally

let org = "org_name_here"

gh search code $"org:($org)" podSecurityContext --extension yaml | table | split row "\n" | parse "{org}/{repo}:{filepath}: {contents}" | reject org | sort-by repo | get repo | histogram | save "podsecuritycontext.json"

gh search code $"org:($org)" securityContext NOT pod --extension yaml | table | split row "\n" | parse "{org}/{repo}:{filepath}: {contents}" | reject org | sort-by repo | get repo | histogram | save "securitycontext_histogram.json"

open podsecuritycontext.json securitycontext_histogram.json | reject quantile percentage frequency | sort-by count --reverse | save security_context_counts_by_repo.json

open ~/security_context_counts_by_repo.json | get value | uniq | each { |repo| gh repo clone $"($org)/($repo)" }


# azure cli tools

let vnets = ["vnets go here"]
let $sp = "service_principal_id"
let role = "role_go_here"


$vnets | each { |vnet| az network vnet list | from json | where name == $vnet | get id.0 | az role assignment create --assignee $sp --role $role --scope $in }
# swap create for delete to remove

let headers = ["header1" "value"]
let api_path = "https://azure.stuff.com"

http get --headers $headers $"($api_path)groups/rules" | flatten | flatten | where status != "INACTIVE" | select name value | where value =~ "azureGroups" | upsert value { |row| $row.value | str replace "Arrays.contains(user.azureGroups," "" } | upsert value { |row| $row.value | str replace ")" "" | str trim } | rename rule_name entra_group_id | save idp_swapper.json


# using `to md` for getting gh repos and putting them in an obsidian note:

gh repo list --limit 64 --json name,updatedAt,description,isFork | from json | move description isFork --after name | to md --pretty | save ~/path/to/obsidian-vault/all_repos.md --append


# semgrepping an org's rep

gh repo list $org | save allrepos.json # i know this doesn't work but assume it does, its just to get the names

open allrepos.json | get name | each { |repo| (gh repo clone $"($org)/($repo)"; cd $repo; semgrep scan $"--output=($repo)-findings.txt --json-output=($repo)-findings.json" --metrics=off --historical-secrets --matching-explanations --max-target-bytes=0 --time ) }

gh repo list $org --no-archived -L 190 --json name | from json | get name |  each { |repo| (gh repo clone $"($org)/($repo)"; cd $repo; semgrep ci; cd .. ) }

gh repo list $org --no-archived -L 190 --json name | from json | get name |  each { |repo| (gh repo clone $"($org)/($repo)"; cd $repo; semgrep scan --output=findings.txt --json-output=findings.json --max-target-bytes=0; cd .. ) }
