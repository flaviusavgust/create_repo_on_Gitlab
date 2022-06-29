REPO_NAME=foo1
GITLAB_TOKEN=ut6x1UjRLBEqvNuvSYJT  # Enter your own.

curl -f -X POST \
  -H "PRIVATE-TOKEN: ${GITLAB_TOKEN}" -H "Content-Type:application/json" \
  "https://gitlab-digital.tele2.kz/api/v4/projects" -d "{\"path\": \"${REPO}\", \"visibility\": \"private\"}"
