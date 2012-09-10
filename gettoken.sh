#! /bin/bash


echo "This will generate a new token for use with the github API."
echo "You must have admin priveleges of the team you want to manipulate."
read -p "Please enter your github username: "
# Just goes to show, I have limited experience with awk
curl -s -u $REPLY -d '{"scopes":["user","public_repo","repo"],"note":"Plone Contributor Agreement Integration"}' \
  https://api.github.com/authorizations | sed -e 's/^[ \n]*//' | awk -F=": " -v RS=", " ' /token/ { print $1}' | cut -c 11- | rev | cut -c 2- | rev



